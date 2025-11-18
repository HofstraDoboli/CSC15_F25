# check ord function - returns the ACII value of a character
char = 'Z'
print(f"The ASCII value of '{char}' is {ord(char)}")
print(f"The character for ASCII value 66 is '{chr(66)}'")

# simple shift cipher example
ascii_char = ord(char)
shift = 10
new_ascii = ord('A') + (ascii_char - ord('A') + shift) % 26 # stays in between the ascii codes for uppercase letters 'A' to 'Z'

# constrain: if new_ascii > ascii code of 'Z', start from 'A' again

new_char = chr(new_ascii)
print(f"After shifting by {shift}, the new character is '{new_char}' with ASCII value {new_ascii}")
# check chr function - returns the character for an ASCII value
