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

- `app/main.py` — FastAPI entrypoint: creates `app`, runs `Base.metadata.create_all` in lifespan, includes routers.
- `app/` packages: `routes/`, `schemas/`, `repositories/`, `services/`, `dependencies/`, `utils/`, `database/`. Pattern: `routes` → `services` → `repositories` → SQLAlchemy; schemas in `schemas/`.
- `httpx` is a dev dependency for `TestClient` (run lifespan via `with TestClient(app) as client:`).
- `app/database/database.py` — SQLAlchemy 2.0: `engine`, `SessionLocal`, `Base` (DeclarativeBase), `get_db` dependency. SQLite default via `DATABASE_URL` (default `sqlite:///./app.db`).
- `app/database/models.py` — SQLAlchemy models (inherit `Base`).
- `app/templates/` and `app/static/` are non-Python dirs (tracked via `.gitkeep`).
- Root `main.py` is the original uv scaffold script, not part of the app.

## Conventions

- Layered architecture: `routes` → `services` (business rules, HTTPExceptions) → `repositories` (SQLAlchemy queries) → DB.
- All DB/JSON field names in `snake_case` (incl. `given_name`, `family_name`, `phone_number`).
- Type hints on every function signature; keep functions small and reusable.
- Comments only where necessary (rarely).
- Commit often with descriptive Spanish messages; `app.db` (SQLite file) is gitignored — never commit it.

## Platform

- **Windows** — paths use `\`, shell commands use PowerShell semantics.
