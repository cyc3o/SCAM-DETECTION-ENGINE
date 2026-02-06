# ======================================================
# 🌍 GLOBAL SCAM LANGUAGE INTELLIGENCE
# HINGLISH + ENGLISH | UPDATED FOR MODERN FRAUD (2024–2026)
# ======================================================

HINGLISH_SCAM_INTELLIGENCE = {

    # -------------------------------
    # BANK / KYC / ACCOUNT BLOCK
    # -------------------------------
    "BANK_KYC_ACCOUNT_BLOCK": [
        r"aapka\s+account",
        r"aapke\s+bank\s+account",
        r"account\s+block",
        r"account\s+suspend",
        r"account\s+band",
        r"kyc\s+pending",
        r"kyc\s+update",
        r"kyc\s+complete",
        r"turant\s+(verify|update|karo|kare)",
        r"abhi\s+(verify|update|karo)",
        r"immediately\s+update",
        r"link\s+(open|karo|click)",
        r"last\s+warning",
        r"final\s+warning",
        r"account\s+band\s+ho\s+jayega",
        r"verify\s+nahin\s+kiya\s+to",
    ],

    # -------------------------------
    # UPI / OTP / REFUND FRAUD
    # -------------------------------
    "UPI_OTP_FRAUD": [
        r"otp\s+(bata|bhej|share|do)",
        r"otp\s+chahiye",
        r"otp\s+confirm",
        r"refund\s+(process|ke\s+liye)",
        r"refund\s+pending",
        r"upi\s+(verify|check|confirm|karo)",
        r"payment\s+reverse",
        r"wrong\s+transaction",
        r"galat\s+transaction",
        r"amount\s+wapas",
        r"refund\s+approve",
        r"upi\s+id\s+share",
    ],

    # -------------------------------
    # DIGITAL ARREST / POLICE / CBI
    # -------------------------------
    "DIGITAL_ARREST_POLICE": [
        r"digital\s+arrest",
        r"police\s+case",
        r"cyber\s+crime",
        r"cbi\s+investigation",
        r"crime\s+branch",
        r"legal\s+case",
        r"fir\s+darj",
        r"aadhaar\s+pe\s+case",
        r"pan\s+card\s+linked\s+crime",
        r"court\s+notice",
        r"warrant\s+issue",
        r"jail\s+ho\s+sakti\s+hai",
        r"arrest\s+ho\s+jaoge",
    ],

    # -------------------------------
    # ELECTRICITY / GAS / WATER
    # -------------------------------
    "UTILITY_SCAMS": [
        r"bijli\s+kat",
        r"power\s+cut",
        r"electricity\s+bill",
        r"bill\s+pending",
        r"aaj\s+last\s+date",
        r"gas\s+connection\s+band",
        r"water\s+connection\s+cut",
        r"service\s+disconnect",
        r"meter\s+issue",
        r"payment\s+receive\s+nahin",
    ],

    # -------------------------------
    # SIM / MOBILE / NETWORK
    # -------------------------------
    "SIM_NETWORK_SCAMS": [
        r"sim\s+block",
        r"number\s+band",
        r"mobile\s+verification",
        r"sim\s+upgrade",
        r"network\s+issue",
        r"reverification",
        r"telecom\s+department",
        r"number\s+deactivate",
    ]
}


ENGLISH_SCAM_INTELLIGENCE = {

    # -------------------------------
    # AUTHORITY / FEAR / LEGAL
    # -------------------------------
    "AUTHORITY_FEAR": [
        r"immediate\s+action",
        r"urgent\s+response",
        r"failure\s+to\s+comply",
        r"final\s+notice",
        r"legal\s+action",
        r"law\s+enforcement",
        r"court\s+order",
        r"arrest\s+warrant",
        r"this\s+is\s+your\s+last\s+chance",
        r"do\s+not\s+ignore",
    ],

    # -------------------------------
    # ACCOUNT SECURITY / BRAND
    # -------------------------------
    "ACCOUNT_SECURITY": [
        r"account\s+suspended",
        r"account\s+locked",
        r"account\s+restricted",
        r"unusual\s+activity",
        r"suspicious\s+login",
        r"security\s+alert",
        r"verify\s+your\s+identity",
        r"verify\s+your\s+account",
        r"confirm\s+your\s+details",
    ],

    # -------------------------------
    # REFUND / PRIZE / GREED
    # -------------------------------
    "REFUND_GREED": [
        r"you\s+have\s+been\s+selected",
        r"congratulations",
        r"claim\s+your\s+reward",
        r"claim\s+your\s+refund",
        r"limited\s+time\s+offer",
        r"exclusive\s+offer",
        r"free\s+gift",
        r"cash\s+reward",
        r"bonus\s+credited",
    ],

    # -------------------------------
    # JOB / WORK FROM HOME
    # -------------------------------
    "JOB_SCAMS": [
        r"work\s+from\s+home",
        r"online\s+job",
        r"easy\s+income",
        r"earn\s+money\s+daily",
        r"no\s+experience\s+required",
        r"part\s+time\s+job",
        r"registration\s+fee",
        r"joining\s+fee",
        r"telegram\s+job",
        r"whatsapp\s+job",
    ],

    # -------------------------------
    # CRYPTO / INVESTMENT
    # -------------------------------
    "CRYPTO_INVESTMENT": [
        r"guaranteed\s+profit",
        r"high\s+return",
        r"risk\s+free\s+investment",
        r"crypto\s+investment",
        r"bitcoin\s+investment",
        r"forex\s+trading",
        r"double\s+your\s+money",
        r"daily\s+profit",
        r"signal\s+group",
    ],

    # -------------------------------
    # ROMANCE / TRUST
    # -------------------------------
    "ROMANCE_TRUST": [
        r"i\s+trust\s+you",
        r"i\s+love\s+you",
        r"i\s+feel\s+lonely",
        r"we\s+have\s+a\s+future",
        r"let\s+us\s+build\s+together",
        r"help\s+me\s+financially",
        r"investment\s+for\s+us",
    ],

    # -------------------------------
    # DELIVERY / PARCEL
    # -------------------------------
    "DELIVERY_SCAMS": [
        r"package\s+on\s+hold",
        r"delivery\s+failed",
        r"customs\s+clearance",
        r"pay\s+delivery\s+fee",
        r"shipment\s+pending",
        r"courier\s+service",
    ]
}