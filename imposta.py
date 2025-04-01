#dal sito del agenzia dell'entrate leggiamo come l'imposta lorda si calcoli appliando al reddito complessivo, al netto degli oneri deducibili, le aliquote per scaglioni
#realizare un programma che chieda a video il reddito complessivo, al netto degli oneri deducibili, e restituisca l'imposta lorda

aliquote = (0.23, 0.25, 0.35)  
scaglioni = (28000, 50000)    
imposta = 0

reddito = int(input("Indica il reddito: "))

if reddito <= scaglioni[28000]: 
   imposta = reddito * aliquote[0.23]

else:
    if reddito > scaglioni[28000] and reddito <= scaglioni[50000]:
       imposta = (scaglioni[28000] * aliquote[0.23] +(reddito - scaglioni[28000]) * aliquote[0.25])

    else:
       imposta = (scaglioni[28000] * aliquote[0.23] +
                  (scaglioni[50000] - scaglioni[28000]) * aliquote[0.25] +
                  (reddito - scaglioni[50000]) * aliquote[0.35])

     
print("L'imposta lorda è: ", imposta)

