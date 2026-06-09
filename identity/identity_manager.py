from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import Any


@dataclass
class IdentityManager:
    mission: str = "Transform Experience into Evolution"
    vision: str = "AI Capability OS -> Enterprise OS -> Evolution"
    principles: tuple[str, ...] = (
        "Small Files",
        "Single Responsibility",
        "Skills First",
        "Memory First",
        "Governance First",
        "Hooks First",
    )

    def verify_structure(self, base_path: str | Path) -> Dict[str, bool]:
        base = Path(base_path)
        checks: Dict[str, bool] = {}
        checks["backend_exists"] = (base / "backend").exists()
        checks["skills_exists"] = (base / "skills").exists()
        checks["memory_exists"] = (base / "memory").exists()
        checks["governance_exists"] = (base / "governance").exists()
        checks["hooks_exists"] = (base / "hooks").exists()
        checks["tests_exists"] = (base / "tests").exists()
        return checks

    def load_config(self, path: str | Path | None = None) -> Dict[str, Any]:
        config_path = Path(path) if path else Path(__file__).resolve().parent / "config.yaml"
        if not config_path.exists():
            return {"error": "config not found"}
        data: Dict[str, Any] = {}
        with config_path.open("r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" not in line:
                    continue
                key, value = [p.strip() for p in line.split(":", 1)]
                data[key] = self._cast_value(value)
        return data

    @staticmethod
    def _cast_value(value: str) -> Any:
        lowered = value.lower()
        if lowered in {"true", "false"}:
            return lowered == "true"
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value
