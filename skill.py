import myTools

listID = [] #List skills

#Create list skills
def showListSkill(data):
    count = 1
    for row in data.keys():
        print("{} - {}".format(count, row))
        listID.append(row)
        count += 1

def createMenu(data):
    flag = True
    while(flag):
        myTools.clearScreen()
        print("\tPlease select a skill you want to know:")
        showListSkill(data)
        select = myTools.intInput("Enter your choise: ")
        if(select != -1 and select <= len(data.keys())):
            print("You should learn:")
            for subject in data[data.keys()[select - 1]]:   #Search subjects of this skill
                print("\t{}".format(subject))
        else:
            print("Sorry, input invalid")
        answer = myTools.intInput(
            "\n1 - Continue this function\n2 - Return to main menu\n")
        if(answer != 1):
            flag = False

#Search skill in jobs
def skillToJob(data, dictonary):
    flag = True
    while(flag):
        myTools.clearScreen()
        print("\tPlease select skill(s) you had:")
        showListSkill(data)
        select = raw_input("Enter list skill you had:(Example: 1,7,18,25)\n")
        listSkillID = select.split(",")
        listNoNull=[]
        for skillID in listSkillID:
            if(skillID not in listNoNull):
                listNoNull.append(skillID)
        listSkillID=listNoNull
        listSkill = []
        for skillID in listSkillID:
            try:
                listSkill.append(listID[int(skillID) - 1])
            except:
                continue
        countJobs = {}
        for job in dictonary.keys():
            countJobs[job] = 0
            for skill in listSkill:
                if(skill in dictonary[job]):
                    countJobs[job] += 1
        rateJobs = {}
        for job in dictonary.keys():
            if(countJobs[job] == 0):
                continue
            rateJobs[job] = float(countJobs[job]) / float(len(dictonary[job])) * 100.0  #Calculate a rate
        sortList = sorted(rateJobs, key=rateJobs.__getitem__, reverse=True) #sort a decreasing rate
        print("List of suitable job(s)")
        for job in sortList:
            print("\t{} - Rate: {} %".format(job, rateJobs[job]))
        answer = myTools.intInput("\n1 - Continue this function\n2 - Return to main menu\n")
        if(answer != 1):
            flag = False
