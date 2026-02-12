import httpx
from bs4 import BeautifulSoup

UA = {"User-Agent": "GrantScout/1.0 (+non-commercial; respects robots)"}

def fetch_text(url: str) -> str:
    """Fetch HTML content and return cleaned, plain text.
    Note: PDF handling is not included in this MVP.
    """
    with httpx.Client(timeout=30, follow_redirects=True, headers=UA) as client:
        r = client.get(url)
        r.raise_for_status()
        html = r.text

    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript"]):
        t.decompose()
    text = " ".join(soup.get_text(" ").split())
    return text[:150000]
