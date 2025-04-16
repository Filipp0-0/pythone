# new_max.py


class Media:

    def __init__(self, txt):
        self.nome_file = txt
        self.somma = 0.0
        self.contatore = 0
        self.addendo = 0.0
        self.max_valore = float('-inf') #-inf = -infinito
        self.riga_max = -1

    def calcola_media(self):

        try:
            with open(self.nome_file, 'r') as file:

                for riga_numero, riga in enumerate(file, start=1):

                    try:
                        self.addendo = float(riga.strip())
                        self.somma += self.addendo
                        if self.addendo > self.max_valore:
                            self.max_valore = self.addendo
                            self.riga_max = riga_numero
                        self.contatore += 1

                    except ValueError:
                        print(f"Valore non valido nella riga {riga_numero}: {riga.strip()}")
                        continue

            if self.contatore > 0:
                media = self.somma / self.contatore
                print(f"La somma dei valori inseriti è: {self.somma}")
                print(f"La media dei valori inseriti è: {media}")
                print(f"Il valore massimo è: {self.max_valore} (trovato alla riga {self.riga_max})")

            else:
                print("Nessun numero valido inserito nel file.")

        except FileNotFoundError:
            print(f"Il file '{self.nome_file}' non è stato trovato.") 
            

nome_file = input("Inserisci il nome del file (includi l'estensione .txt): ")

media_calcolata = Media(nome_file)

media_calcolata.calcola_media()
