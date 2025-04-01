#carte_da_poker.py
#Identificare  i caratteri unicode che rappresentano i  4 semi del carte da poker (cuori, quadri, fiori e picche) nella variante solo bordo. Creare una stringa con i 4 semi.

solo_byte = b'\xe2\x99\xa1' +
            b'\xe2\x99\xa2' +
            b'\xe2\x99\xa7' +
            b'\xe2\x99\xa4' +
stringa = solo_byte.decode()
print(stringa)

