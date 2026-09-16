from fsm import FSMGuardrail, State


class GuardedAgent:

    def __init__(self):
        self.guardrail = FSMGuardrail()

    def request_transition(self, next_state: State) -> bool:
        """
        Attempt to transition the agent to a new state.

        Returns True when the transition is allowed and False when blocked.
        """
        if not self.guardrail.can_transition(next_state):
            print(
                f"BLOCKED: {self.guardrail.state.value} "
                f"-> {next_state.value}"
            )
            return False

        previous_state = self.guardrail.state
        self.guardrail.transition(next_state)

        print(
            f"ALLOWED: {previous_state.value} "
            f"-> {next_state.value}"
        )

        return True
