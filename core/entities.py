import re
from typing import Dict, List

# ======================================================
# ADVANCED PATTERN DETECTION (ENTITY REGEX)
# ======================================================

ANY_WEBSITE_PATTERN = r"(https?://\S+|\b[a-z0-9\-]+\.[a-z]{2,}\b)"

HIGH_RISK_DOMAIN_PATTERN = (
    r"\b[a-z0-9\-]+\."
    r"(cc|tk|xyz|top|ru|cn|gq|ml|ga|cf|pw|icu|cyou|bond|buzz|cam|click|country|date|"
    r"faith|fit|fun|host|info|kim|lat|loan|men|monster|online|party|pro|rest|racing|"
    r"review|science|stream|support|trade|vip|work|zip|mov|quest|bar|surf|shop|site|"
    r"live|cloud|digital|services|solutions|today|center|company|network|email|press|"
    r"media|world|zone|link|space|website|systems|group|global|secure|update|verify|"
    r"account|login|wallet|crypto|exchange|claim|bonus|reward|alert|promo|deal|offer|"
    r"win|free|cash|money|pay|billing|invoice|refund|tax|gov|legal|court|police|support|help)\b"
)

SHORTENED_URL_PATTERN = (
    r"\b(bit\.ly|tinyurl|t\.co|goo\.gl|ow\.ly|short\.io|rebrand\.ly|is\.gd|soo\.gd|buff\.ly|"
    r"adf\.ly|bc\.vc|cutt\.ly|clk\.sh|clicky\.me|bitly\.com|trib\.al|dlvr\.it|snip\.ly|po\.st|"
    r"tiny\.cc|s2r\.co|bl\.ink|lnkd\.in|fb\.me|lnk\.to|lnk\.co|lnk\.bio|linktr\.ee|t2m\.io|"
    r"shorte\.st|shorturl\.at|v\.gd|qr\.ae|qr\.co|yourls|1url\.com|shortcm\.li|mcaf\.ee|"
    r"aka\.ms|aka\.me|amzn\.to|ebay\.to|g\.co|gg\.gg|git\.io|forms\.gle|rb\.gy|surl\.li|"
    r"surl\.me|lstu\.fr|u\.to|zi\.mu|x\.co|kutt\.it|tiny\.one|go2l\.ink|hyperurl\.co|"
    r"link\.zip|link\.one|plink\.me|urlzs\.com|short\.ly|t\.ly|2u\.pw|3ly\.link|tiny\.pl|"
    r"qrco\.de|lnkfi\.re|bit\.do|soo\.me|y2u\.be|chilp\.it|shrt\.co|cur\.lv|q\.gs|vzturl\.com)"
    r"/\S+"
)

IP_ADDRESS_PATTERN = (
    r"\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}"
    r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b|"
    r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"
)

GLOBAL_PHONE_PATTERN = (
    r"\b(?:\+?[1-9]\d{0,2}[\s\-]?)?"
    r"(?:[6-9]\d{9}|\d{3}[\s\-]?\d{3}[\s\-]?\d{4}|\d{7,12})\b"
)

LONG_NUMBER_PATTERN = r"\b(?!19\d{6}\b|20\d{6}\b)\d{8,16}\b"

EMAIL_PATTERN = (
    r"\b[a-z0-9](?:[a-z0-9._%+-]{0,63})@"
    r"(?:[a-z0-9-]{1,63}\.)+[a-z]{2,10}\b"
)

BITCOIN_ADDRESS_PATTERN = (
    r"\b([13][a-km-zA-HJ-NP-Z1-9]{25,34}|"
    r"bc1[ac-hj-np-z02-9]{11,71})\b"
)

ETHEREUM_ADDRESS_PATTERN = r"(?:\b0x[a-fA-F0-9]{40}\b.*){2,}"

UPI_PATTERN = r"\b[a-z0-9._-]{3,}@(upi|paytm|okaxis|okhdfc|oksbi|ybl|ibl|axl)\b"

PAYMENT_HANDLE_PATTERN = r"\$[a-z0-9_]+"

# ======================================================
# ENTITY EXTRACTION ENGINE
# ======================================================

def extract_entities(message: str) -> Dict[str, List[str]]:
    """
    Extract various entities from the message
    """
    msg = message.lower()

    entities = {
        "domains": re.findall(ANY_WEBSITE_PATTERN, msg),
        "emails": re.findall(EMAIL_PATTERN, msg),
        "phones": re.findall(GLOBAL_PHONE_PATTERN, message),
        "ip_addresses": re.findall(IP_ADDRESS_PATTERN, msg),
        "bitcoin_addresses": re.findall(BITCOIN_ADDRESS_PATTERN, message),
        "ethereum_addresses": re.findall(ETHEREUM_ADDRESS_PATTERN, message),
        "upi_ids": re.findall(UPI_PATTERN, msg),
        "payment_handles": re.findall(PAYMENT_HANDLE_PATTERN, message)
    }

    return entities