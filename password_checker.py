import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error or lowercase_error or uppercase_error or digit_error or special_char_error:
        if length_error or (lowercase_error + uppercase_error + digit_error + special_char_error) >= 3:
            return "Weak"
        else:
            return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength = check_password_strength(pwd)
    print("Password strength:", strength)
