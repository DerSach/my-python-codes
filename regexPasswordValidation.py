#Codewars - 5 kyu
#You need to write regex that will validate a password to make sure it meets the following criteria:
#    At least six characters long
#    contains a lowercase letter
#    contains an uppercase letter
#    contains a number

#Valid passwords will only be alphanumeric characters.

import re
regex=re.compile(r"(?=.{6,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=^\S{,}$)(?=[a-zA-Z0-9]{,}$)")
password=input('? ')
print(regex.search(password).group())
