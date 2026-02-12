# GrantScout (MVP)

MVP to discover and index grants, prizes, and innovation challenges from seed sources (RSS/pages).
- FastAPI API (`/opps`)
- Neon Postgres for storage
- GitHub Actions scheduled ingest

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export DATABASE_URL="postgresql://..."
python - << 'PY'
import os, psycopg
sql=open("migrations/001_init.sql","r",encoding="utf-8").read()
with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
  conn.execute(sql)
  conn.commit()
print("migrated")
PY
uvicorn app.main:app --reload
```

## Run ingest locally
```bash
export DATABASE_URL="postgresql://..."
python scripts/run_ingest.py
```

## GitHub Actions
Add `DATABASE_URL` as a repository secret:
Settings -> Secrets and variables -> Actions -> New repository secret.
