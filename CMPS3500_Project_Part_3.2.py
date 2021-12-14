import csv
import os
from time import sleep

data = []
header = []

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
def cleanFile(input, prnt):
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
            try:                                         
                if not bool(val):                                       
                    tempList.remove(i)      # row deletion
                    deleteEmpty+=1
                    
                if val == 'NA':             # column deletion
                    tempList[tempList.index(i)][i.index(val)] = 0
                    pass
                elif isinstance(float(val), float):
                    pass
                elif isinstance(int(val), int):
                    pass
                    
            except ValueError:
                if prnt:
                    print("{} removed...".format(header[i.index(val)]))                 # Automatic column deletion if a value is not at all convertible from str to float/int
                    print("{} from Row {} caused removal...".format(val, tempList.index(i) ) )
                tempList = removeColumn(i.index(val), tempList)                 
                deleteCol+=1
    
    if prnt:
        print("Deletions: \nColumn Deletions: {} \nEmpty Row Deletions: {} \nDuplicate Row Deletions: {}\n".format(deleteCol, deleteEmpty, deleteDupe))
        sleep(8)
    return tempList
    
def removeColumn(col, input):    
    tempInput = input
    header.pop(col)
    for i in range(len(tempInput)):
        try:
            tempInput[i].pop(col)
        except ValueError:
            print("Failure error occured, returning to main.  File must be read again.\n")
            data.clear()
            header.clear()
            main()
        except IndexError:
            print("Failure error occured, returning to main.  File must be read again.\n")
            data.clear()
            header.clear()
            main()
    return tempInput
 #-----------------------------------------------------------------------------------------------------------------------------------   
def searchData(column, value):
    appearNum = 0
    try:
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
            print("\n{} is present {} times in column '{}'".format(value, appearNum, column))
    except IndexError:
        print("Failure error occured, returning to main.  File must be read again.\n")
        data.clear()
        header.clear()
        main()
#-----------------------------------------------------------------------------------------------------------------------------------
def mergeSort(inputList):                                                               # Sorting Algorithm
    tempList = inputList
    if len(tempList) > 1:
        mid = len(tempList) // 2
        leftList = tempList[:mid]
        rightList = tempList[mid:]

        mergeSort(leftList)
        mergeSort(rightList)
        i = 0
        j = 0
        k = 0
        while i < len(leftList) and j < len(rightList):
            if float(leftList[i]) <= float(rightList[j]):
              tempList[k] = leftList[i]
              i += 1
            else:
                tempList[k] = rightList[j]
                j += 1
            k += 1
        while i < len(leftList):
            tempList[k] = leftList[i]
            i += 1
            k += 1
        while j < len(rightList):
            tempList[k]=rightList[j]
            j += 1
            k += 1
            
    return tempList
    
def transpose(inputList, row, col):                                                                               
    tr = [[0 for i in range(row)] for i in range(col)]
    for i in range(row):
        # Traverse each column 
        for j in range(col):
            tr[j][i] = inputList[i][j]
            
    return tr
 
def rowWiseSort(B):
    for i in range(len(B)):
        # Row - Wise Sorting
        #B[i] = sorted(B[i])            # Cannot use due to no allowance of built-in mathematical/sorting functions
        B[i] = mergeSort(B[i])           
    return B
 
def sortCol(inputList, N, M):                                              # Main body of the sorting algorithm
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if '.' in str(inputList[i][j]):
                inputList[i][j] = float(inputList[i][j])
            else:
                inputList[i][j] = int(inputList[i][j])
            
    B = transpose(inputList, N, M)
    B = rowWiseSort(B)
    inputList = transpose(B, M, N)
    
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            inputList[i][j] = str(inputList[i][j])
            
    
    return inputList
 #-----------------------------------------------------------------------------------------------------------------------------------    
def countAndUnique(input):
    countCol = []
    unique = []
    for i in range(len(header)):
        countCol.append(0)
        unique.append(0)
    uniqueNums = []
    for i in range(len(header)):
        uniqueNums.append([])
    for i in range(len(input)):
            j = 0
            for val in input[i]:
                if bool(val):
                    countCol[j] += 1
                    try:
                        if (isinstance(float(val), float) or isinstance(int(val), int)) and not (val in uniqueNums[j]):
                            uniqueNums[j].append(val)
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
    return mean
    
   
