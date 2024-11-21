# Edmon Huang
# UWYO COSC 1010
# Submission Date: 11/19/24
# Lab 10
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here
# AI and Stack overflow
#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

def main():
    try:
        with open('hash', 'r') as hash_file: # Opens hash in read mode
            target_hash = hash_file.read().strip() # reads code and removes white space
    except FileNotFoundError: # Catches error
        print("Error: The file was not found")
        return 
    except Exception as e:
        print(f"An error ocurred while reading the file: {e}")
        return
    
    try:
        with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as password_file: # Open in read with UTF-8 encoding
            passwords = password_file.readlines()
    except FileNotFoundError:
        print("Error: The file was not found.")
        return
    except Exception as e:
        print(f"An error occured while reading text: {e}")
        return
    else:
        for password in passwords:
            password = password.strip()
            hash_password = get_hash(password)
            if hash_password == target_hash:
                print(f"Password: {password}")
                break
        else:
            print("Password not found")
if __name__ == "__main__":
    main()





# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
