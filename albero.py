#albero.py
#ricevuti in input: un carattere da utilizare, l'ampiezza della base
#rappresenrtare l'albero 


ampiezza = int(input("Inserisci l'ampiezza della base dell'albero: "))
carattere = input("Inserisci il carattere da utilizzare: ")

if ampiezza % 2 == 0:
    ampiezza += 1


for i in range(1, ampiezza + 1, 2):
    spazi = (ampiezza - i) // 2
    print(" " * spazi + carattere * i)

# tronco_spazi = (ampiezza - 1) // 2
# print(" " * tronco_spazi + carattere)
