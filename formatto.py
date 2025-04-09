#inizializare un alista con i reciproci primi 10 interi naturali, stampare i float risultanti in modo da visualizarte 8 decimali 


numeri = list(range(1, 10)) 
risultato= [ 1 / x  for x in numeri] 
for i in risultato:
    print(f"{i:.8f}")
