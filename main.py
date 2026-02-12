from fastapi import FastAPI, Query
from datetime import date
from app.db import get_conn

app = FastAPI(title="GrantScout API")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/opps")
def list_opps(
    q: str | None = None,
    opp_type: str | None = None,
    country_ok: str | None = None,
    tag: str | None = None,
    deadline_before: date | None = None,
    limit: int = Query(50, ge=1, le=200),
):
    where = []
    params = []

    if q:
        where.append("(title ILIKE %s OR summary ILIKE %s OR org_name ILIKE %s)")
        params += [f"%{q}%", f"%{q}%", f"%{q}%"]
    if opp_type:
        where.append("opp_type = %s")
        params.append(opp_type)
    if country_ok:
        where.append("(%s = ANY(countries_eligible) OR accepts_international = TRUE)")
        params.append(country_ok)
    if tag:
        where.append("%s = ANY(industry_tags)")
        params.append(tag)
    if deadline_before:
        where.append("(deadline IS NOT NULL AND deadline <= %s)")
        params.append(deadline_before)

    sql = "SELECT * FROM opportunities"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY deadline NULLS LAST, id DESC LIMIT %s"
    params.append(limit)

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
    return rows
