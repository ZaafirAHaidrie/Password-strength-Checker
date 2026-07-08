# Password Checker foundation
import string
password = input("Enter password: ")

def lengthcheck(password):
    if len(password) >= 8:
        return True
    else:
        return False

def ucasecheck(password):
    for character in password:
        if character.isupper():
            return True
    return False

def lcasecheck(password):
    for character in password:
        if character.islower():
            return True
    return False

def digitcheck(password):
    for character in password:
        if character.isdigit():
            return True
    return False
    
def special_char_check(password):
    for character in password:
        if character in string.punctuation:
            return True
    return False

weightage = {
    "length": 3,
    "uppercase" : 1,
    "lowercase" : 1,
    "digit" : 2,
    "special char" : 1
}
def scorecalc(password):
    score = 0
    checks = {
        "length" : lengthcheck(password),
        "uppercase" : ucasecheck(password),
        "lowercase" : lcasecheck(password),
        "digit" : digitcheck(password),  
        "special char" : special_char_check(password)
    }
    for key,passed in checks.items():
        if passed:
            score = score + weightage[key]
    return score,checks

def rating(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"

score, checks = scorecalc(password)
rate_label = rating(score)
print(f"Score: {score}/8 — Rating: {rate_label}")    