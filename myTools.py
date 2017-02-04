import csv
import os
#This is a tools library
#Function checks input information
def floatInput(caption):
    value=raw_input(caption)
    try:
        floatValue=float(value)
        return floatValue
    except:
        return -1   #Return -1 when error
#Read integer number
def intInput(caption):
    return int(floatInput(caption))

def contain(value,iList):
    for row in iList:
        if value == row:
            return True
    return False
#Read file csv to multilist
def readCSV(fileName,cols):
    data=[]
    with open(fileName,'r') as myFile:
        myData=csv.reader(myFile,delimiter=';')
        for i in range(cols):
               data.append([])
        for line in myData:
            for i in range(cols):
                if(line[i] !=""):
                    data[i].append(line[i])
    return data
#Change list to dictonary
def readDictonary(data,colKey,colValue):
    dictonary={}
    for row in range(len(data[colKey])):
        if(data[colKey][row] not in dictonary):
            dictonary[data[colKey][row]]=[]
        if(data[colValue][row] not in dictonary[data[colKey][row]]):
            dictonary[data[colKey][row]].append(data[colValue][row])
    return dictonary

#Clear screen
def clearScreen():
    os.system("cls")