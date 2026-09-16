from agent import GuardedAgent


def main():
    agent = GuardedAgent()

    print("Agent FSM Guardrails Demo\n")

    agent.request_transition("plan")
    agent.request_transition("execute")

    # Invalid: verification cannot be skipped.
    agent.request_transition("complete")

    agent.request_transition("verify")
    agent.request_transition("complete")


if __name__ == "__main__":
    main()
