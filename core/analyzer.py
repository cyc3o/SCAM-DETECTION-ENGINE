import re
from datetime import datetime
from typing import Dict, List, Set

from core.entities import (
    extract_entities,
    HIGH_RISK_DOMAIN_PATTERN,
    SHORTENED_URL_PATTERN,
    LONG_NUMBER_PATTERN
)
from core.language import detect_language_style
from core.context import detect_context_chains
from core.behavioral import detect_behavioral_flows
from core.patterns import detect_suspicious_patterns

from intelligence.signals import SIGNALS
from utils.reputation import ReputationCache
from utils.colors import Colors

# ======================================================
# ADVANCED ANALYSIS ENGINE (CORE BRAIN)
# ======================================================

reputation_cache = ReputationCache()

def analyze_message(message: str) -> Dict:
    """
    Main analysis function with multi-layered intelligence
    """
    msg = message.lower()
    score = 0
    reasons: List[str] = []
    categories: Set[str] = set()
    attack_types: List[str] = []
    regions: Set[str] = set()
    languages: Set[str] = set()

    # --------------------------------------------------
    # 1. SIGNAL-BASED DETECTION
    # --------------------------------------------------
    for signal in SIGNALS:
        matches = re.findall(signal["pattern"], msg)
        if matches:
            match_count = len(matches)
            signal_score = signal["score"] * min(match_count, 3)
            score += signal_score
            categories.add(signal["category"])

            if match_count > 1:
                reasons.append(
                    f"{signal['reason']} (DETECTED {match_count}x)"
                )
            else:
                reasons.append(signal["reason"])

    # --------------------------------------------------
    # 2. ENTITY EXTRACTION
    # --------------------------------------------------
    entities = extract_entities(message)

    # --------------------------------------------------
    # 3. REPUTATION MEMORY CHECK
    # --------------------------------------------------
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            if entity:
                rep_bonus = reputation_cache.check_and_update(entity_type, entity)
                if rep_bonus > 0:
                    score += rep_bonus
                    reasons.append(
                        f"{Colors.GRAY}REPEATED {entity_type.upper().replace('_', ' ')}: "
                        f"{entity[:30]}... (SEEN BEFORE +{rep_bonus}){Colors.END}"
                    )

    # --------------------------------------------------
    # 4. LANGUAGE & PHRASE INTELLIGENCE
    # --------------------------------------------------
    detected_languages, lang_score, lang_reasons = detect_language_style(message)
    languages.update(detected_languages)
    score += lang_score
    reasons.extend(lang_reasons)

    # --------------------------------------------------
    # 5. CONTEXT CHAIN DETECTION
    # --------------------------------------------------
    chain_attacks, chain_score, chain_reasons, chain_regions = detect_context_chains(message)
    score += chain_score
    reasons.extend(chain_reasons)
    attack_types.extend(chain_attacks)
    regions.update(chain_regions)

    # --------------------------------------------------
    # 6. BEHAVIORAL FLOW DETECTION
    # --------------------------------------------------
    flow_score, flow_reasons = detect_behavioral_flows(message)
    score += flow_score
    reasons.extend(flow_reasons)

    # --------------------------------------------------
    # 7. URL & DOMAIN ANALYSIS
    # --------------------------------------------------
    if entities["domains"]:
        score += 20
        categories.add(f"{Colors.SYSTEM_CYAN}WEBSITE PRESENT 🌐{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}MESSAGE CONTAINS {len(entities['domains'])} URL(S).{Colors.END}"
        )

        if any(re.search(HIGH_RISK_DOMAIN_PATTERN, url) for url in entities["domains"]):
            score += 30
            categories.add(f"{Colors.CRITICAL}HIGH-RISK DOMAIN{Colors.END}")
            reasons.append(
                f"{Colors.GRAY}DOMAIN EXTENSION COMMONLY USED IN SCAMS.{Colors.END}"
            )

        if any(re.search(SHORTENED_URL_PATTERN, url) for url in entities["domains"]):
            score += 22
            categories.add(f"{Colors.WARNING}SHORTENED URL{Colors.END}")
            reasons.append(
                f"{Colors.GRAY}SHORTENED URL HIDES FINAL DESTINATION.{Colors.END}"
            )

    # --------------------------------------------------
    # 8. IP ADDRESS DETECTION
    # --------------------------------------------------
    if entities["ip_addresses"]:
        score += 28
        categories.add(f"{Colors.RED}RAW IP ADDRESS{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}RAW IP USED TO BYPASS DOMAIN FILTERS.{Colors.END}"
        )

    # --------------------------------------------------
    # 9. PHONE / VISHING DETECTION
    # --------------------------------------------------
    if entities["phones"]:
        score += 25
        categories.add(f"{Colors.DARK_RED}VISHING INDICATOR 📞{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}PHONE NUMBER PRESENT – CALL-BASED SCAM RISK.{Colors.END}"
        )

    # --------------------------------------------------
    # 10. EMAIL DETECTION
    # --------------------------------------------------
    if entities["emails"]:
        score += 15
        categories.add(f"{Colors.CYAN}EMAIL ADDRESS PRESENT 📧{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}EMAIL ADDRESS USED AS SCAM CONTACT.{Colors.END}"
        )

    # --------------------------------------------------
    # 11. CRYPTOCURRENCY DETECTION
    # --------------------------------------------------
    if entities["bitcoin_addresses"] or entities["ethereum_addresses"]:
        score += 32
        categories.add(f"{Colors.CRITICAL}CRYPTO WALLET DETECTED ₿{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CRYPTO WALLET INDICATES PAYMENT SCAM.{Colors.END}"
        )

    # --------------------------------------------------
    # 12. UPI / PAYMENT HANDLE DETECTION
    # --------------------------------------------------
    if entities["upi_ids"]:
        score += 28
        categories.add(f"{Colors.CRITICAL}UPI ID DETECTED 💳{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}UPI PAYMENT REQUEST – INDIAN FRAUD INDICATOR.{Colors.END}"
        )
        regions.add("INDIA")

    if entities["payment_handles"]:
        score += 26
        categories.add(f"{Colors.CRITICAL}PAYMENT HANDLE DETECTED 💸{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}P2P PAYMENT HANDLE USED IN SCAMS.{Colors.END}"
        )
        regions.add("USA")

    # --------------------------------------------------
    # 13. LONG NUMBER / ID DETECTION
    # --------------------------------------------------
    if re.search(LONG_NUMBER_PATTERN, msg):
        score += 9
        categories.add(f"{Colors.YELLOW}SUSPICIOUS NUMERIC IDENTIFIER 🔢{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}LONG NUMERIC IDENTIFIER FOUND.{Colors.END}"
        )

    # --------------------------------------------------
    # 14. ADVANCED SUSPICIOUS PATTERNS
    # --------------------------------------------------
    suspicious_score, suspicious_reasons = detect_suspicious_patterns(message)
    score += suspicious_score
    reasons.extend(suspicious_reasons)

    # --------------------------------------------------
    # 15. FALLBACKS & NORMALIZATION
    # --------------------------------------------------
    if not regions:
        regions.add("GLOBAL")

    if not languages:
        languages.add("ENGLISH")

    if not attack_types:
        attack_types = ["UNCLASSIFIED SOCIAL ENGINEERING"]

    confidence = round(min(score / 120, 1.0), 2)

    # --------------------------------------------------
    # 16. VERDICT LOGIC
    # --------------------------------------------------
    if score >= 150:
        verdict = f"{Colors.CRITICAL}{Colors.BLINK}🚨 CRITICAL THREAT{Colors.END}"
        threat_level = "CRITICAL"
    elif score >= 100:
        verdict = f"{Colors.CRITICAL}{Colors.BLINK}🚨 HIGH RISK SCAM{Colors.END}"
        threat_level = "HIGH"
    elif score >= 70:
        verdict = f"{Colors.RED}⚠️ ELEVATED RISK{Colors.END}"
        threat_level = "ELEVATED"
    elif score >= 50:
        verdict = f"{Colors.YELLOW}⚠️ MEDIUM RISK{Colors.END}"
        threat_level = "MEDIUM"
    elif score >= 25:
        verdict = f"{Colors.WARNING}⚡ LOW-MEDIUM RISK{Colors.END}"
        threat_level = "LOW-MEDIUM"
    else:
        verdict = f"{Colors.HACKER_GREEN}✅ LOW RISK{Colors.END}"
        threat_level = "LOW"

    # --------------------------------------------------
    # 17. FINAL REPORT
    # --------------------------------------------------
    return {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "verdict": verdict,
        "threat_level": threat_level,
        "risk_score": score,
        "confidence": confidence,
        "attack_types": attack_types,
        "region_detected": sorted(regions),
        "language_style": sorted(languages),
        "categories": sorted(categories),
        "reasons": reasons,
        "entities": entities,
        "message_length": len(message)
    }