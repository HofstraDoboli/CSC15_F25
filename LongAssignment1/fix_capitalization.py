'''
Implement the fix_capitalization() function. fix_capitalization() has a 
string parameter and returns an updated string, where lowercase letters 
at the beginning of sentences are replaced with uppercase letters. 
fix_capitalization() also returns the number of letters that have been
capitalized. 
'''
def fix_capitalization(text):
    '''
    Fixes the capitalization of the input text.
    How to detect the beginning of a sentence:
    - The first character of the text is the beginning of a sentence.
    - Any character that follows a period (.), exclamation mark (!), or
      question mark (?) and a space is the beginning of a sentence.

    Pseudocode:
    1. Initialize an empty string to store the updated text.
    2. Initialize a counter to keep track of the number of capitalized letters.
    3. Loop through each character in the input text using its index.
        a. If the character is the first character of the text and is a lowercase letter:
            i. Capitalize the character.
            ii. Increment the counter.
        b. Else if the character follows a sentence-ending punctuation (., !, ?) and a
              space, and is a lowercase letter:
                i. Capitalize the character.
                ii. Increment the counter.
        add the character (capitalized or not) to the updated text.
    4. Return the updated text and the counter.
    '''
    num_capitalized = 0
    new_text = ""
    end_sentence = False
    for i in range(len(text)):
        new_char = text[i]
        # a. If the character is the first character of the text and is a lowercase letter:
        if i == 0 and text[i].islower(): 
            # capitalize the character
            new_char = text[i].upper()
            # Increment the counter   
            num_capitalized += 1   
        elif text[i] in ".?!":
            end_sentence = True
        elif end_sentence and text[i] != " ":
            if text[i].islower():
                new_char = text[i].upper()
                num_capitalized += 1
            
            end_sentence = False
        new_text += new_char
    return new_text, num_capitalized

if __name__ == "__main__":
    sample_text = "this is a test. This is only a test!!is this working? yes, it is."
    fixed_text, count = fix_capitalization(sample_text)
    print("Original text:", sample_text)
    print("Fixed text:", fixed_text)
    print("Number of letters capitalized:", count)