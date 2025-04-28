import random
import string

# Function to generate password
def generate_password(length):
    # Define the characters to use: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose 'length' number of characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        print("Password length must be greater than 0.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
