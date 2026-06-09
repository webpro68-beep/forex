from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict


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
