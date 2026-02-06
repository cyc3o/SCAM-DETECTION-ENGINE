import os
import json
from typing import Dict

# ======================================================
# 💾 OFFLINE REPUTATION MEMORY
# ======================================================

REPUTATION_FILE = "reputation_cache.json"

class ReputationCache:
    def __init__(self):
        self.cache = self._load()
    
    def _load(self) -> Dict:
        if os.path.exists(REPUTATION_FILE):
            try:
                with open(REPUTATION_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "domains": {},
            "phones": {},
            "emails": {},
            "upi_ids": {},
            "payment_handles": {}
        }
    
    def _save(self):
        try:
            with open(REPUTATION_FILE, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except Exception:
            pass
    
    def check_and_update(self, entity_type: str, value: str) -> int:
        """
        Check reputation and update count.
        Returns bonus score based on history.
        """
        if entity_type not in self.cache:
            self.cache[entity_type] = {}
        
        count = self.cache[entity_type].get(value, 0)
        self.cache[entity_type][value] = count + 1
        self._save()
        
        # Progressive scoring
        # 1st = 0
        # 2nd = 15
        # 3rd = 25
        # 4th+ = 35
        if count == 0:
            return 0
        elif count == 1:
            return 15
        elif count == 2:
            return 25
        else:
            return 35