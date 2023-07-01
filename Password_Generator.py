import random
from colorama import Fore, Style

lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

def password_length():
    print("What length password would you like to generate?")
    while True:
        try:
            length = int(input())
            break
        except ValueError:
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + "Password length must be a number!")
            print("What length password would you like to generate?")
    while length < 4:
        print(Fore.RED + "ERROR: " + Style.RESET_ALL + "Password must be at least 4 characters long! Try Again!")
        print("What length password would you like to generate?")
        length = int(input())
    while length > 25:
        print(Fore.RED + "ERROR: " + Style.RESET_ALL + "Password must be no longer than 25 characters long! Try Again!")
        print("What length password would you like to generate?")
        length = int(input())
    print("Password Length: " + str(length))
    return length

def password_lower():
    print("Would you like your password to include lowercase letters? Yes or No?")
    lower = input().lower()
    if lower != 'yes' and lower != 'no':
        while lower != 'yes' and lower != 'no':
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + "User response must be \"Yes\" or \"No\"! Try again!")
            lower = input()
    if lower == 'yes':
        print("Your password will include lowercase letters.")
    if lower == 'no':
        print("Your password will not include lowercase letters.")
    return lower

def password_caps():
    print("Would you like your password to include capital letters? Yes or No?")
    caps = input().lower()
    if caps != 'yes' and caps != 'no':
        while caps != 'yes' and caps != 'no':
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + "User response must be \"Yes\" or \"No\"! Try again!")
            caps = input()
    if caps == 'yes':
        print("Your password will include capital letters.")
    if caps == 'no':
        print("Your password will not include capital letters.")
    return caps

def password_nums():
    print("Would you like your password to include numbers? Yes or No?")
    nums = input().lower()
    if nums != 'yes' and nums != 'no':
        while nums != 'yes' and nums != 'no':
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + "User response must be \"Yes\" or \"No\"! Try again!")
            nums = input()
    if nums == 'yes':
        print("Your password will include numbers.")
    if nums == 'no':
        print("Your password will not include numbers.")
    return nums

def password_symbols():
    print("Would you like your password to include symbols? Yes or No?")
    symbols = input().lower()
    if symbols != 'yes' and symbols != 'no':
        while symbols != 'yes' and symbols != 'no':
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + "User response must be \"Yes\" or \"No\"! Try again!")
            symbols = input()
    if symbols == 'yes':
        print("Your password will include symbols.")
    if symbols == 'no':
        print("Your password will not include symbols.")
    return symbols

def generate_password():
    print("Hi There! Thanks for using my password generator!")
    while True:
        pass_length = password_length()
        pass_lower = password_lower()
        pass_caps = password_caps()
        pass_nums = password_nums()
        pass_symbols = password_symbols()
        if pass_lower == 'no' and pass_caps == 'no' and pass_nums == 'no':
            print("You must respond " + Fore.GREEN + "yes" + Style.RESET_ALL + " to at least one of the options!")
            print(Fore.RED + "...Program Restarting")
            print(Style.RESET_ALL)
            continue
        else:
            break
    possible_chars = ''
    password = ''
    if pass_caps == 'yes':
        possible_chars += uppercase_characters
    if pass_lower == 'yes':
        possible_chars += lowercase_characters
    if pass_nums == 'yes':
        possible_chars += numbers
    if pass_symbols == 'yes':
        possible_chars += symbols
    for i in range(pass_length):
        password += possible_chars[random.randint(0, len(possible_chars) - 1)]
    print("-------------------------")
    print(Fore.GREEN + "Your password is {}".format(password))
    print(Style.RESET_ALL + "-------------------------")
    return password


generate_password()