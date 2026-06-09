# TUNGNS Phase C Memory OS Patch

## Status
Generate ✓
Verify ☐
Publish ☐

## Status
Generate ✓
Verify ✓
Publish ☐

## Patch 1: Memory OS skill package
- Create `skills/memory` with durable `long_term` persistence and ephemeral `short_term` store.
- Add typed `MemoryRecord`, `MemoryQuery`, and `MemoryType` schemas.
- Keep the package standard-library-only so it remains backend-agnostic.

## Patch 2: Runtime integration
- Add `memory_path` to backend runtime settings.
- Expose a `MemoryOsAgent` from `backend/app/memory/trading_memory.py`.
- Add `MemoryStore` and `short_memory` runtime support in `backend/app/core/runtime.py`.
- Wire the new memory OS agent into `backend/app/core/runtime.py`.

## Patch 3: Memory API
- Add `POST /api/v1/memory/short-term/save` for short-term memory writes.
- Add `GET /api/v1/memory/short-term/recent` for recent short-term retrieval.
- Preserve long-term memory endpoints for durable records.

## Patch 4: Memory UI
- Add a hidden frontend memory page at `/memory` for short-term save and query workflows.
- Add frontend API bindings in `frontend/src/api/memory.js`.

## Patch 5: Documentation
- Document `skills/memory` and short-term memory API in `README.md`.

## Goals
- Establish a Phase C memory OS foundation.
- Preserve single responsibility and package separation.
- Enable future AI/knowledge persistence workflows.
