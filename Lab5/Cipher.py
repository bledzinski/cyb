# Your message
message = 'PTAKI LATAJA KLUCZEM'

key = 12 #Clue

mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Clue
# plaintext -> ciphertext or reversed
translated = ''
# capitalize the string in message
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # wrap-around if num > length of LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]
    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

print(translated)
