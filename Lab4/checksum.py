ile = input('Ile chcesz sprawdzic hashy?')
tablica = []
x = 0
print tablica

while x < ile:
    hash = raw_input('Podaj kolejny hash:')
    tablica.append(hash)
    x+=1

hashToCheck = raw_input('Podaj glowny hash:')

if hashToCheck in tablica:
    print('mamy hash')
else:
    print('nie mamy')

print tablica

# hash1 = raw_input('Podaj pierwszy hash: ')
# hash2 = raw_input('Podaj drugi hash: ')
# if hash1==hash2:
#     print('Hashe sie zgadzaja', hash1,hash2)
# else:
#     print('Hashe nie zgadzaja sie')
