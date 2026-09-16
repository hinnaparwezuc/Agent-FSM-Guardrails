from fsm import FSMGuardrail


class GuardedAgent:
    """Agent wrapper that validates actions through an FSM guardrail."""

    def __init__(self):
        self.guardrail = FSMGuardrail()

    def request_transition(self, next_state: str) -> bool:
        """Attempt a state transition through the guardrail."""

        previous_state = self.guardrail.state

        if not self.guardrail.can_transition(next_state):
            print(
                f"BLOCKED: {previous_state} -> {next_state}"
            )
            return False

        self.guardrail.transition(next_state)

        print(
            f"ALLOWED: {previous_state} -> {next_state}"
        )

        return True
