# Nada Hameed
# Soft Dev
# 05 -- populate krewes dictionary from txt file
# 2022-09-28
#DISCO:
#   - dictionary = {key:[value,value],key:[value,value]....}
#   - list[-n] -> last n element of a list
#QCC:
#   - how do you add a value to a key WITHOUT CREATING A NEW PAIR mannn (resolved)
#   - can't append to objects?
#   - instead of randomly picking devo first, mb pick the pd (the key) and go from there

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
    #print("the devo and their traits:")
    #print(them)
    pd = int((them[0])[-1])

    if (pd not in krewes.keys()):
        krewes[pd] = [] #now this pd exists
    #print("XXX")
    #print(krewes)
    #print(krewes[pd])
    #print("them[-1]:")
    #print(them[1])
    person = [them[1],them[2]]
    krewes[pd].append(person)
    devos.append(them[1])
    #print("devos:")
    #print(devos)
#print(krewes)
#print("devos:")
#print(devos)

#choose a random pd
pdList = list(krewes)
ranpd = random.choice(pdList)
#print(ranpd)

valueList = krewes[ranpd]
me = random.choice(valueList)

#putting it all together
nombre = me[0]
duck = me[1]
print("this is " + nombre + " with ducky " + duck + " from period " + str(ranpd))
