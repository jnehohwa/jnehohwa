"""Refresh public GitHub stats without a hosted stats-card service.

Commits are GitHub Search's indexed public commits attributed to this login,
not every commit on every branch. Streaks use the visible contribution calendar
(commits, issues, PRs, etc.), including anonymous private activity if enabled.
"""
import json
import os
import re
import time
from collections import Counter
from datetime import date, datetime, timedelta
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

USER = os.environ.get("STATS_USER", "jnehohwa")
ROOT = Path(__file__).resolve().parents[1]


def fetch(url):
    headers = {"User-Agent": "github-profile-stats", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers=headers), timeout=30) as response:
                return response.read().decode("utf-8")
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def api(path):
    return json.loads(fetch("https://api.github.com/" + path))


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates, self.counts = {}, {}
        self.target = None
        self.label = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "data-date" in attrs:
            self.dates[attrs["id"]] = attrs["data-date"]
        if tag == "tool-tip":
            self.target = attrs.get("for")
            self.label = ""

    def handle_data(self, data):
        if self.target:
            self.label += data

    def handle_endtag(self, tag):
        if tag == "tool-tip" and self.target:
            if self.target in self.dates:
                match = re.match(r"\s*([\d,]+|No) contributions?\b", self.label)
                if not match:
                    raise ValueError("Unexpected contribution calendar label")
                value = match[1]
                self.counts[self.dates[self.target]] = 0 if value == "No" else int(value.replace(",", ""))
            self.target = None


def streaks(days, today):
    longest = run = 0
    best_start = best_end = start = None
    for day, count in sorted(days.items()):
        if count:
            if run == 0:
                start = day
            run += 1
            if run > longest:
                longest, best_start, best_end = run, start, day
        else:
            run = 0
    current = 0
    cursor = today if days.get(today.isoformat(), 0) else today - timedelta(days=1)
    while days.get(cursor.isoformat(), 0):
        current += 1
        cursor -= timedelta(days=1)
    return longest, best_start, best_end, current


def card(title, rows, footnote):
    height = 112 + 38 * len(rows)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="{height}" viewBox="0 0 620 {height}" role="img" aria-label="{escape(title)}">',
             f'<title>{escape(title)}</title>',
             f'<rect x="1" y="1" width="618" height="{height-2}" rx="14" fill="#141321" stroke="#343044"/>',
             '<g font-family="DejaVu Sans,Arial,sans-serif">',
             f'<text x="26" y="40" font-size="22" font-weight="700" fill="#f97316">{escape(title)}</text>']
    for i, (label, value) in enumerate(rows):
        y = 80 + 38 * i
        parts += [f'<text x="26" y="{y}" font-size="16" fill="#ddd6e8">{escape(label)}</text>',
                  f'<text x="590" y="{y}" text-anchor="end" font-size="18" font-weight="700" fill="#fe428e">{escape(str(value))}</text>']
    parts += [f'<text x="26" y="{height-24}" font-size="11" fill="#aaa4b8">{escape(footnote)}</text>', '</g></svg>']
    return "\n".join(parts) + "\n"


def main():
    today = datetime.now(ZoneInfo("Africa/Johannesburg")).date()
    profile = api(f"users/{USER}")
    first = date.fromisoformat(profile["created_at"][:10])
    days = {}
    for year in range(first.year, today.year + 1):
        parser = Calendar()
        parser.feed(fetch(f"https://github.com/users/{USER}/contributions?from={year}-01-01&to={year}-12-31"))
        if not parser.counts:
            raise ValueError(f"Missing calendar for {year}")
        days.update({d: n for d, n in parser.counts.items() if first.isoformat() <= d <= today.isoformat()})
    expected = (today - first).days + 1
    if len(days) != expected:
        raise ValueError(f"Incomplete calendar: expected {expected} days, got {len(days)}")
    commits = api(f"search/commits?q=author%3A{USER}&per_page=1")
    if commits.get("incomplete_results"):
        raise ValueError("Incomplete commit search")
    repos = []
    page = 1
    while True:
        batch = api(f"users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    languages = Counter()
    for repo in repos:
        if not repo["fork"]:
            languages.update(api(f"repos/{repo['full_name']}/languages"))
    longest, start, end, current = streaks(days, today)
    stats = {
        "updated": today.isoformat(), "username": USER,
        "public_indexed_commits": commits["total_count"],
        "profile_contributions_all_time": sum(days.values()),
        "profile_contributions_this_year": sum(n for d, n in days.items() if d.startswith(str(today.year))),
        "longest_streak_days": longest, "longest_streak_start": start,
        "longest_streak_end": end, "current_streak_days": current,
        "public_repositories": profile["public_repos"], "followers": profile["followers"],
        "stars_received": sum(r["stargazers_count"] for r in repos if not r["fork"]),
        "language_bytes": dict(languages.most_common()),
    }
    rows = [("Public commits (indexed)", stats["public_indexed_commits"]),
            ("Profile contributions (all time)", stats["profile_contributions_all_time"]),
            (f"Contributions in {today.year}", stats["profile_contributions_this_year"]),
            ("Longest contribution streak", f"{longest} days"),
            ("Current contribution streak", f"{current} days"),
            ("Public repositories", stats["public_repositories"]),
            ("Stars received / followers", f"{stats['stars_received']} / {stats['followers']}")]
    total = sum(languages.values())
    language_rows = [(name, f"{100 * size / total:.1f}%") for name, size in languages.most_common(6)] if total else [("No public language data", "")]
    outputs = {
        "stats.json": json.dumps(stats, indent=2) + "\n",
        "github-stats.svg": card("Joshua's GitHub Stats", rows, f"Updated {today} | Streaks use GitHub's visible contribution calendar"),
        "top-languages.svg": card("Top Languages", language_rows, f"Updated {today} | Code bytes in owned public repositories, excluding forks"),
    }
    (ROOT / "assets").mkdir(exist_ok=True)
    for name, content in outputs.items():
        (ROOT / "assets" / name).write_text(content, encoding="utf-8")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
