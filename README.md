# Agent FSM Guardrails

A finite-state-machine (FSM) validation layer for constraining AI agent workflows through deterministic state transitions.

> **Status:** Early development — the core FSM structure, transition validation, configuration, tests, and demo workflow are currently being built and refined.

## Problem

LLM-based agents can behave unpredictably, including skipping required workflow steps or attempting actions outside an expected sequence.

This project explores using a deterministic finite-state machine as a guardrail between an agent's proposed action and its execution.

Instead of allowing an agent to directly control workflow state, proposed transitions are checked against a predefined set of allowed transitions.

## Concept

A workflow may define a sequence such as:

```text
START → PLAN → EXECUTE → VERIFY → COMPLETE
