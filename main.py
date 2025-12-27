from strength_checker import check_strength
from dictionary_attack import dictionary_attack
from password_suggester import suggest_password
import re

def line():
    print("=" * 50)

line()
print("        PASSWORD SECURITY ANALYZER")
line()

password = input("\nPassword Entered : ")

# -------- STRENGTH CHECK --------
strength = check_strength(password)

# -------- DYNAMIC SECURITY SCORE --------
score = 0

# Length contribution (max 40)
score += min(len(password) * 3, 40)

if re.search(r"[a-z]", password):
    score += 10
if re.search(r"[A-Z]", password):
    score += 15
if re.search(r"[0-9]", password):
    score += 15
if re.search(r"[!@#$%^&*()_+=-]", password):
    score += 20

security_score = min(score, 100)

if strength == "WEAK":
    security_score = security_score // 2

# -------- RISK LEVEL --------
if security_score < 40:
    risk = "HIGH"
elif security_score < 70:
    risk = "MEDIUM"
else:
    risk = "LOW"

print("\nStrength Status  :", strength)
print("Security Score   :", security_score, "/ 100")
print("Risk Level       :", risk)

# -------- REASON --------
print("\nReason:")

MIN_LENGTH = 12

if len(password) < MIN_LENGTH:
    remaining = MIN_LENGTH - len(password)
    print(f" - Password is too short, add {remaining} more characters")

if not any(c.islower() for c in password):
    print(" - No lowercase characters")

if not any(c.isupper() for c in password):
    print(" - No uppercase characters")

if not any(c.isdigit() for c in password):
    print(" - No numbers")

if not any(c in "!@#$%^&*()_+=-" for c in password):
    print(" - No special symbols")

# -------- RECOMMENDATION --------
print("\n" + "-" * 50)
print("Security Recommendation")
print("-" * 50)

if strength != "STRONG":
    print("\nSuggested Strong Password:")
    print(" ➜", suggest_password())

print("\nTips:")
print(" - Use at least 12 characters")
print(" - Mix uppercase, lowercase, numbers & symbols")
print(" - Avoid common words")

line()
print("Analysis Completed Successfully")
line()
