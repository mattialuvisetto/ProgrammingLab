my_list = [1,2,3] # Lista di numeri
my_list = ['Marco','irene','paolo'] # Lista di stringhe

x = [23,3,2,65, 6,7,8,9,10]
y = x[1:6:2] # dall'elemento di indice 1 all'elemento di indice 6 (escluso), con step 2
z = x[::2] # dall'inizio alla fine, con step 2.
x.append(67) #mi aggiunge un elemento alla lista
x[1:3]=[] #elimino gli elementi dall'indice 1 all'indice 3 (escluso)
#le stringhe invece sono immutabli

saluti = "Hello, world!"
nuovi_saluti = 'B' + saluti[1:] #prende le lettere dall'indice 1 in poi, quindi sostituisce la H
#print(nuovi_saluti )

list1 = ['Carlo', 'Magno']
list2 = list1 #in questo modo la lista 2 punta all'indirizzo di lista 1
list3 = list1[:] #per copiare senza puntare alla stessa memoria
list4 = list1.copy #per copiare senza puntare alla stessa memoria
#il metodo append non crea una nuova lista, modifica e basta quella esistente

data = "2025-03-02"
parti = data.split("-")
#print(parti)

my_dict1 = {'Trieste': 34100, 'Padova': 35100} # stringa -> numero
diz1 = dict()
diz2 = {}

my_dict2 = {34100: 'Trieste', 35100: 'Padova'} # numero -> stringa
my_dict3 = {'Trieste': 'TS', 'Padova': 'PD'} # stringa -> stringa
#print(my_dict1['Trieste']) #accedo al valore nella chiave Trieste

my_dict1['Venezia'] = 30121 # aggiungere un elemento
my_dict1['Venezia']=30100 # cambiare un valore

# del my_dict1['Padova'] # cancellare un elemento

#IMPORTANTE: Nei dizionari, in verifica la presenza nelle chiavi, non nei valori.

#my_dict1.keys() #mi restituisce le chiavi
#my_dict1.values() #mi restituisce i valori
#my_dict1.items() #mi restituisce le coppie chiave-valore

#Se vuoi una lista vera e propria devo fare il cast. E.g.list(my_dict.keys())

(a,b,c) = (1,2,3) #posso usare le tuple per assegnare pù valori alla volta
t = (5,)   # tupla
x = (5)    # NON è una tupla: è solo un int

a={'a','a','a','c','b','s'} #a=set('s','5')
b = set('abracadabra')
#print(type(a),type(b))
#print ('a - b ', a - b) # differenza
#print ('a | b ', a | b) # unione, or logico.
#print ('a & b ', a & b) #intersezione, and logico.
#print('a^b ' , a^b) #simmetric difference
#print('a' in a)

"""
my_file = open('data/shampoo_sales.csv', 'r')
print(my_file.read())
my_file.close() #sempre chiudere il file una volta aperto
"""
"""
with open('data/shampoo_sales.csv') as file:
    print(file.read()) #per evitare di dover chiudere ogni volta il file
"""
import os
cwd = os.getcwd() #current working directory
#print(cwd)

# Apro il file
my_file = open('data/shampoo_sales.txt', 'r')
# Leggo il contenuto
my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)
# Chiudo il file
my_file.close()

# Il file si può anche leggere riga per riga, una alla volta:

my_file = open('shampoo_sales.csv', 'r')
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()

# il file si può anche leggere riga per riga tutto in un colpo in modo “pythonico”:

my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    print(line)
my_file.close()

# Una stringa come '/Users/laura/git/MyProgrammingLab', che individua la
# collocazione di un file o una directory, è chiamata percorso

os.path.abspath('shampoo_sales.csv') # per avere il path assoluto

# e se volessimo scrivere su file:

"""
my_file = open('saluti.txt', 'w')
my_file.write('Ciao mondo!')
my_file.close()
"""

#oppure

"""
with open ("Saluti.txt", "w") as file:
    file.write("ciao mondo")
"""

# per aggiungere testo a un file

"""
my_file = open('saluti.txt', 'a') # da notare "a"
my_file.write('Addio!')
my_file.close()
"""

# Per leggere i dati da un file CSV bisogna fare un po’ di cose:
# 1) Il metodo “.split” per separare le stringhe su uno specifico carattere;

"""
mia_stringa = 'Date,Sales\n'
lista_elementi = mia_stringa.split(',')
print(lista_elementi)
"""

# 2) La conversione di una stringa a valore numerico (floating point);

"""
mia_stringa = '5.5'
mio_numero = float(mia_stringa)
"""

# 3) Sapere come aggiungere un elemento ad una lista.
"""
mia_lista = [1,2,3]
mia_lista.append(4)
"""

# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open('shampoo_sales.csv','r')

for line in my_file:
    # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')

    # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
        
        # Setto la data e il valore
        date = elements[0]
        value = elements[1]
        
        # Aggiungo alla lista dei valori questo valore
        values.append(value)

#-------------- ESERCIZI --------------

# esercizio (1)
# Scrivete una funzione che sommi tutti gli elementi di una lista

mylist = [1,2,3,4,5,6,7]

def list_sum (mylist):
    somma = 0
    for i in mylist:
        somma += i
    return somma

print(list_sum(mylist))

# esercizio (2)
# Scrivere una funzione che prende in input una stringa e ritorna True se è un
# palindromo, False altrimenti.

s = "suus"

def is_palindrome(s):
    # Trasformo la stringa in minuscolo
    s = s.lower()

    # Creo una nuova stringa al contrario
    inverted = ""
    for char in s:
        inverted = char + inverted

    # Confronto la stringa originale con quella invertita
    if s == inverted:
        return True
    else:
        return False
    
print(is_palindrome(s))

# esercizio 3
# Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di
# A[i] con A[j].

def scambia_elementi(mylist,i,j):
    if len(mylist) < j:
        return "lista troppo corta"
    else:
        tmp = mylist[i]
        mylist[i] = mylist[j]
        mylist[j] = tmp
    return mylist

mylist = [1,2,3,4,5,6,7,8,9]
mylist = scambia_elementi(mylist,2,11)
print(mylist)

# esercizio 4
# Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno
# almeno un elemento in comune

mylist1 = [1,2,3,4,5,6,7]
mylist2 = [8,9,10,11,12,13,14,1]

def check_sim (mylist1, mylist2):
    for item in mylist1:
        if item in mylist2:
            return True
    return False

print(check_sim(mylist1,mylist2))

# esercizio 5
# Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una
# lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] ->
# ["uno","zero","sette","nove","otto"]

def transform_nums (mylist):  
    new_list = []

    dict = {0 : "zero", 1 : "uno", 2 : "due", 3 : "tre", 4 : "quattro", 5 : "cinque", 6 : "sei", 7 : "sette", 8 : "otto", 9 : "nove"}

    for num in mylist:
        new_list.append(dict[num])
    
    return new_list

# esercizio 6
# Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il
# conteggio delle occorrenze

word_list = ["ciao", "ok", "ok", "ciao", "ciao", "salve"]

