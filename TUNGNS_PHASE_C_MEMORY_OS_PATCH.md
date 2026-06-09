# TUNGNS Phase C Memory OS Patch

## Status
Generate ✓
Verify ☐
Publish ☐

## Patch 1: Memory OS skill package
- Create `skills/memory` with durable `long_term` persistence and ephemeral `short_term` store.
- Add typed `MemoryRecord`, `MemoryQuery`, and `MemoryType` schemas.
- Keep the package standard-library-only so it remains backend-agnostic.

## Patch 2: Runtime integration
- Add `memory_path` to backend runtime settings.
- Expose a `MemoryOsAgent` from `backend/app/memory/trading_memory.py`.
- Wire the new memory OS agent into `backend/app/core/runtime.py`.

## Patch 3: Documentation
- Document `skills/memory` in `README.md`.

## Goals
- Establish a Phase C memory OS foundation.
- Preserve single responsibility and package separation.
- Enable future AI/knowledge persistence workflows.
