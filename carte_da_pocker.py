#carte_da_pocker.py
#Identificare  i caratteri unicode che rappresentano i  4 semi del carte da pocker (cuori, quadri, fiori e picche) nella variante solo bordo. Creare una stringa con i 4 semi.

solo_byte = b'\xe2\x99\xa1\xe2\x99\xa2\xe2\x99\xa7\xe2\x99\xa4'  
stringa = solo_byte.decode('utf-8')
print(stringa)

