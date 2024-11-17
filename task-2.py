# A password generator is a useful tool that generates strong and
# random passwords for users. This project aims to create a
# password generator application using Python, allowing users to
# specify the length and complexity of the password.

import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets for password generation
    characters = string.ascii_letters + string.digits + string.punctuation  # a-zA-Z0-9!@#$%^&*
    
    # Randomly choose characters to create the password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main program
print("Welcome to the Password Generator!")

# User input for password length
try:
    password_length = int(input("Enter the desired length of your password: "))
    
    if password_length < 1:
        print("Password length should be at least 1 character.")
    else:
        # Generate the password
        generated_password = generate_password(password_length)

        # Display the generated password
        print(f"Your generated password is: {generated_password}")
        
except ValueError:
    print("Invalid input! Please enter a valid number for password length.")

