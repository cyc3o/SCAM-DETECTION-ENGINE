import re
from typing import Tuple, List
from utils.colors import Colors

# ======================================================
# ADVANCED SUSPICIOUS PATTERN DETECTION
# ======================================================

def detect_suspicious_patterns(message: str) -> Tuple[int, List[str]]:
    """
    Detect additional suspicious patterns
    """
    score = 0
    reasons = []
    msg = message.lower()
    
    # --------------------------------------------------
    # EXCESSIVE PUNCTUATION
    # --------------------------------------------------
    if len(re.findall(r'[!?]{3,}', message)) > 0:
        score += 12
        reasons.append(
            f"{Colors.GRAY}EXCESSIVE PUNCTUATION USED TO CREATE URGENCY OR EXCITEMENT.{Colors.END}"
        )
    
    # --------------------------------------------------
    # EXCESSIVE CAPITALIZATION
    # --------------------------------------------------
    caps_ratio = sum(1 for c in message if c.isupper()) / max(len(message), 1)
    if caps_ratio > 0.5 and len(message) > 20:
        score += 10
        reasons.append(
            f"{Colors.GRAY}EXCESSIVE CAPITALIZATION TO GRAB ATTENTION OR CREATE ALARM.{Colors.END}"
        )
    
    # --------------------------------------------------
    # MULTIPLE CURRENCY SYMBOLS
    # --------------------------------------------------
    currency_count = len(re.findall(r'[$€£¥₹]', message))
    if currency_count >= 2:
        score += 15
        reasons.append(
            f"{Colors.GRAY}MULTIPLE CURRENCY SYMBOLS SUGGESTING FINANCIAL SCAM.{Colors.END}"
        )
    
    # --------------------------------------------------
    # EXCESSIVE EMOJIS
    # --------------------------------------------------
    emoji_pattern = (
        r'[\U0001F600-\U0001F64F'
        r'\U0001F300-\U0001F5FF'
        r'\U0001F680-\U0001F6FF'
        r'\U0001F1E0-\U0001F1FF]'
    )
    emoji_count = len(re.findall(emoji_pattern, message))
    if emoji_count > 5:
        score += 8
        reasons.append(
            f"{Colors.GRAY}EXCESSIVE EMOJI USAGE TYPICAL OF SOCIAL ENGINEERING.{Colors.END}"
        )
    
    # --------------------------------------------------
    # CREDIT CARD–LIKE NUMBER PATTERN
    # --------------------------------------------------
    if re.search(r'\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}', message):
        score += 35
        reasons.append(
            f"{Colors.GRAY}PATTERN RESEMBLES CREDIT CARD NUMBER FORMAT.{Colors.END}"
        )
    
    # --------------------------------------------------
    # BASE64-LIKE STRING DETECTION
    # --------------------------------------------------
    base64_pattern = r'\b[A-Za-z0-9+/]{20,}={0,2}\b'
    if re.search(base64_pattern, message):
        score += 18
        reasons.append(
            f"{Colors.GRAY}CONTAINS BASE64-LIKE ENCODED STRING (POTENTIAL MALWARE).{Colors.END}"
        )
    
    # --------------------------------------------------
    # OBFUSCATED TEXT (L33T / NUMBERS)
    # --------------------------------------------------
    if re.search(r'\b\w*[0-9]\w*[0-9]\w*\b', msg) and len(msg) > 30:
        score += 11
        reasons.append(
            f"{Colors.GRAY}TEXT OBFUSCATION DETECTED (EVADING FILTERS).{Colors.END}"
        )
    
    return score, reasons