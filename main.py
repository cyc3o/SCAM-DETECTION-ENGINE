import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.analyzer import analyze_message
from utils.statistics import StatisticsTracker
from utils.colors import Colors, AUTHOR
from utils.ioc_exporter import export_iocs
from utils.report_writer import save_report

# ======================================================
# SOC / ANALYZER BANNER (DIRECT IN MAIN)
# ======================================================

print(f"""{Colors.RED}
╱╲⠀⠀╱╲
▏⠀╲⠀▏⠀╲
╲⠀▕⠀╲⠀▕
⠀╲▕⠀⠀╲▕
⠀╱⠀▔▔▔⠀╲
▕╭⠀╮⠀╭⠀╮▏
╱┊▉┊⠀┊▉┊╲
▏⠀┳▕▇▏┳⠀▕
╲⠀╰┳┻┳╯⠀╱
⠀▔▏┗┻┛▕▔⠀╱╲
⠀╱▕╲▂╱▏╲╱⠀╱
╱⠀▕╱▔╲▏⠀⠀╱
⠀╱▏⠀⠀⠀▕╲╱ 
{Colors.END}""")

print(
    f"{Colors.CRITICAL}"
    f"[ CHEAT DETECTOR —  MODE ACTIVATED ]"
    f"{Colors.END}"
)

print(
    f"{Colors.GRAY}"
    f"AUTHOR  :  {AUTHOR}"
    f"{Colors.END}"
)

print(
    f"{Colors.GRAY}"
    f"GITHUB  :  @cyc3o"
    f"{Colors.END}"
)

print(
    f"{Colors.SYSTEM_CYAN}"
    f"{'=' * 60}"
    f"{Colors.END}\n"
)

print(f"{Colors.GRAY}📌 PASTE MESSAGE & PRESS ENTER TWICE ON EMPTY LINES TO ANALYZE ! {Colors.END}")
print(f"{Colors.RED}🌐 « MINIMUM 10 CHARACTERS REQUIRED TO ANALYZE »{Colors.END}")
print(f"{Colors.GRAY}📡 « ENGINE IS WORKING 3 MAX CLICK  »{Colors.END}\n")

# ======================================================
# CLI LOOP
# ======================================================

stats = StatisticsTracker()
last_message = None
analyzed_messages = set()  # Track message hashes to prevent duplicates

while True:
    lines = []
    line_count = 0

    print(f"{Colors.TERMINAL_GREEN}⌁ ANALYSE >{Colors.END}", flush=True)

    # --------------------------------------------------
    # MULTI-LINE INPUT (FIXED FOR PASTED EMAILS)
    # --------------------------------------------------
    empty_line_count = 0
    while True:
        try:
            if line_count > 0:
                print(f"{Colors.GRAY}... {Colors.END}", end="", flush=True)
            line = input()
            line_count += 1
        except (EOFError, KeyboardInterrupt):
            print(f"\n{Colors.CRITICAL}🛑 SYSTEM SHUTDOWN. STAY SAFE!{Colors.END}\n")
            exit(0)

        # CRITICAL FIX: Require TWO consecutive empty lines to end input
        # This allows pasted emails with blank lines to be collected as ONE message
        if line.strip() == "":
            empty_line_count += 1
            if empty_line_count >= 2:
                break
            lines.append(line)  # Keep the blank line in the message
        else:
            empty_line_count = 0  # Reset counter
            lines.append(line)

    user_msg = "\n".join(lines).strip()

    # --------------------------------------------------
    # VALIDATION
    # --------------------------------------------------
    if not user_msg:
        continue

    if len(user_msg) < 10:
        print(f"{Colors.YELLOW}⚠️ TOO SHORT [ MIN 10 CHARACTER ] TRY AGAIN ! {Colors.END}\n")
        continue

    # --------------------------------------------------
    # COMMANDS
    # --------------------------------------------------
    if user_msg.lower() == "exit":
        stats.display()
        print(f"\n{Colors.CRITICAL}🛑 SYSTEM SHUTDOWN. STAY SAFE!{Colors.END}\n")
        break

    if user_msg.lower() == "stats":
        stats.display()
        print()
        continue

    # --------------------------------------------------
    # DUPLICATE CHECK (COMPREHENSIVE)
    # --------------------------------------------------
    import hashlib
    
    # Generate message hash for deduplication
    msg_hash = hashlib.sha256(user_msg.encode('utf-8')).hexdigest()
    
    # Check hash-based duplicates (catches identical content even if formatted differently)
    if msg_hash in analyzed_messages:
        print(f"{Colors.YELLOW}⚠️ MESSAGE ALREADY ANALYZED — SKIPPED.{Colors.END}\n")
        continue
    
    # Check exact string duplicates (fast path)
    if user_msg == last_message:
        print(f"{Colors.YELLOW}⚠️ DUPLICATE DETECTED — SKIPPED.{Colors.END}\n")
        continue

    # Mark this message as analyzed
    last_message = user_msg
    analyzed_messages.add(msg_hash)

    # --------------------------------------------------
    # ANALYSIS
    # --------------------------------------------------
    try:
        report = analyze_message(user_msg)
        stats.update(report)

        # SAVE REPORT
        report_path = save_report(report)

        # EXPORT IOCs
        json_ioc, csv_ioc = export_iocs(report["entities"])

        # --------------------------------------------------
        # OUTPUT
        # --------------------------------------------------
        print(f"\n{Colors.CYBER_BLUE}{'=' * 60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.SYSTEM_CYAN}🔬 INTELLIGENCE REPORT{Colors.END}")
        print(f"{Colors.CYBER_BLUE}{'=' * 60}{Colors.END}")

        print(f"{Colors.DATA}📅 TIMESTAMP   :{Colors.END} {report['date']}")
        print(f"{Colors.DATA}🧠 VERDICT     :{Colors.END} {report['verdict']}")
        print(f"{Colors.DATA}📈 RISK SCORE  :{Colors.END} {Colors.BOLD}{report['risk_score']}{Colors.END}")
        print(f"{Colors.DATA}🎯 CONFIDENCE  :{Colors.END} {report['confidence'] * 100:.0f}%")

        if report["categories"]:
            print(f"\n{Colors.TERMINAL_GREEN}🔎 DETECTED CATEGORIES:{Colors.END}")
            for c in report["categories"]:
                print(f" {Colors.GRAY}•{Colors.END} {c}")

        if report["reasons"]:
            print(f"\n{Colors.WARNING}❗ WHY THIS MESSAGE IS RISKY:{Colors.END}")
            for r in report["reasons"]:
                print(f" {Colors.GRAY}•{Colors.END} {r}")

        # IOC STATUS
        print(f"\n{Colors.CYAN}📤 IOCs EXPORTED:{Colors.END}")
        print(f" {Colors.GRAY}• JSON:{Colors.END} {json_ioc}")
        print(f" {Colors.GRAY}• CSV :{Colors.END} {csv_ioc}")

        # REPORT STATUS
        print(f"\n{Colors.CYAN}📄 REPORT SAVED:{Colors.END}")
        print(f" {Colors.GRAY}• FILE:{Colors.END} {report_path}")

        print(f"\n{Colors.GRAY}{'─' * 60}{Colors.END}")
        print(f"{Colors.TERMINAL_GREEN}👤 AUTHOR:{Colors.END} {AUTHOR}")
        print(f"{Colors.GRAY}{'─' * 60}{Colors.END}\n")

    except Exception as e:
        print(f"{Colors.RED}❌ ERROR: {str(e)}{Colors.END}\n")
        continue