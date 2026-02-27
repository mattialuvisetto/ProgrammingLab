#print("Hello world!") 
#print("ciao")
#print("ciao", "gigi", sep = " separatore ", end = " idk ")

#esercizio 1
"""
tinmin = 538
ore = int(tinmin/60)
minuti = tinmin%60
print(f"{ore}h:{minuti}min")
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

#versione 2
word = input("choose a word: ")
let = input("choose a letter: ")
def number_of_times(let, word):
    count = 0
    for let in word:
        if let == word:
            count = count + 1
    return count
print(number_of_times(let, word))
    

#esercizio 5