import re

print("Password Strength Checker")
print("-------------------------")

password = input("Enter your password: ")

# Check each condition
length = len(password) >= 8
capital = re.search("[A-Z]", password)
number = re.search("[0-9]", password)
special = re.search("[!@#$%^&*]", password)

# Display result
if length and capital and number and special:
    print("Strong Password")
else:
    print("Weak Password")
    print("\nYour password should have:")

    if not length:
        print("- Minimum 8 characters")

    if not capital:
        print("- At least one capital letter")

    if not number:
        print("- At least one number")

    if not special:
        print("- At least one special character")