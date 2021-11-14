import csv

# file name to load
FILENAME = 'InputDataSample.csv'
data = []

# Open the file
with open(FILENAME, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append([row['Column A'], row['Column B']])

print(data)

#for i in range(100):        #can be written as for i in range data:   print(i), but too many results so far
#    for values in data[i]:
#        print(values, end="             ")
#    print("\n")

