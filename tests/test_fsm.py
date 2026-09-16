import pytest

from fsm import FSMGuardrail, State


def test_initial_state():
    fsm = FSMGuardrail()

    assert fsm.state == State.START


def test_valid_transition():
    fsm = FSMGuardrail()

    fsm.transition(State.PLAN)

    assert fsm.state == State.PLAN


def test_invalid_transition():
    fsm = FSMGuardrail()

    with pytest.raises(ValueError):
        fsm.transition(State.EXECUTE)

    assert fsm.state == State.START


def test_complete_workflow():
    fsm = FSMGuardrail()

    fsm.transition(State.PLAN)
    fsm.transition(State.EXECUTE)
    fsm.transition(State.VERIFY)
    fsm.transition(State.COMPLETE)

    assert fsm.state == State.COMPLETE


def test_cannot_leave_complete_state():
    fsm = FSMGuardrail()

    fsm.transition(State.PLAN)
    fsm.transition(State.EXECUTE)
    fsm.transition(State.VERIFY)
    fsm.transition(State.COMPLETE)

    with pytest.raises(ValueError):
        fsm.transition(State.EXECUTE)


def test_reset():
    fsm = FSMGuardrail()

    fsm.transition(State.PLAN)
    fsm.reset()

    assert fsm.state == State.START
