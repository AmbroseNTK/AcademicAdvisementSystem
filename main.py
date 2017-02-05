import csv
import myTools
import job
import skill
import subject
import salary

flag = True
#Read all data
data = myTools.readCSV("data\JobsList.csv", 4)
fullData = myTools.readCSV("data\FullData.csv", 6)
dictonarySkills = myTools.readDictonary(fullData, 4, 5)
dictonarySubject = myTools.readDictonary(fullData, 5, 4)
dictonarySkilltoJob = myTools.readDictonary(fullData, 1, 4)

while(flag):
    myTools.clearScreen()  #Clear the screen
    print("Welcome to Academic Advisement System\n")
    print("Please choose a function: ")
    # Create a function menu
    fMenuFunctions = open("data\menu.dat", 'r')
    menuCount = 1
    for function in fMenuFunctions:
        print("{} - {}".format(menuCount, function))
        menuCount += 1
    choise = myTools.intInput("Enter your choise:")
    if(choise == 1):
        job.createMenu(data)
    if(choise == 2):
        skill.createMenu(dictonarySkills)
    if(choise == 3):
        subject.createMenu(dictonarySubject)
    if(choise == 4):
        salary.createMenu(data)
    if(choise == 5):
        skill.skillToJob(dictonarySkills, dictonarySkilltoJob)
    answer = myTools.intInput("\n1 - Select another function\n2 - Exit\n")  #Continue or Exit
    if(answer != 1):
        flag = False