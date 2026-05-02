class ExamException (Exception):
    pass

class CSVTemperatureFile():
    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise ExamException("errore: il nome del file dev'essere di tipo stringa")
        self.file_name = file_name
    
    def get_data(self):
        try:
            with open (self.file_name, 'r') as file:
                next(file)
                for line in file:
                    parts = line.strip().split(',')
                    date = parts[0]
                    try:
                        temp = float(parts[1])
                    except:
                        continue
            

        except OSError:
            raise ExamException("errore ell'apertura del file")
    