import re
import dateparser
from langdetect import detect
from urllib.parse import urlparse

def detect_lang(text: str) -> str:
    try:
        return detect(text[:4000])
    except Exception:
        return "unknown"

def extract_deadline(text: str):
    patterns = [
        r"(fecha l[ií]mite|cierre|deadline|closing date|date limite|fecha de cierre)\s*[:\-]?\s*(.{0,60})",
    ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            candidate = m.group(2)
            dt = dateparser.parse(candidate, languages=None)
            if dt:
                return dt.date()
    return None

def extract_amount(text: str):
    t = text.lower().replace(",", "")
    m = re.search(r"(hasta|up to|maximum|max)\s*([$€£]?\s*\d+(?:\.\d+)?)\s*(mxn|usd|eur|gbp)?", t)
    if m:
        val = float(re.sub(r"[^\d\.]", "", m.group(2)))
        cur = m.group(3) or ("USD" if "$" in m.group(2) else None)
        return (None, val, (cur.upper() if cur else None))
    return (None, None, None)

def domain(url: str) -> str:
    return urlparse(url).netloc
