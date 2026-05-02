class ExamException(Exception):
    pass


class CSVSalesFile:
    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise ExamException("il nome del file dev'essere una stringa")
        self.file_name = file_name

    def get_data(self):
        try:
            with open(self.file_name, 'r') as file:

                data = []
                next(file)  # salto intestazione

                for line in file:
                    parts = line.strip().split(',')

                    if len(parts) < 3:
                        continue

                    date = parts[0]

                    try:
                        amount = float(parts[1])
                    except ValueError:
                        continue

                    if amount <= 0:
                        continue

                    category = parts[2]
                    if category == '':
                        continue

                    data.append([date, amount, category])

                return data

        except OSError:
            raise ExamException("errore nell'apertura del file")
        
def compute_category_totals(data, start_date, end_date):
    if not isinstance(data, list):
        raise ExamException("errore: data non è una lista")
    if not isinstance(start_date, str) or not isinstance(end_date, str):
        raise ExamException("errore: le date devono essere in formato stringa")
    if start_date > end_date:
        raise ExamException("errore: date in ordine sbagliato")
    
    totals = {}
    valid_sales_count = 0

    for item in data:
        date = item[0]
        amount = item[1]
        category = item[2]

        if start_date <= date <= end_date:

            valid_sales_count += 1

            if category not in totals:
                totals[category] = amount
            else:
                totals[category] += amount
    
    if valid_sales_count < 2:
        raise ExamException("non ci sono ababstanza vendite nel periodo")
    
    return totals


csv = CSVSalesFile("analisivendite.csv")
data = csv.get_data()
print (data)
print (compute_category_totals(data, "2024-02-01", "2024-02-06"))   


