# Mattia Luvisetto SM32A00024

class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

        # Controllo esistenza file
        try:
            open(self.name, 'r')
        except:
            raise ExamException("File non trovato")

    def get_data(self):
        data = []

        with open(self.name, 'r') as file:
            # Salto intestazione
            next(file)

            for line in file:
                elements = line.strip().split(',')

                # Riga malformata
                if len(elements) != 2:
                    continue

                date = elements[0]

                # Valore di consumo non valido
                try:
                    consumption = float(elements[1])
                except:
                    continue

                data.append([date, consumption])

        return data


def compute_annual_mean(time_series, first_year, last_year):
    # Validazione input
    if not isinstance(first_year, int) or not isinstance(last_year, int):
        raise ExamException("Gli anni devono essere interi")

    if first_year > last_year:
        raise ExamException("Intervallo di anni non valido")

    yearly_values = {}

    for date, value in time_series:
        # Estrazione anno
        try:
            year = int(date.split('/')[1])
        except:
            continue

        if first_year <= year <= last_year:
            if year not in yearly_values:
                yearly_values[year] = []
            yearly_values[year].append(value)

    if not yearly_values:
        raise ExamException("Nessun dato valido nell'intervallo")

    # Calcolo medie
    result = {}
    for year in yearly_values:
        values = yearly_values[year]
        result[str(year)] = round(sum(values) / len(values), 2)
        # creo una chiave nel dizionario con il nome dell'anno che contiene come valore la media dell'anno

    return result



# --- Test (facoltativo) ---
if __name__ == "__main__":
    ts_file = CSVTimeSeriesFile("LAB1/electricity.csv")
    ts = ts_file.get_data()
    print(compute_annual_mean(ts, 2019, 2021))