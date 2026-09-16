from agent import GuardedAgent
from fsm import State


def main():
    agent = GuardedAgent()

    print("Agent FSM Guardrails Demo\n")

    agent.request_transition(State.PLAN)
    agent.request_transition(State.EXECUTE)

    # Invalid transition: execution cannot skip verification.
    agent.request_transition(State.COMPLETE)

    agent.request_transition(State.VERIFY)
    agent.request_transition(State.COMPLETE)


if __name__ == "__main__":
    main()
