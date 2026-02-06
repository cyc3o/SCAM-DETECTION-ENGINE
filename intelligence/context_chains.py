# ======================================================
# 🧠 CONTEXT INTELLIGENCE CHAINS
# ======================================================

CONTEXT_CHAINS = {
    "INDIAN_BANKING_PHISHING": {
        "keywords": ["kyc", "aadhaar", "pan", "link", "urgent", "verify", "account", "bank"],
        "min_matches": 3,
        "score": 45,
        "region": "INDIA"
    },
    "INDIAN_DIGITAL_ARREST": {
        "keywords": ["digital arrest", "police", "cbi", "court", "legal action", "warrant", "case"],
        "min_matches": 3,
        "score": 50,
        "region": "INDIA"
    },
    "INDIAN_UPI_FRAUD": {
        "keywords": ["upi", "refund", "verify", "otp", "payment", "paytm", "phonepe", "gpay"],
        "min_matches": 3,
        "score": 42,
        "region": "INDIA"
    },
    "INDIAN_UTILITY_SCAM": {
        "keywords": ["electricity", "bill", "power cut", "disconnect", "urgent", "payment", "overdue"],
        "min_matches": 3,
        "score": 38,
        "region": "INDIA"
    },
    "US_IRS_PHISHING": {
        "keywords": ["irs", "tax", "refund", "link", "verify", "payment", "owe", "audit"],
        "min_matches": 3,
        "score": 48,
        "region": "USA"
    },
    "US_SSA_SCAM": {
        "keywords": ["social security", "ssn", "suspension", "suspended", "verify", "number", "compromised"],
        "min_matches": 3,
        "score": 47,
        "region": "USA"
    },
    "US_ECOMMERCE_SCAM": {
        "keywords": ["amazon", "refund", "verify", "account", "suspended", "order", "payment"],
        "min_matches": 3,
        "score": 40,
        "region": "USA"
    },
    "US_P2P_PAYMENT_FRAUD": {
        "keywords": ["zelle", "cashapp", "venmo", "payment", "issue", "verify", "refund", "cancel"],
        "min_matches": 3,
        "score": 44,
        "region": "USA"
    },
    "US_LEGAL_THREAT": {
        "keywords": ["warrant", "court", "arrest", "legal", "lawsuit", "attorney", "comply"],
        "min_matches": 3,
        "score": 46,
        "region": "USA"
    },
    "ROMANCE_TO_CRYPTO": {
        "keywords": ["love", "investment", "crypto", "bitcoin", "trust", "opportunity", "help"],
        "min_matches": 4,
        "score": 43,
        "region": "GLOBAL"
    }
}