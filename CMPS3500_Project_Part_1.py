import csv
data = []

def printData(input):
    for i in range(len(input)):        #can be written as for i in range(len(input)):   print(i), but too many results so far
        for val in input[i]:
            print(val, end="\t\t\t\t")
        print("")
        
def fileRead(filename):
    # file name to load
    with open(FILENAME, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for cat in header:
            print(cat, end="\t\t\t")
        print("")
        for row in csvreader:
            data.append(row)
    csvfile.close()

def cleanFile(input):
    tempList = input
    uniqueNums = []
    deletes = 0;
    for i in range(120):
        for val in tempList[i]:
            if not bool(val):            # if an entry in either column is empty
                #do the remove here
                tempList.remove(input[i])
                deletes+=1
                break
            elif not val.isnumeric():
                tempList.remove(input[i])
                deletes+=1
                break
            elif val in uniqueNums:
                tempList.remove(input[i])
                deletes+=1
                break
            else:
                uniqueNums.append(val)
    print("Deletions: %d" % deletes)
    return tempList
    
    
# Open the file
FILENAME = 'InputDataSample.csv'
fileRead(FILENAME)


data[100] = (("hello", "lol"))              #This is for debugging dupes and nonnummeric
data[2] = (('320141', '978515'))            
printData(data)
#tempData = cleanFile(data)

