#!/usr/bin/python
import numpy 
data = open("data.dat","r")
lines = data.readlines()
#print(lines)
names = []
for l in lines:     #Extracting names 
    name = l[0:l.index(",")]    #removing unnecessary parts
    names.append(name)
#print(names)
def identitycreation(repeat = 1):    #function because of flexability
    credentials= open("credentials.txt","w")    #Save to a file instead of printing to screen
    for r in range(repeat):
        firstname = str(numpy.random.choice(names))     #randomly choosing names
        surname = str(numpy.random.choice(names))

        print(str(r+1)+"-"+firstname,surname,file=credentials)   
        email = f"{firstname}.{surname}@gmail.com".lower()
        phonenum = []
        for i in range(0,12):   #Generating phone number
            phonenum.append(numpy.random.randint(0,10))
        pnum = "+"
        for i in phonenum:
            pnum += str(i)
        print(email+"\n"+pnum+"\n\n",file=credentials)

repeat= input("How many credential do you want?\n>>")

identitycreation(int(repeat))
