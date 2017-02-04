import myTools

def createMenu(data):
    flag = True
    while(flag):
        myTools.clearScreen()
        print("\tPlease select a subject you want to know:")
        count = 1
        for row in data.keys():
            print("{} - {}".format(count,row))
            count +=1
        select=myTools.intInput("Enter your choise: ")
        if(select != -1 and select<=len(data.keys())):
            print("You will have:")
            for skill in data[data.keys()[select-1]]:   #Search skills of this subject
                print("\t{}".format(skill))
        else:
            print("Sorry, input invalid")
        answer=myTools.intInput("\n1 - Continue this function\n2 - Return to main menu\n")
        if(answer != 1):
            flag=False