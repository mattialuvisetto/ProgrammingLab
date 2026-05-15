# Mattia Luvisetto SM32A00024

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name # nome del file
    
    def get_data(self):

        try:

            with open (self.name, 'r') as file: 

                next(file)
                # salto la prima riga di intestazione

                data = []
                # creo una lista vuota che conterrà i valori desiderati

                for line in file:
                # ciclo sulle righe del csv

                    parts = line.strip().split(',')
                    # parts è una lista che contiene data e valore

                    if len(parts) < 2:
                        # caso di dati mancanti
                        continue 

                    date = parts[0] 
                    # la data è il primo elemento di parts

                    try:
                        value = int(parts[1])
                        # value è il secondo elemento di parts
                    except:
                        # se non è convertibile a intero escludo la riga
                        continue

                    data.append([date, value])
                    # aggiungo i dati alla lista inizialmente vuota

                # ritorno la lista creata all'inizio
                return data
            
        except FileExistsError:
            # se il file non esiste alzo l'eccezione
            raise ExamException("ERRORE: il file non esiste")
        
def compute_annual_mean(time_series, first_year, last_year):

    if not isinstance(time_series, list):
        # controllo sulla time series in input
        # non era richiesto dalla consegna 
        # ma un controllo in più aiuta
        raise ExamException("ERRORE: la time_series dev'essere di tipo lista")
    
    if not isinstance(first_year, int) or not isinstance(last_year, int):
        # controllo sugli anni in input
        raise ExamException("ERRORE: gli anni devono essere di tipo intero")
    
    if last_year < first_year:
        # controllo sull'ordine degli anni in input
        raise ExamException("ERRORE: anni in ordine sbagliato")
    
    valid_year_values = 0
    # conto i valori validi

    annual_values_sum = {}
    # creo un dizionario che contine le somme dei valori
    # per ogni anno

    annual_values_len = {}
    # allo stesso modo creo un dizionario che contiene 
    # la quantità di valori registrati per ogni anno

    # questi due dizionari tornano utili alla fine della funzione
    # per calcolare la media per ogni anno.

    for couple in time_series:
    # analizzo le coppie [data, valore] nella lista time_series

        items = couple[0].strip().split('/') 
        # couple[0] è la data in formato MM/YYYY
        # in questo modo ho diviso i mesi dagli anni
        # e posso operare sugli anni

        year = int(items[1])
        # l'anno è il secondo elemento di items (il primo è il mese)

        if year < first_year or year > last_year:
            # controllo sulla validità dell'anno considerato
            # se troppo basso o troppo alto non lo considero
            continue
        
        valid_year_values += 1

        if year not in annual_values_sum:
            annual_values_sum[year] = couple[1]
            # inizializzo la chiave anno col valore associato
        else:
            annual_values_sum[year] += couple[1]
            #faccio la somma di tutti i valori per anno

        if year not in annual_values_len:
            annual_values_len[year] = 1
            # inizializzo a 1 la chiave 
        else:
            annual_values_len[year] += 1
            # incremento fino ad avere il numero di registrazioni per anno

    if valid_year_values < 2:
        # controllo se ci sono abbastanza valori validi
        raise ExamException("ERRORE: l'intervallo non contiene"
                            "abbastamza valori validi")

    means = {}
    # creo un dizionario che conterrà le medie 
    # e verrà ritornato in output
   
    for key in annual_values_sum:
        means[key] = round(annual_values_sum[key]/annual_values_len[key], 2)
        # calcolo la media iterando su uno dei due dizionari che avevo
        # creato in precedenza. aggiungo a means le chiavi (gli anni) 
        # e calcolo le medie arrotondando a due cifre decimali
    
    # ritorno il dizionario con le medie
    return means

# prova per vedere se tutto funziona
time_series_file = CSVTimeSeriesFile("electricity.csv")
time_series = time_series_file.get_data()
print(time_series)
print(compute_annual_mean(time_series, 2019, 2021))