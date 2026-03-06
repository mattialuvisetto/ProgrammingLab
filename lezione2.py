#print("Hello world!") 
#print("ciao")
#print("ciao", "gigi", sep = " separatore ", end = " idk ")

#esercizio 1
"""
tot = 538
ore = int(tot/60)
# ore = time//60 divisione in intero
minuti = tot%60
print(f"{ore}h:{minuti}min")
"""

"""

"""

#esercizio 2
"""
num = input("scegli un numero intero: ")
num = int(num)
print(num**2, num**3)
"""

#esercizio 3
"""
num = input("scegli un numero intero: ")
num = int(num)
print(num % 2 == 0)
"""

#esercizio 4
"""
#versione 1
word = input("choose a word: ")
let = input("choose a letter: ")
len = len(word)
def number_of_times(let, word, len):
    count = 0
    for i in range(len):
        if let == word[i]:
            count = count + 1
    return count

print(number_of_times(let, word, len))
"""

#funzione enumerate 
#versione 2
"""
def contalettere(lettera, parola):
    lettera = lettera.lower()
    parola = parola.lower()
    print("Dopo lower: {parola}")
    k = 0
    for item in parola:
        print(item)
        if(item == lettera):
            k = k + 1

    for idx, item in enumerate(parola):
        ...
"""



#esercizio 5
"""
x = (int (input("scegli un numero: ")))
 
def primo (x):    #funzione che dato un numero verifica se è primo o meno
    for i in range(2, x):
        if (x%(i) == 0):
            print (f"{x} non è primo")
            return
    print (f"{x} è primo")
 
primo(x)
"""

#esercizio 6
"""
print("inserire numeri, inserire 0 per fermarsi")
sum = 0
x = int(input())
while x!=0:
    sum = sum + x
    x = int(input())
print(sum)
"""

#esercizio 7
"""
def fatt(num: int):
    n = 1
    for i in range(num):
        n *= (i + 1)
    return n
 
x = int(input())
print(fatt(x))
"""

#esercizio 8

# un segmento deve avere un lunghezza inferiore alla somma degli altri due lati e maggiore della loro differenza
"""
a = (int(input ("scegli il lato a: ")))
b = (int(input ("scegli il lato b: ")))
c = (int(input ("scegli il lato c: ")))
 
def controllo_somma (a,b,c):
    errore=0
    if a>b+c:
        errore=errore+1
    if b>a+c:
        errore=errore+1
    if c>b+a:
        errore=errore+1
    return errore
 
 
def controllo_differenza (a,b,c):
    errore=0
    if a<b-c:
        errore=errore+1
    if b<a-c:
        errore=errore+1
    if c<b-a:
        errore=errore+1
    return errore
 
def tipo_triangolo (a,b,c):
   
    if (a==b or b==c or c==a):
        if (a==b==c):
            print ("è un triangolo equilatero")
        else:
            print ("è un triangolo isoscele")
    if ((a^2 + b^2 == c^2) or (c^2 + b^2 == a^2) or (a^2 + c^2 == b^2)):
        print ("è un triangolo rettangolo")
    else:
        print ("è un triangolo scaleno")
 
if (controllo_somma (a,b,c) +controllo_differenza (a,b,c) ==0):
    print ("questo puo essere un triangolo")
    tipo_triangolo (a,b,c)
else:
    print ("questo NON puo essere un triangolo")
"""

#esercizio 9
"""
def conta_vocali():
    stringa = input("Stringa: ")
    vocali = "aeiou"
    count = 0
 
    for letter in stringa:
        #for vocale in vocali:
        if letter.lower() in vocali:
            count += 1
 
    print(f"le vocali sono {count}")
 
conta_vocali()
"""