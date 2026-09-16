from enum import Enum
from typing import Dict, Set


class State(Enum):
    START = "start"
    PLAN = "plan"
    EXECUTE = "execute"
    VERIFY = "verify"
    COMPLETE = "complete"
    BLOCKED = "blocked"


class FSMGuardrail:
    """Finite-state-machine guardrail for validating agent state transitions."""

    def __init__(self):
        self.state = State.START

        self.transitions: Dict[State, Set[State]] = {
            State.START: {State.PLAN},
            State.PLAN: {State.EXECUTE, State.BLOCKED},
            State.EXECUTE: {State.VERIFY, State.BLOCKED},
            State.VERIFY: {State.EXECUTE, State.COMPLETE, State.BLOCKED},
            State.COMPLETE: set(),
            State.BLOCKED: set(),
        }

    def can_transition(self, next_state: State) -> bool:
        """Return True if the requested transition is allowed."""
        return next_state in self.transitions[self.state]

    def transition(self, next_state: State) -> None:
        """Move to the requested state if the transition is valid."""
        if not self.can_transition(next_state):
            raise ValueError(
                f"Invalid transition: {self.state.value} -> {next_state.value}"
            )

        self.state = next_state

    def reset(self) -> None:
        """Reset the workflow to its initial state."""
        self.state = State.START
