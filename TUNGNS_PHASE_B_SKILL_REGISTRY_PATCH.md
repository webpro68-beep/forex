# TUNGNS Phase B - Skill Registry Patch

## Create folders

```bash
mkdir -p skills/{market-analysis,signal-engine,risk-management,execution,journal,backtesting,shared}
```

## market-analysis

```bash
touch skills/market-analysis/__init__.py
touch skills/market-analysis/trend.py
touch skills/market-analysis/support_resistance.py
touch skills/market-analysis/liquidity.py
touch skills/market-analysis/schemas.py
touch skills/market-analysis/README.md
```

## signal-engine

```bash
touch skills/signal-engine/__init__.py
touch skills/signal-engine/ema_cross.py
touch skills/signal-engine/breakout.py
touch skills/signal-engine/bos.py
touch skills/signal-engine/schemas.py
touch skills/signal-engine/README.md
```

## risk-management

```bash
touch skills/risk-management/__init__.py
touch skills/risk-management/position_size.py
touch skills/risk-management/stop_loss.py
touch skills/risk-management/take_profit.py
touch skills/risk-management/risk_reward.py
touch skills/risk-management/schemas.py
touch skills/risk-management/README.md
```

## execution

```bash
touch skills/execution/__init__.py
touch skills/execution/open_order.py
touch skills/execution/close_order.py
touch skills/execution/modify_order.py
touch skills/execution/schemas.py
touch skills/execution/README.md
```

## journal

```bash
touch skills/journal/__init__.py
touch skills/journal/save_trade.py
touch skills/journal/trade_statistics.py
touch skills/journal/export_journal.py
touch skills/journal/schemas.py
touch skills/journal/README.md
```

## backtesting

```bash
touch skills/backtesting/__init__.py
touch skills/backtesting/run_backtest.py
touch skills/backtesting/metrics.py
touch skills/backtesting/equity_curve.py
touch skills/backtesting/schemas.py
touch skills/backtesting/README.md
```

## shared

```bash
touch skills/shared/__init__.py
touch skills/shared/models.py
touch skills/shared/constants.py
touch skills/shared/exceptions.py
touch skills/shared/enums.py
touch skills/shared/utils.py
```
