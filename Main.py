password = input("Enter password: ")

# Checks if the password has 8 characters
if len(password) < 8:
    print("Password must be at least 8 characters long")
    exit()
else:
    print("Good length")

# Checks if the password has an uppercase letter
valid = False
for letter in password:
    if letter.isupper():
      valid = True

if valid:
    print("Password is valid")
else:
    print("Password is not valid")

#Checks if the password has a lowercase letter
valid1 = False
for letter in password:
    if letter.islower():
      valid1 = True

if valid1:
    print("Password is valid")
else:
    print("Password is not valid")

#Checks if the password has a number
valid2 = False
for letter in password:
    if letter.isdigit():
      valid2 = True

if valid2:
    print("Password is valid")
else:
    print("Password is not valid")

