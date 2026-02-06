from typing import Tuple, List, Set
from intelligence.context_chains import CONTEXT_CHAINS
from utils.colors import Colors

# ======================================================
# CONTEXT CHAIN DETECTION ENGINE
# ======================================================

def detect_context_chains(message: str) -> Tuple[List[str], int, List[str], Set[str]]:
    """
    Detect multi-step scam intent context chains
    """
    msg = message.lower()
    attack_types = []
    score = 0
    reasons = []
    regions = set()
    
    for chain_name, chain_data in CONTEXT_CHAINS.items():
        matches = sum(
            1 for keyword in chain_data["keywords"]
            if keyword in msg
        )
        
        if matches >= chain_data["min_matches"]:
            attack_types.append(chain_name.replace("_", " "))
            score += chain_data["score"]
            regions.add(chain_data["region"])
            reasons.append(
                f"{Colors.ORANGE}CONTEXT CHAIN DETECTED: "
                f"{chain_name.replace('_', ' ')} "
                f"({matches}/{len(chain_data['keywords'])} keywords matched)."
                f"{Colors.END}"
            )
    
    return attack_types, score, reasons, regions