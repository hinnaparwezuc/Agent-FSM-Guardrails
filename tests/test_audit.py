import json

from audit import AuditLogger


def test_audit_logger_creates_event(tmp_path):
    log_file = tmp_path / "audit.jsonl"

    logger = AuditLogger(str(log_file))

    logger.log_transition(
        from_state="start",
        to_state="plan",
        allowed=True,
        reason="Test transition",
    )

    assert log_file.exists()

    with log_file.open("r", encoding="utf-8") as file:
        event = json.loads(file.readline())

    assert event["from_state"] == "start"
    assert event["to_state"] == "plan"
    assert event["allowed"] is True
    assert event["reason"] == "Test transition"


def test_blocked_transition_is_recorded(tmp_path):
    log_file = tmp_path / "audit.jsonl"

    logger = AuditLogger(str(log_file))

    logger.log_transition(
        from_state="execute",
        to_state="complete",
        allowed=False,
        reason="Invalid transition",
    )

    with log_file.open("r", encoding="utf-8") as file:
        event = json.loads(file.readline())

    assert event["allowed"] is False
    assert event["from_state"] == "execute"
    assert event["to_state"] == "complete"
