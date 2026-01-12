from typing import Tuple, List
from intelligence.behavioral_flows import BEHAVIORAL_FLOWS
from utils.colors import Colors

# ======================================================
# BEHAVIORAL FLOW DETECTION ENGINE
# ======================================================

def detect_behavioral_flows(message: str) -> Tuple[int, List[str]]:
    """
    Detect behavioral manipulation flow patterns
    """
    msg = message.lower()
    score = 0
    reasons = []
    
    for flow in BEHAVIORAL_FLOWS:
        matched_stages = 0
        stage_positions = []
        
        for stage_idx, stage_keywords in enumerate(flow["sequence"]):
            for keyword in stage_keywords:
                pos = msg.find(keyword)
                if pos != -1:
                    matched_stages += 1
                    stage_positions.append((stage_idx, pos))
                    break
        
        # Check if stages appear in order
        if matched_stages >= 3:
            stage_positions.sort(key=lambda x: x[1])
            stage_order = [s[0] for s in stage_positions]
            
            # Check if stages are generally increasing
            is_ordered = all(
                stage_order[i] <= stage_order[i + 1] + 1
                for i in range(len(stage_order) - 1)
            )
            
            if is_ordered:
                score += flow["score"]
                reasons.append(
                    f"{Colors.ORANGE}BEHAVIORAL FLOW: "
                    f"{flow['name'].replace('_', ' ')} "
                    f"- {flow['description']}"
                    f"{Colors.END}"
                )
    
    return score, reasons