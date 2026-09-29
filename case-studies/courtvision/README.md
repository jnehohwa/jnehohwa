# CourtVision AI: Screenshots and Demo Guide

**Replay-first basketball analytics with FastAPI, Next.js and SwiftUI**

[Project source](https://github.com/jnehohwa/courtvision-ai) · [Full setup instructions](https://github.com/jnehohwa/courtvision-ai/blob/main/README.md) · [Current MVP boundaries](https://github.com/jnehohwa/courtvision-ai/blob/main/docs/mvp-status.md) · [Back to my profile](../../README.md)

## Desktop Preview

![Existing CourtVision desktop dashboard capture](https://raw.githubusercontent.com/jnehohwa/courtvision-ai/main/outputs/courtvision-dashboard-desktop.png)

## Mobile Preview

![Existing CourtVision mobile dashboard capture](https://raw.githubusercontent.com/jnehohwa/courtvision-ai/main/outputs/courtvision-dashboard-mobile.png)

These are existing captures committed in the project repository. They illustrate the replay dashboard rather than a newly hosted deployment.

## What the Demo Shows

- A seeded historical replay fixture with synthetic data.
- A REST snapshot followed by sequenced WebSocket events.
- A changing score, shot map and win-probability timeline.
- Reconnection and polling fallback when streaming is unavailable.
- A backend replay worker and tests for recovery after interruption.

This project does not claim licensed real-time NBA coverage. Public hosting and physical iPhone/TestFlight installation remain pending.

## Run Locally

With Git and Docker Compose installed:

~~~bash
git clone https://github.com/jnehohwa/courtvision-ai.git
cd courtvision-ai
cp .env.example .env
docker compose up --build
~~~

Open the dashboard at **http://localhost:3000**, and API documentation at **http://localhost:8000/docs**.

Follow the main repository README for environment configuration, port conflicts and non-Docker setup. These instructions are documented in the repository; this profile update did not rerun the full application.

## Five-Minute Walkthrough

1. Explain the problem: make basketball game events and model outputs understandable in one dashboard.
2. Open the seeded Boston/New York game and point out the historical replay label.
3. Press Play and follow the score, shot map and probability timeline.
4. Show how the REST snapshot and WebSocket stream work together.
5. Open the worker restart test and explain how it verifies recovery.
6. Finish with the limitations: synthetic fixtures, single replay worker, and hosting still pending.

## Code Worth Discussing

- [Replay worker](https://github.com/jnehohwa/courtvision-ai/blob/main/apps/api/courtvision/worker.py): command validation, claiming pending work and acknowledgement.
- [Worker recovery integration tests](https://github.com/jnehohwa/courtvision-ai/blob/main/apps/api/tests/test_worker_redis_integration.py): interruption, recovery, malformed commands and lock ownership.
- [GitHub Actions](https://github.com/jnehohwa/courtvision-ai/actions): recorded CI results.
- [API modules](https://github.com/jnehohwa/courtvision-ai/tree/main/apps/api/courtvision): models, contracts, inference and replay.

## Questions to Prepare

Why Redis? What happens when the worker stops halfway through? Why keep sequence numbers? How does the browser recover missed events? What changes would multiple workers require? How do you distinguish benchmark inference from a promoted ML artifact?
