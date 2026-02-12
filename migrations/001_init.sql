CREATE TABLE IF NOT EXISTS sources (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  url TEXT UNIQUE NOT NULL,
  kind TEXT NOT NULL, -- rss|page|sitemap
  country_hint TEXT,
  language_hint TEXT,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS opportunities (
  id BIGSERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  org_name TEXT,
  opp_type TEXT,                 -- grant|prize|challenge|accelerator|in_kind
  source_kind TEXT,              -- gov|corp|ngo|university|multilateral|unknown

  country TEXT,
  countries_eligible TEXT[],     -- array
  accepts_international BOOLEAN DEFAULT FALSE,

  amount_min DOUBLE PRECISION,
  amount_max DOUBLE PRECISION,
  currency TEXT,

  open_date DATE,
  deadline DATE,

  industry_tags TEXT[],          -- array
  stage TEXT,                    -- idea|mvp|traction|scale

  language TEXT,
  summary TEXT,
  raw_url TEXT UNIQUE NOT NULL,
  source_domain TEXT,

  extracted_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_opps_type ON opportunities(opp_type);
CREATE INDEX IF NOT EXISTS idx_opps_deadline ON opportunities(deadline);
CREATE INDEX IF NOT EXISTS idx_opps_country ON opportunities(country);
CREATE INDEX IF NOT EXISTS idx_opps_tags ON opportunities USING GIN(industry_tags);
CREATE INDEX IF NOT EXISTS idx_opps_eligible ON opportunities USING GIN(countries_eligible);
