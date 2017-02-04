import myTools


def createMenu(data):
    flag = True
    while(flag):
        myTools.clearScreen()
        salary = myTools.floatInput("\nPlease enter salary you want to get (USD/Year):")
        salary /= float(1000)
        print("Suitable job(s):")
        isNothing = True
        for row in range(len(data[0])):
            if((float(data[2][row]) <= salary) == True) and ((float(data[3][row]) >= salary) == True):  #Compare salary with range
                if(isNothing):
                    isNothing = False
                print(
                    "\t{} - Min salary:{} - Max salary:{}".format(data[1][row], data[2][row], data[3][row]))
        if(isNothing):
            print("Sorry, we don't have any suitable job")
        answer = myTools.intInput(
            "\n1 - Continue this function\n2 - Return to main menu\n")
        if(answer != 1):
            flag = False
