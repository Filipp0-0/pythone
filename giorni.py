# Scrivete un programma per tradurre i numeri da 1 a 7 nei nomi dei giorni 
#giorni.py

giorni = ("Lunedì   " + 
          "Martedì  " + 
          "Mercoledì" + 
          "Giovedì  " + 
          "Venerdì  " + 
          "Sabato   " + 
          "Domenica ")

giorno = int(input("Indica il giorno (1-7): "))
p = (giorno - 1) * 9

print(giorni[p:p + 9])
