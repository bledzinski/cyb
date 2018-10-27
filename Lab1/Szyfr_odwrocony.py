#Szyfr odwrócony

'''
Wykorzystane zmienne:

wiadomosc   : dowolny ciąg znaków do zaszyfrowania.
szyfrowanie : lista wykorzystane do zapisu znaków
i           : inkrementacja
'''

wiadomosc = 'awotset csomodaiW .awtsnezceipzebrebyc z muirotarobal ezswreiP'


szyfrowanie = ''

i = len(wiadomosc) - 1 #len liczone od 1!

while i >= 0:
    szyfrowanie = szyfrowanie + wiadomosc[i] #Indeksowanie (wiadomosc[i]) liczone od 0!

    i = i - 1
szyfrowanie = "".join(map(lambda ch: "" if ch==" " else ch, szyfrowanie))
print(szyfrowanie)