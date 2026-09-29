# Interview Preparation Notes

A practical preparation guide for discussing my projects and practising coding questions. This document is a plan, not a record of solved problems or completed interview preparation.

## Project Walkthrough Structure

For each project, prepare a two-minute answer covering:

1. Who had the problem and why it mattered.
2. My actual contribution, including which parts were collaborative or AI-assisted.
3. One implementation decision and an alternative.
4. One failure I investigated and the evidence behind the fix.
5. How the work was tested.
6. Current limitations and the next useful improvement.

Describe decisions I understand. For code built with assistance, be ready to explain, change and test it.

## CourtVision

Use the [demo guide](../case-studies/courtvision/README.md).

Prepare explanations for REST versus WebSocket responsibilities, sequence-based recovery, Redis queues, lock ownership, validation, worker restart tests and the boundary between synthetic replay and unofficial live data.

A useful test to understand is the worker restart integration test. Trace what it arranges, where it stops the first process, and what proves the second process recovers the replay. Do not describe the failure as one I personally debugged unless I can explain that history accurately.

## KuCoNa

Use the [case study](../case-studies/kucona/README.md).

Prepare explanations for choosing WordPress, structuring programme pages, routing registrations through Jotform/Make/Airtable, keeping operational data private, logging integration activity and handing the system over to staff.

Use a real issue from my implementation notes for the debugging example. Planned publishing, attendance and certificate automations should be described as roadmap work.

## PitchPredict

Start with the [repository explanation](https://github.com/jnehohwa/pitch-predict).

Be ready to explain expected goals, Poisson assumptions, date-based backtesting, leakage, Brier score and the small reported improvement from XGBoost. Distinguish the model findings documented in the repo from results I have personally reproduced.

## Coding Practice

Work through these topics in order. Mark them complete only after I can explain and implement the approach without copying.

- [ ] Arrays and hash maps: Two Sum, Contains Duplicate, Valid Anagram.
- [ ] Two pointers: Valid Palindrome, sorted Two Sum.
- [ ] Sliding windows: longest substring without repeated characters.
- [ ] Stacks: Valid Parentheses, Min Stack.
- [ ] Binary search: ordinary search and finding a boundary.
- [ ] Linked lists: reversal and cycle detection.
- [ ] Trees: traversal, maximum depth and inversion.

For each problem, record the brute-force approach, improved approach, time/space complexity, edge cases and executable checks. Use separate names for multiple implementations so one does not overwrite the other.

## A Practice Session

- Solve one problem aloud without assistance first.
- Check empty input, duplicates and boundary cases.
- Explain the complexity.
- Review one project module and make sure I can describe each important step.
- Practise one answer about a design tradeoff.

## Before the Interview

- Run the project I intend to demonstrate.
- Open the demo, source and relevant tests before the call.
- Know the project's current deployment status.
- Prepare a specific answer about my contribution and any tools or assistance used.
- Clarify the role's stack and technical-session format with the recruiter.