def median(input):
    medianList = []
    if ((len(input) % 2) == 1):
        for i in range(len(header)):
            medianList.append(input[    int(len(input)  /   2) ][i])
    else:
        for i in range(len(header)):
            medianCalc = float(   input[int(len(input) / 2)][i]    )    +   float(    input[ int(len(input) / 2) - 1 ][i]   )
            medianCalc = medianCalc / 2
            medianList.append(medianCalc)
    
    print("Median:", end="\t\t")
    for val in medianList:
        print("{:.2f}".format(float(val)), end="\t\t")   
    print("")
    medianList.clear()

def mode(input):
    mode = []
    for i in range(len(header)):
        mode.append(0)
    
    for j in range(len(header)):
        tempList = []
        for i in range(len(input)):
            tempList.append(input[i][j])
            
        mode[j] = max(set(tempList), key=tempList.count)
     
    print("Mode:", end="\t\t")
    for val in mode:
        print(str(float(val)), end="\t\t")    
    print("")
    mode.clear()
    
def sdAndVariance(input, meanData):
    sd = []
    variance = []
    for i in range(len(header)):
        sd.append(0)
        variance.append(0)
    
    for j in range(len(header)):
        count = 0
        for i in range(len(input)):
            try:
                variance[j] += (float(input[i][j]) - meanData[j]) ** 2
                count+=1
            except ValueError:
                pass
        variance[j] = variance[j] / (count - 1)
    
    for j in range(len(header)):
        sd[j] = variance[j] ** (1/2)
    
    print("SD:", end="\t\t")
    for val in sd:
        print("{:.2f}".format(float(val)), end="\t\t")    
    print("")
    
    print("Variance:", end="\t")
    for val in variance:
        print("{:.2f}".format(float(val)), end="\t\t")    
    print("")
    
def minMax(input):
    minMax = []
    for i in range(len(header)):
        minMax.append([999999999999999999999,-999999999999999999999])
    
    for j in range(len(header)):
        for i in range(len(input)):
            try:
                if float(input[i][j]) > minMax[j][1]:
                    minMax[j][1] = float(input[i][j])
            
                if float(input[i][j]) < minMax[j][0]:
                    minMax[j][0] = float(input[i][j])
            except ValueError:
                pass
                
    return minMax
    
    
def percentile(input, percent):
    percentile = []
    for i in range(len(header)):
        percentile.append(0)

    for j in range(len(header)):
        n = len(data)
        p = float((percent / 100) * n)
        percentile[j] = input[int(p)][j]
        # Rewrite as percentile[j] = data[int(p)][j] if it works
    
    print(str(percent) + "th %ile:", end="\t")
    for val in percentile:
        print("{:.2f}".format(float(val)), end="\t\t")  
    print("")
    percentile.clear()



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
        print("6        -       Print a sorted data set\n")
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
                data.clear()
                header.clear()
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
                cleanList = data
                cleanList = cleanFile(cleanList, 1)
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
                print("")
                searchData(colInput, valInput)     #used to be searchData('all', '320141')
                sleep(6)
            else:
                print("No file has been read...")
                
        elif intInput == 5:
            if len(data) > 0:
                print("\t\t", end="")
                for cat in header:
                    print(cat, end="\t\t")
                print("")
                print("\t\t", end="")
                for cat in header:
                    for i in range(len(cat)):
                        print("*", end="")
                    print("\t\t", end="")
                print("")
                countAndUnique(data)
                meanL = mean(data)
            
                cleanData = data
                try:
                    cleanData = cleanFile(cleanData, 0)
                    cleanData = sortCol(cleanData, len(cleanData), len(header))
                except TypeError:
                    pass
                finally:
                    median(cleanData)
                    mode(cleanData)
                    sdAndVariance(cleanData, meanL)
                    minMaxL = minMax(cleanData)
                
                    print("Min:", end="\t")
                    for i in range(len(minMaxL)):
                        print("\t" + str(float(minMaxL[i][0])), end="\t\t")    
                    print("")
                
                    percentile(cleanData, 20)
                    percentile(cleanData, 40)
                    percentile(cleanData, 60)
                    percentile(cleanData, 80)
                
                    print("Max:", end="\t\t")
                    for i in range(len(minMaxL)):
                        print("" + str(float(minMaxL[i][1])), end="\t\t")    
                    print("")
            
                meanL.clear()
                sleep(23)
            else:
                print("No file has been read...")
                
        elif intInput == 6:
            if len(data) > 0:
                cleanData = data
                cleanData = cleanFile(cleanData, 0)
                cleanData = sortCol(cleanData, len(cleanData), len(header))
                printData(cleanData)
                sleep(8)
            else:
                print("No file has been read...")
            
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
