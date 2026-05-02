# VERSIONE 1

class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self,window_length):

        self.window_length = window_length

        if not isinstance(window_length,int):
            raise ExamException("errore: la lunghezza dev'essere intera")

        if window_length <= 0:
            raise ExamException("errore: la lunghezza dev'essere > 0")


    def compute(self,data):
        if not isinstance(data,list):
            raise ExamException("errore: data non è una lista")
        
        if data == []:
            raise ExamException("errore: la lista è vuota")
        
        if len(data) < self.window_length:
            raise ExamException("lista troppo corta")
        
        data_new = []
        
        for elem in data:
            if not isinstance(elem, (int, float)):
                raise ExamException(f"Errore, l'elemento '{elem}' della lista non è int")
            

        for i in range(len(data) - self.window_length+1):

            med = (sum(data[i : i + self.window_length])/self.window_length)

            data_new.append(med)
        
        return data_new
 
moving_average = MovingAverage(1)
result = moving_average.compute([2,4,8,16])
print("Senza eccezioni: ", result)

# VERSIONE 2

class ExamException(Exception):
    pass
 
class MovingAverage():
    def __init__(self, window):
        if(window != int(window)): # meglio usare isinstance
            raise ExamException('Il valore da inserire deve essere di tipo intero\n')
        self.window = window
        # manca caso negativo
        
    def compute(self, lista):
        if(lista != list(lista)): raise ExamException('Deve essere inserita una lista\n')
        if(lista == []): raise ExamException('Errore, lista valori vuota\n')
        for item in lista:
            try:
                if(item != float(item)): raise ExamException('I valori nella lista devono essere numeri\n')
            except ValueError:
                raise ExamException('I valori nella lista devono essere numeri\n')
        if(len(lista)<self.window): raise ExamException("La lunghezza della finestra non può essere maggiore di quella della lista\n")
        media_m = []
        for i in range(0, len(lista), self.window):
            sum = 0
            for idx in range(i, i+self.window, 1):
                sum = sum + lista[idx]
            media_m.append(sum/self.window)
        return media_m
 
lista = [2, 4, 8, 16]
media_mobile = MovingAverage (2)
media = media_mobile.compute(lista)
print(media)