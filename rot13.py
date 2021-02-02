# Codewars - 5 kyu
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in
# the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

def rot13(message):
    liste = list(message)
    for i, c in enumerate(liste):
        if c.isalpha():
            if ord(c.lower()) > 109:
                liste[i] = chr(ord(c.lower())-13)
            else:
                liste[i] = chr(ord(c.lower())+13)
            if c.isupper():
                liste[i]=liste[i].upper()
    return ''.join(liste)

spam='helmPn'
print(rot13(spam))
