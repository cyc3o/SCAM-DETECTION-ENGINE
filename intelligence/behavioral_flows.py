# ======================================================
# 🧬 BEHAVIORAL FLOW PATTERNS
# ======================================================

BEHAVIORAL_FLOWS = [
    {
        "name": "AUTHORITY_FEAR_URGENCY_ACTION",
        "sequence": [
            ["bank", "irs", "police", "support", "admin", "security"],
            ["suspended", "blocked", "compromised", "unauthorized", "violation"],
            ["urgent", "immediately", "now", "today", "deadline"],
            ["verify", "click", "login", "confirm", "update", "call"]
        ],
        "score": 35,
        "description": "Classic authority-fear-urgency manipulation flow"
    },
    {
        "name": "REFUND_LINK_VERIFY_PAYMENT",
        "sequence": [
            ["refund", "prize", "reward", "bonus"],
            ["link", "website", "click", "visit"],
            ["verify", "confirm", "authenticate"],
            ["payment", "credit card", "bank", "account"]
        ],
        "score": 38,
        "description": "Refund bait to credential/payment harvesting"
    },
    {
        "name": "ROMANCE_TRUST_INVESTMENT_CRYPTO",
        "sequence": [
            ["love", "lonely", "relationship", "soulmate"],
            ["trust", "help", "support", "together"],
            ["investment", "opportunity", "business", "profit"],
            ["bitcoin", "crypto", "wallet", "transfer"]
        ],
        "score": 40,
        "description": "Romance scam escalation to financial fraud"
    }
]