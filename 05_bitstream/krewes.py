# Nada Hameed
# Soft Dev
# 05 -- populate krewes dictionary from txt file
# 2022-09-28
#DISCO:
#   - dictionary = {key:[value,value],key:[value,value]....}
#   - list[-n] -> last n elements of a list
#QCC:
#   - how do you add a value to a key WITHOUT CREATING A NEW PAIR mannn

import random

#open and read txt file
file = open("krewes.txt")
#print(file.read())
text = file.read()
people = text.split("@@@")

#to choose random devo later
devos = []

krewes = {}
for i in people:
    them = i.split("$$$")
    #print(i)
    print("the devo and their traits:")
    print(them)
    pd = them[0]
    if (pd not in krewes.keys()):
        krewes[pd] = them[-2]
    else:
        krewes[pd].append(them[-2])
    devos.append(them[1])
    #print("devos:")
    #print(devos)
print(krewes)
#print("devos:")
#print(devos)

#choose a random devo
randomDevo = random.choice(devos)
print(randomDevo)



#end: print a random devo and then use the dictionary
#   to print their pd and ducky too
#list = [dictionary1,dictionary2]
