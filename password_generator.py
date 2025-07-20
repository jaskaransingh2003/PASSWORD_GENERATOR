import random
import string
import re

def generate_password(length=15):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return ""

# Character sets
    letters= string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

# Ensure at least one character from each category
    password = [
    random.choice(letters),
    random.choice(digits),
    random.choice(symbols)
]

# Fill the rest of the password with random characters
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k = length- 3)
  
# Shuffle the password to avoid patterns
    random.shuffle(password)
    return ''.join(password)

def Check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d",password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?/:{}|<>]", password) is None

    score = 5 - sum([length_error, uppercase_error,lowercase_error,digit_error,symbol_error])
    if score == 5:
        return "Very Strong Password"
    elif score == 4:
        return "Strong Password"
    elif score == 3:
        return "Moderate Password"
    elif score == 2:
        return "Weak Passwprd"
    else:
        return "Very Weak Password"
    
# -----Main Program------
while True:
    print("\n1. Generate a password")
    print("2. Check Your Password Strength")
    print("3. Exit")
    choice = input("Enter Your Choice (1/2/3):")

    if choice == '1':
        length = int(input("Enter the Desired Length of Password):"))
        new_password = generate_password(length)
        print("Generated Password:", new_password)
        print("Password Strength:", Check_password_strength(new_password))

    elif choice == '2':
        user_password = input("Enter Your Password to Check:")
        print("Your Password Strength is:", Check_password_strength(user_password))

    elif choice == '3':
        print("Exiting the program.\nGoodbye.....")
        break
    else:
        print("Invalid choice. Please try again.")

