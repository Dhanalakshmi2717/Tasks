def password_strength(password):
    score = 0
    special_chars = "!@#$%^&*"

    if len(password) >= 8:
        score += 1

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


if __name__ == "__main__":
    print(password_strength("Dhana@123"))
    print(password_strength("pass123"))
    print(password_strength("password"))
