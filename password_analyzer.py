import re

def analyze_password(password):
    score = 0

    # Length Check
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1

    # Number Check
    if re.search(r"\d", password):
        score += 1

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength Evaluation
    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    print("\nSuggestions:")
    if len(password) < 12:
        print("- Increase password length")
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters")
    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters")
    if not re.search(r"\d", password):
        print("- Add numbers")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add special characters")

password = input("Enter Password: ")
analyze_password(password)