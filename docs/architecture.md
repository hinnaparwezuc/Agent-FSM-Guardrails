# Architecture

Agent FSM Guardrails separates probabilistic agent decision-making from
deterministic workflow enforcement.

## Core Flow

1. An agent proposes its next action or workflow state.
2. The FSM guardrail receives the proposed transition.
3. The guardrail compares the request against the allowed transition graph.
4. Valid transitions are executed.
5. Invalid transitions are rejected before execution.
6. Transition outcomes can be recorded for auditing and debugging.

## Components

### Agent

The agent is responsible for proposing actions. It does not have authority
to directly modify workflow state.

### FSM Guardrail

The guardrail maintains the current state and validates proposed transitions.

Example workflow:

START -> PLAN -> EXECUTE -> VERIFY -> COMPLETE

An attempt to transition directly from EXECUTE to COMPLETE is rejected
because verification cannot be skipped.

### Workflow Configuration

Workflow definitions are stored separately from agent logic so that
different state machines can eventually be configured without modifying
the core validation engine.

### Testing

Automated tests verify:

- valid state transitions
- invalid transition rejection
- terminal-state behavior
- workflow completion
- state reset behavior

## Planned Architecture

Future versions will support:

- JSON-based workflow loading
- transition audit logs
- action-level permissions
- configurable failure states
- LLM agent integration
- structured transition events
