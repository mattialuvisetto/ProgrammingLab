class ExamException(Exception):
    pass


class CSVEnergyFile:
    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise ExamException("Il nome dev'essere una stringa")
        self.file_name = file_name

    def get_data(self):
        try:
            with open(self.file_name, 'r') as file:
                next(file)  # salto intestazione

                data = []

                for line in file:
                    parts = line.strip().split(',')

                    if len(parts) < 2:
                        continue

                    date = parts[0]

                    try:
                        value = int(parts[1])
                    except ValueError:
                        continue

                    if value < 0:
                        continue

                    data.append([date, value])

                return data

        except OSError:
            raise ExamException("impossibile aprire il file")
        

def compute_daily_statistics(data, start_date, end_date):

    # 1) Controlli di base sugli input
    if not isinstance(data, list):
        raise ExamException("data non è una lista")

    if not isinstance(start_date, str) or not isinstance(end_date, str):
        raise ExamException("Le date devono essere stringhe")

    if start_date > end_date: # tanto viene ocnsiderato l'ordine lessico-grafico
        raise ExamException("Intervallo di date non valido")

    # 2) Selezione dei valori nel range di date
    values_in_range = []

    for item in data:
        date = item[0]
        value = item[1]

        if start_date <= date <= end_date:
            values_in_range.append(value)

    # 3) Caso limite: almeno due misurazioni valide
    if len(values_in_range) < 2:
        raise ExamException("Non ci sono abbastanza dati nel range richiesto")

    # 4) Calcolo statistiche
    min_value = min(values_in_range)
    max_value = max(values_in_range)
    average_value = sum(values_in_range) / len(values_in_range)

    # 5) Creazione del dizionario risultato
    return {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }

    

        

        
csv = CSVEnergyFile("energy.csv")
dati = csv.get_data()
print(dati)
print(compute_daily_statistics(dati, "2024-01-01", "2024-01-07"))
