import random

class Coin:
    def __init__(self, faccia):
        # Attributo della faccia della moneta
        self.faccia = faccia

    def lanciare(self):
        # Simula il lancio scegliendo "testa" o "croce"
        #self.faccia = random.choice(["testa", "croce"])
        if random.randint(0,1) == 0:
            self.faccia = "Testa"
        else:
            self.faccia = "Croce"

    def che_faccia(self):
        # Ritorna il valore dell'attributo 'faccia'
        return self.faccia


# --- ESEMPIO D'USO ---
moneta = Coin("Testa")     # creo un oggetto Coin
moneta.lanciare()     # simulo un lancio
print(moneta.che_faccia())  # stampo il risultato