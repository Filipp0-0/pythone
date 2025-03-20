#Scrivete un programma per tradurre i numeri da 1 a 12 nei nomi dei mesi corrispondenti in italiano.
#mesi.py

mesi = ("Gennaio  " + 
        "Febbraio " + 
        "Marzo    " + 
        "Aprile   " + 
        "Maggio   " + 
        "Giugno   " + 
        "Luglio   " + 
        "Agosto   " + 
        "Settembre" + 
        "Ottobre  " + 
        "Novembre " + 
        "Dicembre ")

mese = int(input("Indica mese (1-12): "))
p = (mese - 1) * 9

print(mesi[p:p + 9])
