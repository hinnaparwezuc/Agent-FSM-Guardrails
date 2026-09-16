import json
from pathlib import Path
from typing import Dict, Set


class FSMGuardrail:
    """Validates agent workflow transitions using a configurable FSM."""

    def __init__(self, config_path: str = "config/workflow.json"):
        self.config_path = Path(config_path)

        self.initial_state: str
        self.transitions: Dict[str, Set[str]]

        self._load_config()

        self.state = self.initial_state

    def _load_config(self) -> None:
        """Load states and allowed transitions from a JSON workflow."""

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Workflow configuration not found: {self.config_path}"
            )

        with self.config_path.open("r", encoding="utf-8") as file:
            config = json.load(file)

        if "initial_state" not in config or "states" not in config:
            raise ValueError(
                "Workflow configuration must define "
                "'initial_state' and 'states'."
            )

        self.initial_state = config["initial_state"]

        self.transitions = {
            state: set(allowed_states)
            for state, allowed_states in config["states"].items()
        }

        if self.initial_state not in self.transitions:
            raise ValueError(
                f"Initial state '{self.initial_state}' "
                "is not defined in workflow states."
            )

    def can_transition(self, next_state: str) -> bool:
        """Return whether the requested transition is allowed."""
        return next_state in self.transitions.get(self.state, set())

    def transition(self, next_state: str) -> None:
        """Move to the next state when the transition is valid."""

        if not self.can_transition(next_state):
            raise ValueError(
                f"Invalid transition: {self.state} -> {next_state}"
            )

        self.state = next_state

    def reset(self) -> None:
        """Reset the workflow to its configured initial state."""
        self.state = self.initial_state
