import pytest

from fsm import FSMGuardrail


def test_initial_state():
    fsm = FSMGuardrail()
    assert fsm.state == "start"


def test_valid_transition():
    fsm = FSMGuardrail()

    fsm.transition("plan")

    assert fsm.state == "plan"


def test_invalid_transition():
    fsm = FSMGuardrail()

    with pytest.raises(ValueError):
        fsm.transition("execute")

    assert fsm.state == "start"


def test_complete_workflow():
    fsm = FSMGuardrail()

    fsm.transition("plan")
    fsm.transition("execute")
    fsm.transition("verify")
    fsm.transition("complete")

    assert fsm.state == "complete"


def test_terminal_state_blocks_transition():
    fsm = FSMGuardrail()

    fsm.transition("plan")
    fsm.transition("execute")
    fsm.transition("verify")
    fsm.transition("complete")

    assert not fsm.can_transition("execute")


def test_reset():
    fsm = FSMGuardrail()

    fsm.transition("plan")
    fsm.reset()

    assert fsm.state == "start"
