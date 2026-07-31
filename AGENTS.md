# ProyectoFinalFastAPI

## Quick start

```bash
uv sync              # install deps (uses uv.lock)
uv run python main.py                # root scaffold script (not the app)
uv run uvicorn app.main:app --reload # dev server (once the app exists)
```

## Toolchain

- **Package manager**: `uv` — use `uv add`, `uv remove`, never `pip install`.
- **Python**: >=3.10 (pinned in `.python-version`).
- **No test/lint/format configured yet** — if adding, the `.gitignore` already accounts for `.ruff_cache/` and `.mypy_cache/`.

## Env

- `python-dotenv` is a dependency — `.env` files will be loaded at runtime.
- `.env` is gitignored; don't commit secrets.

## Structure

- `app/main.py` — FastAPI entrypoint (still empty: no `app = FastAPI()` yet).
- `app/` packages: `routes/`, `schemas/`, `repositories/`, `services/`, `dependencies/`, `utils/`, `database/`.
- `app/templates/` and `app/static/` are non-Python dirs (tracked via `.gitkeep`).
- Root `main.py` is the original uv scaffold script, not part of the app.

## Platform

- **Windows** — paths use `\`, shell commands use PowerShell semantics.
