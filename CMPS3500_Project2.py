import csv
import os
from time import sleep
#import math
#import statistics
#import numpy


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
    with open(FILENAME, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        tempHeader = next(csvreader)
        for val in tempHeader:
            header.append(val)
        for row in csvreader:
            data.append(row)
    csvfile.close()
    
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
    

def count(data):
    return len(data)

def unique(column):
    uni = []
    for num in column:
        if num not in uni:
            uni.append(num)
    return uni

def mean(column):
    total = 0
    for count in column:
        total = total + count
    return total(column) /count
        
def mode(column):
    repeat = (0,0)
    for num in column:
        appearance = column.count(num)
        if appearance > repeat[0]:
            repeat = (appearance, num)
    return repeat[1]
        
def median(column):
    column.sort()
    if len(column) % 2 != 0:
        middle = int((len(column) - 1) / 2)
        return column[middle]
    elif len(column) % 2 ==0:
        middle1 = int(len(column) / 2)
        middle2 = int(len(column) / 2) -1
        return mean([column[middle1], column[middle2]])

#IFFY
def sd (column):
    vari = varience(column)
    std = math.sqrt(vari)
    return std

##iffy
def variance(column):
    sum = 0
    for temp in column:
        sum += (temp -mean)**2
        variance = sum//len(data)
    return variance

##iffyy ?...

def minimum(column):
    mini = column[0]
    for num in column:
        if num < mini:
            mini = num
    return mini


#maybe not 
#column or data or? 

def twenty_p(column):
    n = len(data)
    p = n * 20 /100
    return p

# = numpy.percentile(column, 20)


def forty_p(column):
    n = len(data)
    k = n * 40 / 100
    return k

def fifthy_p(column):
    n = len(data)
    j = n * 50 / 100
    return j

def sixty_p(column):
    n = len(data)
    s = n * 60/100
    return s

def eighty_p(column):
    n = len(data)
    e = n * 80 /100
    return e

def maximum(column):
    maxi = column[0]
    for numb in column:
        if numb > maxi:
            maxi = numb
    return maxi


def main():
    while 1:
        print("Current commands \n")
        print("1        -       read a file\n")
        print("2        -       print the contents of a file\n")
        print("3        -       clean a file\n")
        print("4        -       search a value\n")

        print("5        -       Print statistics of columns\n")

        print("0        -       quit\n")
        
        intInput = int(input("What would you like to do? \t"))
        
        if intInput == 1:
            # Open the file
            #fileInput = string(input("What is the name of the file?\t"))
            global FILENAME 
            FILENAME = 'InputDataSample.csv'    #FILENAME = fileInput
            fileRead(FILENAME)
            print("{} has been read!".format(FILENAME))
            sleep(3)
            clearConsole()
        elif intInput == 2:
            clearConsole()
            printData(data)
            sleep(10)
            clearConsole()
        elif intInput == 3:
            tempData = cleanFile(data)
            clearConsole()
            printData(tempData)
            sleep(10)
            clearConsole()
        elif intInput == 4:
            print("Current columns:")
            for cat in header:
                print(cat, end="\t\t\t")
            print("\n")
            colInput = str(input("What column would you like to search in?    (type all for all columns)\t\t"))
            valInput = str(input("What value would you like to find?   \t\t\t"))
            searchData(colInput, valInput)     #used to be searchData('all', '320141')
            
#        elif intInput == 5:
#           x = numpy.std(data)
#           print("std: ", x)

        elif intInput == 0:
            break
        else:
            break
        
        main()
     
    print("Terminating...\n")
    sleep(2)
    clearConsole()
    quit()

main()
