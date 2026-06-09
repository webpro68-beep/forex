from __future__ import annotations

import json
import sys
from pathlib import Path

from identity.identity_manager import IdentityManager


def main():
    repo_root = Path(__file__).resolve().parents[1]
    mgr = IdentityManager()
    violations = mgr.scan_for_violations(repo_root)
    print(json.dumps(violations, indent=2))
    # consider violations if any list is non-empty
    any_viol = any(len(v) > 0 for v in violations.values())
    if any_viol:
        print("Policy violations detected", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
