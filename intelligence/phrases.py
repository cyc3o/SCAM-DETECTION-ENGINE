# ======================================================
# 🗣️ LANGUAGE & PHRASE INTELLIGENCE
# ======================================================

INDIAN_SCAM_PHRASES = {
    "hindi_hinglish": [
        r"\b(aapka\s+account|tumhara\s+account)\b",
        r"\b(turant|abhi|immediately)\s+(action|verify|karo|update)\b",
        r"\b(link\s+(open|click)\s+kar[eo]?)\b",
        r"\b(otp\s+(share|bhej[eo]?|send))\b",
        r"\b(account\s+(block|band)\s+(ho\s+jayega|hoga))\b",
        r"\b(last\s+warning|antim\s+chetavani)\b",
        r"\b(kyc\s+(complete|update|pending|verify)\s+kar[eo]?)\b",
        r"\b(aadhaar\s+(link|update|verify))\b",
        r"\b(pan\s+card\s+(update|link))\b",
        r"\b(digital\s+arrest)\b",
        r"\b(police\s+(action|case|complaint))\b",
        r"\b(electricity\s+bill\s+(pending|overdue))\b",
        r"\b(power\s+cut|bijli\s+kat)\b",
    ],
    "formal_english_indian": [
        r"\b(dear\s+(customer|sir|madam|user))\b",
        r"\b(immediate\s+action\s+required)\b",
        r"\b(kindly\s+(verify|update|confirm))\b",
        r"\b(failure\s+to\s+comply)\b",
        r"\b(legal\s+action\s+will\s+be\s+taken)\b",
    ]
}

US_SCAM_PHRASES = {
    "authority_style": [
        r"\b(final\s+notice)\b",
        r"\b(immediate\s+action\s+required)\b",
        r"\b(failure\s+to\s+respond)\b",
        r"\b(this\s+call\s+is\s+being\s+recorded)\b",
        r"\b(you\s+have\s+been\s+selected)\b",
        r"\b(verify\s+your\s+identity)\b",
        r"\b(suspended|frozen|locked)\s+(account|card|ssn)\b",
    ],
    "payment_pressure": [
        r"\b(zelle|cashapp|venmo|paypal)\s+(payment|transaction|required)\b",
        r"\b(gift\s+card|itunes|google\s+play)\b",
        r"\b(wire\s+transfer)\b",
        r"\b(bitcoin|cryptocurrency)\s+payment\b",
    ]
}