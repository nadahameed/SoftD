# Nada Hameed
# Soft Dev
# 06 -- build dictionary from file and use percentages as probability
# 2022-09-30
#time spent: 1hr
#DISCO:
#   - use backslash to avoid messups when putting double quotes in double quotes
#QCC:
#   - value is percentage, key is job
#   - why is there a new line at the end of the csv (or txt) file no matter what
#   -

import random

#dictionary with everything
krewes = {}
#lets read the file
file = open("occupations.csv")
#print(file.read())
text = file.read()
mrm = text.split("\n")
x = 0
for i in mrm:
    #x exists just bc there are random lns of info that shouldn't be generated
    x += 1
    if x in range(2,len(mrm)-1):
        if("," in i):
            #to deal with quotations
            if("\"" in i):
                #print("shoot")
                #print(i)
                quotes = i.split("\"")
                #print(quotes)
                perc = quotes[2]
                percc = perc[1:]
                krewes[quotes[1]] = float(percc)
            else:
                #no commas in job
                eachLn = i.split(",")
                # print("each LINE:")
                # print(eachLn)
                # print(i)
                krewes[eachLn[0]] = float(eachLn[1])
#print(krewes)

def chooseJob(krewes):
    percList = krewes.values()
    #print(percList)
    jobList = list(krewes)
    #print(jobList)
    return (random.choices(jobList, weights = (percList)))

print(chooseJob(krewes))
