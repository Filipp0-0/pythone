#media.py
#Acquisire tramite input una sequenza di valori numerici fino a che l'utewnte non scriva "exit" 
#In tal caso stampare la media dei valori inseriti 


numero = input("Inserisci un numero: ")  
somma = 0
contatore = 0

while numero != "exit":

    try:
        numero = float(numero)
        somma += numero
        contatore += 1

    #per gestire l'errore se l'utente inserisce un valore non numerico
    except ValueError:  
        print("Valore non valido, inserisci un numero o 'exit' per terminare.") 


    numero = input("Inserisci un numero, digita 'exit' per terminare: ")

if contatore > 0:
    media = somma / contatore
    print("La media dei valori inseriti è:", media)
