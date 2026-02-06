import json
import os
from datetime import datetime

# ======================================================
# REPORT SAVE ENGINE
# ======================================================

REPORT_DIR = "reports"

def save_report(report: dict) -> str:
    """
    Save full intelligence report to a JSON file.
    Returns the saved file path.
    """

    os.makedirs(REPORT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"report_{timestamp}.json"
    path = os.path.join(REPORT_DIR, filename)

    with open(path, "w") as f:
        json.dump(report, f, indent=2)

    return path