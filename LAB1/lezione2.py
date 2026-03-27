#print("Hello world!") 
#print("ciao")
#print("ciao", "gigi", sep = " separatore ", end = " idk ")

parola = "ciaomondomiserveunaparolamoltolunga"
#print(parola[-1::-1]) #serve a leggere al contrario tutta la parola, utile negli esercizi coi palindromi

#for i, item in enumerate(parola):
#    print("Posizione {}: {}".format(i, item)) #enumerate praticamente mi fornisce una lista numerata, molto comodo

def eleva_alla_n(numero, n=2): #se quando la chiamo non specifico il secondo valore, esso viene preso di default come 2
    """
    eleva un numero dato per un esponente dato o 2
    """
    return numero**n
    #così abbiamo creato una docstring

#esercizio 1

total = 538
hours = total // 60
mins = total % 60

print(f"{hours}h:{mins:02d}min")

#esercizio 2

num = int(input("Inserisci un numero intero: "))

print(f"Quadrato: {num**2}")
print(f"Cubo: {num**3}")

#esercizio 3

num = int(input("Inserisci un numero intero: "))

tipo = "pari" if num % 2 == 0 else "dispari"
print(f"{num} è {tipo}")

#in questo esercizio sfruttiamo l'operatore ternario A if cond else B

#esercizio 4

word = str(input("scegli una parola: "))
let = str(input("scegli una lettera: "))

def count_times (word, let):

    count = 0

    for letter in word.lower():

        if letter == let.lower():
            count += 1

    return count 

conta = count_times(word, let)

print(f"la lettera '{let}' appare {conta} volte nella parola '{word}'")

#python ha una funzione built-in per fare questa cosa:
word.count(let)

#esercizio 5

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:   # evita sqrt ad ogni giro
        if n % i == 0:
            return False
        i += 2          # salta i pari
    return True

num = int(input("Inserisci un numero intero positivo: "))

if is_prime(num):
    print(f"Il numero {num} è primo")
else:
    print(f"Il numero {num} non è primo")

#esercizio 6

somma = 0
while True:
    num = int(input("Inserisci un numero intero (0 per terminare): "))
    if num == 0:
        break
    somma += num

print(f"La somma vale: {somma}")

#esercizio 7

def fatt(n: int) -> int:
    if n < 0:
        raise ValueError("Il fattoriale è definito solo per interi >= 0")
    ft = 1
    for i in range(2, n + 1):
        ft *= i
    return ft

num = int(input("inserisci un intero: "))
print(fatt(num))

#esercizio 8

# un segmento deve avere un lunghezza inferiore alla somma degli altri due lati e maggiore della loro differenza

def tipo_triangolo(a: int, b: int, c: int) -> str:
    """
    Dati tre interi a, b, c, determina se formano un triangolo e, in caso affermativo,
    ritorna il tipo: 'equilatero', 'isoscele' o 'scaleno'. Altrimenti 'non valido'.
    """
    # 1) validità di base
    if a <= 0 or b <= 0 or c <= 0:
        return "non valido"

    # 2) disuguaglianze triangolari
    if not (a + b > c and a + c > b and b + c > a):
        return "non valido"

    # 3) classificazione
    if a == b == c:
        return "equilatero"
    elif a == b or a == c or b == c:
        return "isoscele"
    else:
        return "scaleno"
    
a = int(input("lato A: "))
b = int(input("lato B: "))
c = int(input("lato C: "))

print(tipo_triangolo(a,b,c))

# esercizio 9

def conta_vocali():
    stringa = input("Stringa: ")
    vocali = "aeiou"
    count = 0
 
    for letter in stringa:
        #for vocale in vocali:
        if letter.lower() in vocali: #controlla direttamente se appartiene agli elementi della stringa
            count += 1
 
    print(f"le vocali sono {count}")
    