from utils.colors import Colors

# ======================================================
# ENHANCED DETECTION SIGNALS
# ======================================================

SIGNALS = [
    {
        "category": f"{Colors.CRITICAL}PSYCHOLOGICAL PRESSURE{Colors.END}",
        "pattern": r"\b(urgent|immediately|act\s*now|limited\s*time|final\s*warning|hurry|expires?|deadline|time\s*sensitive|last\s*chance)\b",
        "score": 15,
        "reason": f"{Colors.ORANGE}USES URGENCY TO FORCE QUICK ACTION WITHOUT THINKING.{Colors.END}"
    },
    {
        "category": f"{Colors.ORANGE}GREED MANIPULATION{Colors.END}",
        "pattern": r"\b(reward|lottery|prize|winner|bonus|free|gift|congratulations|selected|jackpot|cash|money|earn|profit)\b",
        "score": 30,
        "reason": f"{Colors.ORANGE}USES REWARDS OR GIFTS TO LURE THE VICTIM.{Colors.END}"
    },
    {
        "category": f"{Colors.CRITICAL}AUTHORITY IMPERSONATION{Colors.END}",
        "pattern": r"\b(bank|support|admin|security\s*team|customer\s*care|meta|facebook|google|microsoft|apple|amazon|paypal|instagram|twitter|netflix|government|irs|tax|police|fbi|legal|court)\b",
        "score": 25,
        "reason": f"{Colors.ORANGE}IMPERSONATES A TRUSTED COMPANY OR AUTHORITY.{Colors.END}"
    },
    {
        "category": f"{Colors.DARK_RED}CREDENTIAL HARVESTING{Colors.END}",
        "pattern": r"\b(login|verify|password|otp|pin|account|access|confirm|authenticate|credentials|username|security\s*code|2fa|validation)\b",
        "score": 25,
        "reason": f"{Colors.ORANGE}ATTEMPTS TO STEAL LOGIN OR AUTHENTICATION DETAILS.{Colors.END}"
    },
    {
        "category": f"{Colors.PURPLE}PLATFORM ABUSE{Colors.END}",
        "pattern": r"\b(t\.me/|telegram|wa\.me/|whatsapp|fb\.com|instagram|discord|signal|snapchat|tiktok|dm\s*me|contact\s*via)\b",
        "score": 20,
        "reason": f"{Colors.ORANGE}USES SOCIAL OR MESSAGING PLATFORMS TO EVADE SECURITY.{Colors.END}"
    },
    {
        "category": f"{Colors.RED}SCAM / THREAT INDICATORS{Colors.END}",
        "pattern": r"\b(scam|phishing|fraud|hack|hacked|misuse|suspicious|threat|compromised|breach|leaked|exposed|malware|virus|ransomware)\b",
        "score": 20,
        "reason": f"{Colors.ORANGE}CONTAINS DIRECT SCAM OR THREAT-RELATED TERMINOLOGY.{Colors.END}"
    },
    {
        "category": f"{Colors.YELLOW}ACCOUNT FEAR TACTICS{Colors.END}",
        "pattern": r"\b(blocked|suspended|terminated|disabled|restricted|deactivated|closed|frozen|locked|violation|unauthorized)\b",
        "score": 20,
        "reason": f"{Colors.ORANGE}USES FEAR OF ACCOUNT LOSS TO MANIPULATE USER ACTION.{Colors.END}"
    },
    {
        "category": f"{Colors.CRITICAL}FINANCIAL MANIPULATION{Colors.END}",
        "pattern": r"\b(payment|transaction|transfer|credit\s*card|debit\s*card|cvv|billing|invoice|refund|charge|withdraw|deposit)\b",
        "score": 22,
        "reason": f"{Colors.ORANGE}ATTEMPTS TO MANIPULATE FINANCIAL TRANSACTIONS OR STEAL PAYMENT INFO.{Colors.END}"
    },
    {
        "category": f"{Colors.RED}MALICIOUS ATTACHMENTS{Colors.END}",
        "pattern": r"\b(download|attachment|file|document|pdf|zip|exe|apk|install|click\s*here|open\s*link)\b",
        "score": 18,
        "reason": f"{Colors.ORANGE}ENCOURAGES DOWNLOADING POTENTIALLY MALICIOUS FILES.{Colors.END}"
    },
    {
        "category": f"{Colors.DARK_RED}CRYPTOCURRENCY SCAMS{Colors.END}",
        "pattern": r"\b(bitcoin|btc|ethereum|eth|crypto|wallet|blockchain|nft|investment|trading|forex|binary|mining)\b",
        "score": 28,
        "reason": f"{Colors.ORANGE}INVOLVES CRYPTOCURRENCY-RELATED SCAM TACTICS.{Colors.END}"
    },
    {
        "category": f"{Colors.PURPLE}ROMANCE / CATFISHING{Colors.END}",
        "pattern": r"\b(love|lonely|relationship|dating|meet|romance|attracted|beautiful|handsome|marry|soulmate)\b",
        "score": 24,
        "reason": f"{Colors.ORANGE}USES EMOTIONAL MANIPULATION TYPICAL OF ROMANCE SCAMS.{Colors.END}"
    },
    {
        "category": f"{Colors.WARNING}JOB / EMPLOYMENT SCAMS{Colors.END}",
        "pattern": r"\b(job|work\s*from\s*home|hiring|employment|opportunity|salary|income|weekly\s*pay|easy\s*money|part\s*time)\b",
        "score": 19,
        "reason": f"{Colors.ORANGE}CHARACTERISTICS OF FRAUDULENT JOB OFFERS.{Colors.END}"
    },
    {
        "category": f"{Colors.CYAN}PERSONAL INFO HARVESTING{Colors.END}",
        "pattern": r"\b(ssn|social\s*security|date\s*of\s*birth|dob|address|full\s*name|mother|maiden|passport|license|aadhar|pan)\b",
        "score": 27,
        "reason": f"{Colors.ORANGE}REQUESTS SENSITIVE PERSONAL IDENTIFICATION INFORMATION.{Colors.END}"
    },
    {
        "category": f"{Colors.ORANGE}FAKE DELIVERY SCAMS{Colors.END}",
        "pattern": r"\b(package|delivery|shipment|courier|parcel|tracking|customs|fedex|ups|dhl|usps|postal)\b",
        "score": 21,
        "reason": f"{Colors.ORANGE}MIMICS DELIVERY NOTIFICATIONS TO STEAL INFO OR MONEY.{Colors.END}"
    },
    {
        "category": f"{Colors.RED}TAX / IRS SCAMS{Colors.END}",
        "pattern": r"\b(tax|irs|refund|audit|penalty|fine|owe|outstanding|arrears|treasury)\b",
        "score": 26,
        "reason": f"{Colors.ORANGE}IMPERSONATES TAX AUTHORITIES TO CREATE FEAR.{Colors.END}"
    }
]