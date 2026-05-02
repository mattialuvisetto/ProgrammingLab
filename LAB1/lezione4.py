# python è un linguaggio di programmazione orientata ad oggetti

class cat:
    def __init__(self, name, age): #bisogna sempre mettere init e self
        self.name = name # attributi dell'oggetto cat
        self.age = 13
    
    def miagola(self):
        print("miao")

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

gatto = cat("Tom", 13)
print(gatto.name)


# ESERCIZIO 1

class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self._speed = 0

    @classmethod
    def from_string(cls, s):
        parts = s.split(",")
        marca = parts[0]
        modello = parts[1]
        anno = int(parts[2])
        return cls(marca, modello, anno)

    def accelera(self):
        self._speed += 5

    def frena(self):
        self._speed = max(0, self._speed - 5)

    def get_speed(self):
        return self._speed

    def __str__(self):
        return (
            f"{self.marca} {self.modello} ({self.anno}) - "
            f"{self._speed} km/h"
        )


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def __str__(self):
        return (
            f"Auto {self.marca} {self.modello} ({self.anno}) - "
            f"{self.numero_porte} porte - {self.get_speed()} km/h"
        )


class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def __str__(self):
        return (
            f"Moto {self.marca} {self.modello} ({self.anno}) - "
            f"{self.tipo} - {self.get_speed()} km/h"
        )
                
                 

# ESERCIZIO 2

class CSVFile:
    def __init__(self, name):
        # Salvo il nome del file come attributo
        self.name = name

    def get_data(self):
        data = []  # qui salveremo i dati

        # Apro il file in lettura
        with open(self.name, 'r') as f:
            for line in f:
                # Tolgo eventuali spazi e newline
                line = line.strip()

                # Divido la riga in una lista
                elements = line.split(',')

                # Aggiungo la lista alla lista totale
                data.append(elements)

        return data


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