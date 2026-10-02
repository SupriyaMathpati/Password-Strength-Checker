
import string
from getpass import getpass

def check_password(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Character checks
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Repeated character check
    repeated = any(
        password[i] == password[i + 1]
        for i in range(len(password) - 1)
    )

    if repeated:
        score -= 1
        suggestions.append("Avoid repeated characters.")

    # Common pattern check
    common_patterns = ["password", "1234", "qwerty", "admin"]
    if any(p in password.lower() for p in common_patterns):
        score -= 2
        suggestions.append("Avoid common password patterns.")

    # Strength classification
    if score >= 6 and len(password) >= 12 and not repeated:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


print("=== Password Strength Checker ===")

password = getpass("Enter a password: ")

if not password:
    print("Error: Password cannot be empty.")
else:
    strength, suggestions = check_password(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSecurity Recommendations:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Good! No basic issues detected.")

print("\nYour password is not saved.")