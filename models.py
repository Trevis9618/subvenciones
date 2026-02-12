from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class SourceIn(BaseModel):
    name: str
    url: str
    kind: str  # rss|page|sitemap
    country_hint: Optional[str] = None
    language_hint: Optional[str] = None

class OpportunityOut(BaseModel):
    title: str
    org_name: str | None = None
    opp_type: str | None = None
    country: str | None = None
    countries_eligible: List[str] | None = None
    accepts_international: bool | None = None
    amount_min: float | None = None
    amount_max: float | None = None
    currency: str | None = None
    open_date: date | None = None
    deadline: date | None = None
    industry_tags: List[str] | None = None
    stage: str | None = None
    language: str | None = None
    summary: str | None = None
    raw_url: str
    source_domain: str | None = None
