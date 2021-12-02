import csv
import os
from time import sleep

data = []
header = []
startUp = 1

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
        print(cat, end="\t\t\t")
    print("")
    for i in range(120):        #can be written as for i in range(len(input)):   print(i), but too many results so far
        for val in input[i]:
            print(val, end="\t\t\t\t")
        print("")

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
    
def searchData(column, value):
    appearNum = 0
    if column == 'all':
        for i in range(len(data)):        #can be written as for i in range(len(input)):   print(i), but too many results so far
            for val in data[i]:
                if value == val:
                    indexVal = data[i].index(value)
                    appearNum += 1
                    print("{} is present in {} row {}".format(value, header[indexVal], i)) 
        print("{} is present {} times in the data set.".format(value, appearNum))
    else:
        colnum = header.index(column)
        for i in range(len(data)):
            if value == data[i][colnum]:
                appearNum += 1
                print("{} is present in {} row {}".format(value, header[colnum], i))
        print("{} is present {} times in column '{}'".format(value, appearNum, column))
    
def main():
    while 1:
        print("Current commands \n")
        print("1        -       read a file\n")
        print("2        -       print the contents of a file\n")
        print("3        -       clean a file\n")
        print("4        -       search a value\n")
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
                tempData = cleanFile(data)
                clearConsole()
                printData(tempData)
                sleep(8)
            else:
                print("No file has been read...")
                
        elif intInput == 4:
            if len(data) > 0:
                print("Current columns:")
                for cat in header:
                    print(cat, end="\t\t\t")
                print("\n")
                colInput = str(input("What column would you like to search in?    (type all for all columns)\t\t"))
                valInput = str(input("What value would you like to find?   \t\t\t"))
                searchData(colInput, valInput)     #used to be searchData('all', '320141')
            else:
                print("No file has been read...")

        elif intInput == 0:
            break
        else:
            print("Command does not exist!")
        
        sleep(2)    
        clearConsole()
        main()
     
    print("Terminating...\n")
    sleep(2)
    clearConsole()
    quit()

main()