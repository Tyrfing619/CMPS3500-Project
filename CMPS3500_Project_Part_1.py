import csv

# file name to load
FILENAME = 'InputDataSample.csv'
data = []

# Open the file
with open(FILENAME, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for cat in header:
        print(cat, end="\t\t\t")
    print("")
    for row in csvreader:
        data.append(row)

csvfile.close()
for i in range(100):        #can be written as for i in range data:   print(i), but too many results so far
    for val in data[i]:
        print(val, end="\t\t\t\t")
    print("")                                         

