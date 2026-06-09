# TUNGNS_PHASE_D_GOVERNANCE_OS_PATCH

## Overview

Phase D introduces Governance OS.

Purpose:

* Move rules out of business logic.
* Centralize risk and permissions.
* Create a stable foundation for Evolution OS.

TUNGNS Flow:

```text
Generate
↓
Verify
↓
Publish
```

---

# Folder Structure

```text
governance/
│
├── risk_rules.yaml
├── capital_rules.yaml
├── permissions.yaml
├── schemas.py
├── governance_manager.py
└── __init__.py
```

---

# risk_rules.yaml

Purpose:

Store risk constraints.

Fields:

```text
max_risk_per_trade
max_daily_loss
max_weekly_loss
max_open_positions
minimum_rr
```

Example:

```yaml
max_risk_per_trade: 1.0
max_daily_loss: 3.0
max_weekly_loss: 10.0
max_open_positions: 5
minimum_rr: 2.0
```

---

# capital_rules.yaml

Purpose:

Store capital constraints.

Fields:

```text
starting_balance
max_lot_size
compounding_enabled
capital_allocation
```

Example:

```yaml
starting_balance: 10000
max_lot_size: 1.0
compounding_enabled: true
capital_allocation: 100
```

---

# permissions.yaml

Purpose:

Store system permissions.

Fields:

```text
allow_live_trading
allow_news_trading
allow_scalping
allow_weekend_positions
```

Example:

```yaml
allow_live_trading: false
allow_news_trading: false
allow_scalping: true
allow_weekend_positions: false
```

---

# schemas.py

Define:

```text
RiskRule
CapitalRule
PermissionRule
```

Purpose:

* Standardize Governance data.
* Support future expansion.

---

# governance_manager.py

Single Governance entry point.

Public API:

```python
load_rules()
validate_trade()
validate_position_size()
check_permissions()
```

Governance Manager is the only component allowed to access YAML rule files.

---

# Architecture Rule

Correct:

```text
Agent
↓
Skill
↓
Memory
↓
Governance
↓
Execution
```

Incorrect:

```text
Skill
↓
Read YAML Directly
```

Incorrect:

```text
Agent
↓
Hard-code Rules
```

---

# Forbidden Examples

Wrong:

```python
RiskGuardAgent.max_risk = 1
```

Wrong:

```python
ema_cross.py.read_yaml()
```

Wrong:

```python
execution.py.open("risk_rules.yaml")
```

---

# Single Entry Point

Only:

```text
governance/governance_manager.py
```

may access:

```text
risk_rules.yaml
capital_rules.yaml
permissions.yaml
```

---

# Verify Checklist

```text
Phase D
Governance OS

Generate ✓
Verify ✓
Publish ✓
```

Conditions:

* No Skill reads YAML directly.
* No Agent stores rules.
* Governance Manager is the only rule gateway.
* Rules are externalized from business logic.

---

# Architecture After Phase D

```text
10 Agents
        ↓
100+ Skills
        ↓
Memory OS
        ↓
Governance OS
        ↓
Evolution OS
```

---

# Preparation for Phase E

Next phase:

```text
Phase E
Evolution OS
```

Expected structure:

```text
hooks/
├── before_trade/
├── after_trade/
├── before_signal/
└── after_signal/
```

---

# TUNGNS Principle

Rules do not belong to Agents.

Rules do not belong to Skills.

Rules belong to Governance OS.

Governance creates stability.

Stability enables Evolution.
