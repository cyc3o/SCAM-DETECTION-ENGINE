# Detection Test Cases

This folder contains sample inputs used to validate the
ENHANCED CHEAT DETECTOR V3 detection engine.

## Files

### phishing_samples.txt
Contains realistic scam and phishing messages including:
- Banking phishing
- UPI fraud
- Utility scams
- Authority impersonation
- Crypto investment scams
- URL shortening abuse

Expected Result:
- Medium to Critical risk verdicts
- IOC extraction
- Report + IOC export

### benign_samples.txt
Contains legitimate, non-malicious messages.

Expected Result:
- Low risk verdict
- Minimal or no detection signals
- No aggressive warnings