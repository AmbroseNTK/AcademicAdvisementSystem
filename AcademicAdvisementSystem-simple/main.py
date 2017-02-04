import csv
import os

def readCSV(fileName):
    data = csv.reader(open(fileName,'r'),delimiter=';')
    table=[]
    for row in data:
        table.append(row)
    return table
def createMenu(data):
    i = 1
    for row in data:
        print("{} - {}".format(i,data[i-1][1]))
        i +=1
    try:
        #select = int(input("Enter your choise: "))
        select =3
        if(select>=1 and select <=i):
            return select
    except:
        return -1
def searchJobByID(id,data):
    row = data[id-1]
    for i in range(len(row)):
        cap=""
        if(i == 1):
            cap="Job: {}"
        if(i == 2):
            cap = "Min salary: {}"
        if(i ==3):
            cap="Max salary: {}"
        if(i >=4):
            if(i == 4):
                print("Skill(s):")
            if(row[i]==""):
                print("Subject(s):")
            cap="\t{}"
        print(cap.format(row[i]))

flag = True
data = readCSV("FullData.csv")
while(flag):
    os.system("cls")
    print("\tWelcome to Academic Advisement System\n")
    select=createMenu(data)
    if(select !=-1):
        searchJobByID(select,data)
    else:
        print("Sorry, Input invalid !\n")
    ans=input("1 - Continue\n2 - Exit\n")
    if(ans!="1"):
        flag =False