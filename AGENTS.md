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

- `app/config.py` reads all settings from env vars via `python-dotenv` (loads `.env` at import).
- Copy `.env.example` to `.env` for local dev — no secrets should be hardcoded.
- `Settings` raises `ValueError` if `SECRET_KEY` is missing.
- `.env` is gitignored; don't commit secrets.

## Structure

- `app/main.py` — FastAPI entrypoint (still empty: no `app = FastAPI()` yet).
- `app/` packages: `routes/`, `schemas/`, `repositories/`, `services/`, `dependencies/`, `utils/`, `database/`.
- `app/database/database.py` — SQLAlchemy 2.0: `engine`, `SessionLocal`, `Base` (DeclarativeBase), `get_db` dependency. SQLite default via `DATABASE_URL` (default `sqlite:///./app.db`).
- `app/database/models.py` — SQLAlchemy models (inherit `Base`).
- `app/templates/` and `app/static/` are non-Python dirs (tracked via `.gitkeep`).
- Root `main.py` is the original uv scaffold script, not part of the app.

## Platform

- **Windows** — paths use `\`, shell commands use PowerShell semantics.
