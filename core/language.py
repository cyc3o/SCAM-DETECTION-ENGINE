import re
from typing import Tuple, Set, List

from intelligence.phrases import INDIAN_SCAM_PHRASES, US_SCAM_PHRASES
from intelligence.global_scam_language_intelligence import (
    HINGLISH_SCAM_INTELLIGENCE,
    ENGLISH_SCAM_INTELLIGENCE
)
from utils.colors import Colors

# ======================================================
# LANGUAGE & PHRASE DETECTION ENGINE
# ======================================================

def detect_language_style(message: str) -> Tuple[Set[str], int, List[str]]:
    """
    Detect language style and scam phrases
    """
    msg = message.lower()
    languages: Set[str] = set()
    score = 0
    reasons: List[str] = []

    # --------------------------------------------------
    # EXISTING INDIAN SCAM LANGUAGE DETECTION
    # --------------------------------------------------
    indian_matches = 0
    for phrase_list in INDIAN_SCAM_PHRASES.values():
        for pattern in phrase_list:
            if re.search(pattern, msg):
                indian_matches += 1

    if indian_matches >= 2:
        languages.add("HINDI/HINGLISH")
        score += 20
        reasons.append(
            f"{Colors.GRAY}INDIAN SCAM LANGUAGE PATTERN DETECTED (HINGLISH/HINDI).{Colors.END}"
        )

    # --------------------------------------------------
    # EXISTING US AUTHORITY-STYLE SCAM DETECTION
    # --------------------------------------------------
    us_matches = 0
    for phrase_list in US_SCAM_PHRASES.values():
        for pattern in phrase_list:
            if re.search(pattern, msg):
                us_matches += 1

    if us_matches >= 2:
        languages.add("ENGLISH-US")
        score += 18
        reasons.append(
            f"{Colors.GRAY}US AUTHORITY-STYLE SCAM LANGUAGE DETECTED.{Colors.END}"
        )

    # --------------------------------------------------
    # NEW: EXTRA SCAM LANGUAGE INTELLIGENCE (HINGLISH)
    # --------------------------------------------------
    for category, patterns in HINGLISH_SCAM_INTELLIGENCE.items():
        for pattern in patterns:
            if re.search(pattern, msg):
                languages.add("HINGLISH")
                score += 5
                reasons.append(
                    f"{Colors.GRAY}HINGLISH SCAM PHRASE DETECTED ({category}).{Colors.END}"
                )
                break  # one hit per category is enough

    # --------------------------------------------------
    # NEW: EXTRA SCAM LANGUAGE INTELLIGENCE (ENGLISH)
    # --------------------------------------------------
    for category, patterns in ENGLISH_SCAM_INTELLIGENCE.items():
        for pattern in patterns:
            if re.search(pattern, msg):
                languages.add("ENGLISH-SCAM")
                score += 4
                reasons.append(
                    f"{Colors.GRAY}ENGLISH SCAM PHRASE DETECTED ({category}).{Colors.END}"
                )
                break

    # --------------------------------------------------
    # DEFAULT LANGUAGE FALLBACK
    # --------------------------------------------------
    if not languages:
        languages.add("ENGLISH")

    return languages, score, reasons