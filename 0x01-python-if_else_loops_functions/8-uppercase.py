#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting the difference between lowercase and uppercase ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print()
