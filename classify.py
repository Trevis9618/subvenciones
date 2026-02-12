def classify(text: str) -> str:
    """Classify opportunity type: grant, prize, challenge, or unknown.
    This is a lightweight keyword-based classifier for the MVP.
    """
    t = text.lower()

    prize_kw = ["premio", "award", "prize", "ganador", "winners", "competition", "concurso"]
    challenge_kw = ["reto", "challenge", "call for solutions", "open innovation", "poc", "piloto", "proof of concept"]
    grant_kw = ["subvención", "grant", "fondo perdido", "apoyo económico", "subvention", "förderung", "appel à projets", "edital"]

    score_prize = sum(k in t for k in prize_kw)
    score_chal = sum(k in t for k in challenge_kw)
    score_grant = sum(k in t for k in grant_kw)

    if score_chal >= max(score_prize, score_grant) and score_chal > 0:
        return "challenge"
    if score_prize >= max(score_chal, score_grant) and score_prize > 0:
        return "prize"
    if score_grant > 0:
        return "grant"
    return "unknown"
