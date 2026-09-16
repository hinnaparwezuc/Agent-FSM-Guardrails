import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


class AuditLogger:

    def __init__(self, log_path: str = "logs/audit.jsonl"):
        self.log_path = Path(log_path)

        # Create the logs directory automatically if needed.
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def log_transition(
        self,
        from_state: str,
        to_state: str,
        allowed: bool,
        reason: Optional[str] = None,
    ) -> None:
        """Record an attempted FSM transition."""

        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "from_state": from_state,
            "to_state": to_state,
            "allowed": allowed,
            "reason": reason,
        }

        with self.log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(event) + "\n")
