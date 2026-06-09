# HedgeMath OS MVP

MVP robot hedging operating system theo kiến trúc Agent + FSM + Risk Guard + Grid Math + Winner Genes.

## Skills Package

A new `skills/` package has been added to support modular strategy building and analysis.

Package structure:
- `skills/market-analysis` — market trend, support/resistance, liquidity analysis.
- `skills/signal-engine` — signal generation for EMA crossovers, breakouts, and structure breaks.
- `skills/risk-management` — position sizing, stop loss, take profit, and risk/reward tools.
- `skills/execution` — order payload builders for open, close, and modify operations.
- `skills/journal` — trade journaling, statistics, and export helpers.
- `skills/backtesting` — lightweight backtesting routines and performance metrics.
- `skills/shared` — shared models, constants, enums, exceptions, and utilities.

Example usage:

- `skills/market-analysis/trend.py`
- `skills/signal-engine/ema_cross.py`

## Chạy nhanh

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
PYTHONPATH=. uvicorn app.main:app --reload --port 8000
```

### Giao diện mới
Giao diện hiện tại đã được thay bằng app `QuantDinger-Vue` trong thư mục `frontend`.

```bash
cd frontend
pnpm install
pnpm dev
```

Mặc định app frontend sẽ kết nối tới backend tại `http://127.0.0.1:8000`.

## Safety

Live trading bị tắt mặc định bằng `ALLOW_LIVE_EXECUTION=false`. Đây là bản MVP mô phỏng/paper-first, không phải lời khuyên đầu tư.
