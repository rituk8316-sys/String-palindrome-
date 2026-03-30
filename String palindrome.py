# Program to check whether a string is a palindrome
# Author: Your Name
# Description: This program checks if the entered string is same forward and backward

def is_palindrome(text):
    # Convert to lowercase for uniform comparison
    text = text.lower()
    
    # Reverse the string
    reversed_text = text[::-1]
    
    # Check palindrome
    if text == reversed_text:
        return True
    else:
        return False


# Taking input from user
input_string = input("Enter a string: ")

# Function call
if is_palindrome(input_string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
