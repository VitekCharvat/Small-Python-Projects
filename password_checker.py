import string

def password_strenght(password):
    print("enter password")
    password = input()
    has_letters = any(c. isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    if len(password) < 6 or not has_letters and not has_numbers:
        return "Weak"
    elif not has_symbols or len(password) < 10:
        return "Medium"
    else:
        return "Strong"

print("your password is",password_strenght("password"))


