#Acquisire una serie di numeri interi addottando un valore sentinella per terminare la lettura (input()). Quindi stampare il valore massimo. Adottare q come valore sentinella.

numero = 0
q = "q"
numeri = []

while numero != q:
    numero = input("Inserisci un numero intero, digita 'q' per terminare: ")

    if numero != q:
        try:
            numeri.append(int(numero))
        except ValueError:
            print("Errore: inserire solo numeri interi o 'q' per terminare.")
        
if numeri:  
    
    massimo = numeri[0]

    for numero in numeri:
        if numero > massimo:
            massimo = numero
            
    print("Il valore massimo è:", massimo)




