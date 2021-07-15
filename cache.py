import csv
def writeCSV(movies,dest='movies.csv'):
    with open(dest, 'w', newline='') as csvfile:
        fieldnames = ['title', 'year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for m in movies:
            writer.writerow({'title': m[0], 'year': m[1]})

def readCSV(source='movies.csv'):
    result=[]
    with open(source, newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             result.append((row['title'],row['year']))

    return result

