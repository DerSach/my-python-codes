# Codewars - 6 kyu

# Alternative solution:
# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

# Loading dictionnary for test 'S O S' and 'HEY JUDE'
MORSE_CODE = {'....':'H','-.--':'Y', '.':'E', '-..' : 'D', '..-':'U', '.---':'J','...':'S','---':'O'}

def decodeMorse(morse_code):
    morse_codeList = morse_code.split(' ')
    for i, j in enumerate(morse_codeList):
        try:
            morse_codeList[i] = MORSE_CODE[j]
        except KeyError:
            continue
    for i in range(len(morse_codeList)-1):
        if morse_codeList[i] == morse_codeList[i+1] == '':
            morse_codeList[i] = ' '
    return ''.join(morse_codeList).replace('  ',' ').strip()

spam1 = '...   ---   ...'
spam2 = '.... . -.--   .--- ..- -.. .'
print(decodeMorse(spam1))
print(decodeMorse(spam2))
