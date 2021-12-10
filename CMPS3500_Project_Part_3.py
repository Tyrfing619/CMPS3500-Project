import csv
import os
from time import sleep

data = []
header = []
countCol = []

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def fileRead(filename):
    # file name to load
    try:
        with open(FILENAME, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            tempHeader = next(csvreader)
            for val in tempHeader:
                header.append(val)
            for row in csvreader:
                data.append(row)
        csvfile.close()
    except OSError:
        print("Failed to open file! File may be corrupted...")
    
def printData(input):
    for cat in header:
        print(cat, end="\t")
        
    print("")
    for i in input:        #can be written as for i in input:   print(i), but too many results so far
        for val in i:    #for val in i
            print(val, end="\t\t")
        print("")
    print("")
    for cat in header:
        print(cat, end="\t")
    print("")
 #-----------------------------------------------------------------------------------------------------------------------------------       
def cleanFile(input):
    tempList = input
    uniqueRows = []
    deleteCol = 0
    deleteEmpty = 0
    deleteDupe = 0
    for i in tempList:
        if i in uniqueRows:
            tempList.pop(tempList.index(i))
            deleteDupe+= 1
        else:
            uniqueRows.append(i)
            for val in i:   
                try:                                                                                        # Column Deletion
                    if not bool(val):
                        tempList.remove(i)
                        deleteEmpty+=1
                    if val == 'NA':
                        pass
                    elif isinstance(float(val), float):
                        pass
                    elif isinstance(int(val), int):
                        pass
                    else:
                        print("{} removed...".format(header[i.index(val)]))
                        print("{} from Row {} caused removal...".format(val, tempList.index(i) ) )
                        tempList = removeColumn(i.index(val), tempList) 
                        deleteCol+=1
                    
                except ValueError:
                    print("{} removed...".format(header[i.index(val)]))
                    print("{} from Row {} caused removal...".format(val, tempList.index(i) ) )
                    tempList = removeColumn(i.index(val), tempList) 
                    deleteCol+=1
    
    print("Deletions: \nColumn Deletions: {} \nEmpty Row Deletions: {} \nDuplicate Row Deletions: {}\n".format(deleteCol, deleteEmpty, deleteDupe))
    sleep(8)
    return tempList
    
def removeColumn(col, input):    
    tempInput = input
    header.pop(col)
    for i in range(len(tempInput)):
        for val in tempInput[i]:
            try:
                tempInput[i].pop(col)
            except ValueError:
                pass
            except IndexError:
                pass
    return tempInput
 #-----------------------------------------------------------------------------------------------------------------------------------   
def searchData(column, value):
    appearNum = 0
    if column == 'all':
        for i in range(len(data)):        #can be written as for i in range(len(input)):   print(i), but too many results so far
            for val in data[i]:
                if value == val:
                    indexVal = data[i].index(value)
                    appearNum += 1
                    print("{} is present in {} row {}".format(value, header[indexVal], i+1)) 
        print("{} is present {} times in the data set.".format(value, appearNum))
    else:
        colnum = header.index(column)
        for i in range(len(data)):
            if value == data[i][colnum]:
                appearNum += 1
                print("{} is present in {} row {}".format(value, header[colnum], i+1))
        print("{} is present {} times in column '{}'".format(value, appearNum, column))

 #-----------------------------------------------------------------------------------------------------------------------------------    
def sort(input):                                                                                    #needs to be a cleaned data set!
    tempData = input
    changed = 1
    while changed:
        changed = 0
        for i in range(len(tempData)):
            for j in range(len(tempData[i])):
                if (i+1) != len(tempData):
                    if tempData[i][j] > tempData[i+1][j]:
                        temp = tempData[i+1][j]
                        tempData[i+1][j] = tempData[i][j]
                        tempData[i][j] = temp
                        changed = 1
    return tempData
 
def countAndUnique(input):
    unique = []
    for i in range(len(header)):
        countCol.append(0)
        unique.append(0)
    uniqueNums = []
    for i in range(len(input)):
            j = 0
            for val in input[i]:
                if bool(val):
                    countCol[j] += 1
                    try:
                        if (isinstance(float(val), float) or isinstance(int(val), int)) and not (val in uniqueNums):
                            uniqueNums.append(val)
                            unique[j] += 1
                    except ValueError:
                        pass
                j+=1
    print("Count:", end="")
    for val in countCol:
        print("\t\t" + str(val), end="\t")
    print("\nUnique:", end="")
    for val in unique:
        print("\t\t" + str(val), end="\t")
    print("")

def mean(input):
    mean = []
    for i in range(len(header)):
        mean.append(0)
    for i in range(len(data)):
        j = 0
        for val in data[i]:
            if bool(val):
                    try:
                        if isinstance(float(val), float) or isinstance(int(val), int):
                            mean[j] += float(val)
                    except ValueError:
                        pass
            j += 1
    for i in range(len(mean)):
        mean[i] = int(mean[i] / len(data))
        
    print("Mean:", end="")
    for val in mean:
        print("\t\t" + str(val), end="\t")
    print("")
   
    
    
 #-----------------------------------------------------------------------------------------------------------------------------------   
    
    
def main():
    cleanList = []
    while 1:
        clearConsole()
        print("Current commands \n")
        print("1        -       read a file\n")
        print("2        -       print the contents of a file\n")
        print("3        -       clean a file\n")
        print("4        -       search a value\n")
        print("5        -       Statistics\n")      
        print("0        -       quit\n")
        while 1:
            try:
                intInput = int(input("What would you like to do? \t"))
                break
            except ValueError:
                print("Please have a valid input...")
        print("\n\n")
        if intInput == 1:
            # Open the file
            try:
                fileInput = input("What is the name of the file?\t")
                global FILENAME 
                FILENAME = fileInput    #FILENAME = fileInput
                fo = open(FILENAME, newline='')
                fo.close()
                fileRead(FILENAME)
                print("{} has been read!".format(FILENAME))
            except FileNotFoundError:
                print("\n\nFile does not exist!")
                
        elif intInput == 2:
            if len(data) > 0:
                clearConsole()
                printData(data)
                sleep(8)
            else:
                print("No file has been read...")
                
        elif intInput == 3:
            if len(data) > 0:
                cleanList = cleanFile(data)
                printData(cleanList)
                sleep(8)
            else:
                print("No file has been read...")
                
        elif intInput == 4:
            if len(data) > 0:
                clearConsole()
                print("Current columns:")
                for cat in header:
                    print(cat, end="\t\t\t\t")
                print("\n")
                colInput = str(input("What column would you like to search in?    (type all for all columns)\t\t"))
                valInput = str(input("What value would you like to find?   \t\t\t"))
                searchData(colInput, valInput)     #used to be searchData('all', '320141')
                sleep(6)
            else:
                print("No file has been read...")
        elif intInput == 5:
            print("\t\t", end="")
            for cat in header:
                print(cat, end="\t\t")
            print("")
            countAndUnique(data)
            mean(data)
            sleep(6)
            #cleanData = cleanFile(data)
            #cleanData = sort(cleanData)
                
            
        elif intInput == 0:
            break
        else:
            print("Command does not exist!")
        
        sleep(2)    
        main()
        
    print("Terminating...\n")
    sleep(2)
    clearConsole()
    quit()

main()
