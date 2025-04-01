
#media.py
#Acquisire tramite input una sequenza di valori numerici fino a che l'utewnte non scriva "exit" 
#In tal caso stampare la media dei valori inseriti 


numero = input("Inserisci un numero: ")  
somma = 0
contatore = 0

while numero != "exit":

    try:
        numero = float(numero)

    except ValueError:  
      print("Valore non valido, inserisci un numero o 'exit' per terminare.") 
    numero = input("Inserisci un numero, digita 'exit' per terminare: ")

    continue   
somma += numero
contatore += 1
numero = input("Inserisci un numero, digita 'exit' per terminare: ")

if contatore > 0:
    media = somma / contatore
    print("la somma dei valori inseriti è:", somma)
    print("La media dei valori inseriti è:", media)



