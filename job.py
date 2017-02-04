import myTools

def createMenu(data):
    flag=True
    while(flag):
        myTools.clearScreen()
        print("\tPlease select a job you want to know:")
        for i in range(len(data[0])):
            print("{} - {}".format(data[0][i],data[1][i]))
        select=myTools.intInput("Enter your choise: ")
        if(select != -1 and select <=len(data[0])):
            subData=myTools.readCSV("data\{}".format(str(select)+".csv"),2)
            #Show all data about this job
            print("\nJob: {}\nMin salary: {} USD/Year\nMax salary: {} USD/Year\nYou should have skills:".format(data[1][select-1],data[2][select-1],data[3][select-1]))
            for i in range(len(subData[0])):
                print("\t{}".format(subData[0][i]))
            print("You should learn subjects: ")
            for i in range(len(subData[1])):
                print("\t{}".format(subData[1][i]))
        else:
            print("Sorry, input invalid")
        answer=myTools.intInput("\n1 - Continue this function\n2 - Return to main menu\n")
        if(answer != 1):
            flag=False