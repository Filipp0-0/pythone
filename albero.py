#albero.py
#ricevuti in input: un carattere da utilizare, l'ampiezza della base
#rappresenrtare l'albero 


ampiezza = int(input("Inserisci l'ampiezza della base dell'albero: "))
carattere = input("Inserisci il carattere da utilizzare: ")


if ampiezza % 2 == 0:
    ampiezza += 1


i = 1
while i <= ampiezza:
    spazi = (ampiezza - i) // 2
    print(" " * spazi + carattere * i)
    i += 2  

