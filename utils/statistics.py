from utils.colors import Colors

# ======================================================
# STATISTICS TRACKER
# ======================================================

class StatisticsTracker:
    def __init__(self):
        self.total_analyzed = 0
        self.threat_distribution = {
            "CRITICAL": 0,
            "HIGH": 0,
            "ELEVATED": 0,
            "MEDIUM": 0,
            "LOW-MEDIUM": 0,
            "LOW": 0
        }
        self.total_score = 0
    
    def update(self, report: dict):
        self.total_analyzed += 1
        self.threat_distribution[report["threat_level"]] += 1
        self.total_score += report["risk_score"]
    
    def display(self):
        print(f"\n{Colors.CYBER_BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.SYSTEM_CYAN}📊 SESSION STATISTICS{Colors.END}")
        print(f"{Colors.CYBER_BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.DATA}Total Messages Analyzed:{Colors.END} {self.total_analyzed}")
        
        if self.total_analyzed > 0:
            print(f"{Colors.DATA}Average Risk Score:{Colors.END} {self.total_score / self.total_analyzed:.2f}")
            print(f"\n{Colors.TERMINAL_GREEN}Threat Level Distribution:{Colors.END}")
            for level, count in self.threat_distribution.items():
                if count > 0:
                    percentage = (count / self.total_analyzed) * 100
                    print(f"  {Colors.GRAY}•{Colors.END} {level}: {count} ({percentage:.1f}%)")