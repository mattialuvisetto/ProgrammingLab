class ExamException(Exception):
    pass
 
class CSVTimeSeriesFile:
    
    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        ret = []
        try:
            with open(self.name, "r") as f:
                lines = f.readlines()
                for line in lines[1:]: # skippa l'intestazione
                    l = line.strip().split(",") 
                    if l not in ret and (date_is_ordered(ret[- 1][0], l[0])if len(ret) > 0 else True):
                        ret.append(l)
        except FileNotFoundError:
            raise ExamException("Errore: file non trovato")
        except:
            raise ExamException("Errore: generico")
        return ret
 
 
def compute_variations(time_series : CSVTimeSeriesFile, first_year, last_year):
    try:
        first_year = int(first_year)
        last_year = int(last_year)
        
    except ValueError:
        raise ExamException("Errore: valori passati errati")
    lst = time_series.get_data()
    years = {}
    for i in range(first_year, last_year + 1):
        s = 0
        l = 0
        for line in lst:
            try:
                if int(line[0].split("-")[0]) == i:
                    try:
                        n = int(line[1])
                        s += int(line[1])
                        l += 1
                    except TypeError:
                        print(f"Errore: tipo non valido `{line[1]}`")
                    except ValueError:
                        print(f"Errore:valore non valido `{line[1]}`")   
            except ValueError:
                print(f"Errore nel risolvere la riga {line}")
        if l != 0:
            years[i] = s/l
    ret = {}  
    year = first_year
    while year < last_year:
        if year not in years:
            year += 1
            continue
        if (year+1) in years:
            ret[f"{year}-{year+1}"] = round((years[year + 1] - years[year]), 3)
        else:
            it = year+2
            while it not in years and it <= last_year:
                it += 1
            if it <= last_year and it in years:
                ret[f"{year}-{it}"] = round((years[it] - years[year]), 3)
                year = it
        year += 1
    if len(ret) == 0:
        raise ExamException("Errore: dati inseriti non validi")
    return ret
        
        
def date_is_ordered(date1, date2):
    date1 = date1.split("-")
    d1 = date1[0] + date1[1]
    date2 = date2.split("-")
    d2 = date2[0] + date2[1]
    return int(d2) > int(d1)
    
 
csv = CSVTimeSeriesFile(name = "data.csv")
lst = csv.get_data()
 
# for item in lst:
#     print(item)
dct = compute_variations(csv, "1949", "1960")
print("Valori finali:")
for item,key in dct.items():
    print(f"{item} : {key}")