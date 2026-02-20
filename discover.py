import feedparser
from bs4 import BeautifulSoup
import httpx
from urllib.parse import urljoin, urlparse

UA = {"User-Agent": "GrantScout/1.0 (+non-commercial; respects robots)"}

def _domain(u: str) -> str:
    return urlparse(u).netloc

def discover_from_rss(rss_url: str) -> list[str]:
    feed = feedparser.parse(rss_url)
    links: list[str] = []
    for e in feed.entries[:200]:
        if getattr(e, "link", None):
            links.append(e.link)
    return list(dict.fromkeys(links))

def discover_from_page(page_url: str) -> list[str]:
    with httpx.Client(timeout=30, follow_redirects=True, headers=UA) as client:
        r = client.get(page_url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

    links: list[str] = []
    for a in soup.select("a[href]"):
        href = a.get("href")
        if not href:
            continue
        u = urljoin(page_url, href)
        if u.startswith("http"):
            links.append(u)
    return list(dict.fromkeys(links))[:500]
