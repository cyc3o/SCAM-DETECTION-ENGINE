import json
import csv
import os
from datetime import datetime

# ======================================================
# IOC EXPORT ENGINE
# ======================================================

IOC_DIR = "iocs"

def export_iocs(entities: dict):
    """
    Export extracted Indicators of Compromise (IOCs)
    to JSON and CSV formats.
    """

    os.makedirs(IOC_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    ioc_data = {
        "domains": list(set(entities.get("domains", []))),
        "ip_addresses": list(set(entities.get("ip_addresses", []))),
        "emails": list(set(entities.get("emails", []))),
        "phones": list(set(entities.get("phones", []))),
        "bitcoin_addresses": list(set(entities.get("bitcoin_addresses", []))),
        "ethereum_addresses": list(set(entities.get("ethereum_addresses", []))),
        "upi_ids": list(set(entities.get("upi_ids", []))),
        "payment_handles": list(set(entities.get("payment_handles", []))),
        "generated_at": timestamp
    }

    # -----------------------------
    # JSON EXPORT
    # -----------------------------
    json_path = os.path.join(IOC_DIR, f"iocs_{timestamp}.json")
    with open(json_path, "w") as jf:
        json.dump(ioc_data, jf, indent=2)

    # -----------------------------
    # CSV EXPORT
    # -----------------------------
    csv_path = os.path.join(IOC_DIR, f"iocs_{timestamp}.csv")
    with open(csv_path, "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(["IOC_TYPE", "VALUE"])

        for ioc_type, values in ioc_data.items():
            if isinstance(values, list):
                for val in values:
                    writer.writerow([ioc_type, val])

    return json_path, csv_path