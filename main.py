import csv

print("Welcome to Academic Advisement System")
print("Please choose a function: ")

#Create a function menu
fMenuFunctions=open("data\menu.dat",'r')
menuCount=1
for function in fMenuFunctions:
    print("{} - {}".format(menuCount,function))
    menuCount +=1

#Function checks input information
def intInput(caption):
    value=input(caption)
    try:
        intValue=int(value)
        return intValue
    except ValueError:
        return -1   #Return -1 when error

choise=intInput("Enter your choise:")
