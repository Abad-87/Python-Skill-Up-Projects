import random
import string

def password_gen(min_length, numbers = True, Character = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if Character:
        characters += special

    pwd = ""
    satisfy_cond = False
    number_present = False
    has_special_chars = False

    while not satisfy_cond or len(pwd) < min_length:
        new = random.choice(characters)
        pwd += new

        if new in digits:
            number_present = True
        elif new in special:
            has_special_chars = True

        satisfy_cond = True
        if numbers:
            satisfy_cond = number_present
        if Character:
            satisfy_cond = satisfy_cond and has_special_chars
    return pwd

min_length = int(input("Enter the numbers: "))
number_present = input("Do u want numbers (y/n)? ").lower() == 'y'
has_special_chars = input("Do u want special characters (y/n)? ").lower() == 'y'

pwd = password_gen(min_length, number_present, has_special_chars)
print("Genrate password is: ", pwd)
    
        