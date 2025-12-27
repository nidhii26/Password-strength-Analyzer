📌 Project Overview
The Password Security Analyzer is a Python-based cybersecurity project designed to evaluate password strength and calculate a dynamic security score. 
The project focuses on improving authentication security by enforcing strong password policies and educating users about common password vulnerabilities.
This tool analyzes passwords using rule-based logic, simulates common attack scenarios, and provides actionable feedback along with secure password recommendations.

🎯 Key Features
✔ Enforces a minimum password length of 12 characters
✔ Classifies passwords as WEAK, MEDIUM, or STRONG
✔ STRONG passwords require:
Uppercase letters
Lowercase letters
Numbers
Special characters
✔ Calculates a dynamic security score (0–100) for every password
✔ Applies penalty scoring for weak passwords (score is reduced by half)
✔ Displays risk level (HIGH / MEDIUM / LOW)
✔ Explains why a password is weak
✔ Simulates dictionary attack (educational purpose)
✔ Suggests strong passwords automatically
✔ Modular and easy-to-understand code structure

🔢 Security Score Calculation
The security score is calculated dynamically using a weighted formula:
Password length contributes up to 40 points
Each character type contributes 15 points:
Lowercase letter
Uppercase letter
Digit
Special character
If the password is classified as WEAK, the final score is reduced by 50% to clearly reflect low security.

🛡️ Technologies Used
Python
Regular Expressions (re)
Modular Programming Approach
Console-based Interface

🧠 Security Concepts Implemented
Password Authentication
Access Control
Identity Protection
Dictionary Attack Simulation
Password Complexity Policies
Risk-Based Scoring

🚀 Use Case
This project is suitable for:
Academic learning (Cybersecurity / IAM)
Understanding password strength mechanisms
Demonstrating authentication security concepts
Beginner-friendly security tool implementation

🔮 Future Enhancements
GUI or Web-based version
Integration with login/registration systems
Real-time breached password checking
Advanced entropy-based scoring
Multi-Factor Authentication (MFA) support
