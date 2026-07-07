# Password Checker foundation
import string

password = input("Enter password: ")
print('\n')

def lengthcheck(password):
    if len(password) < 8:
        print("Invalid password length (should be atleast 8 characters)")
    else:
        print("Password length [>8]: YES")

def ucasecheck(password):
    is_uppercase = False
    for character in password:
        if character.isupper():
            is_uppercase = True
    if not is_uppercase:
        print("There should be atleast 1 uppercase letter")
    else:
        print("At least one uppercase letter: YES")

def lcasecheck(password):
    is_lowercase = False
    for character in password:
        if character.islower():
            is_lowercase = True
    if not is_lowercase:
        print("There should be atleast 1 lowercase letter")
    else:
        print("At least one lowercase letter: YES")

def digitcheck(password):
    has_num = False
    for character in password:
        if character.isdigit():
            has_num = True
    if not has_num:
        print("There should be atleast one digit")
    else:
        print("At least one digit: YES")
    
def special_char_check(password):
    has_sp_char = False
    for character in password:
        if character in string.punctuation:
            has_sp_char = True
    if not has_sp_char:
        print("There should be atleast one special character")
    else: 
        print("Atleast one special character: YES")

lengthcheck(password)
ucasecheck(password)
lcasecheck(password)
digitcheck(password)
special_char_check(password)