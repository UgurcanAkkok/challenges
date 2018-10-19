#!/usr/bin/python
maxn = int(input("Which number shall be the highest?"))
fbnums = [] 

for i in range(1,maxn + 1):
    if i % 15 == 0:
        fbnums.append("fizzbuzz")
    elif i % 3 == 0:
        fbnums.append("fizz")
    elif i % 5 == 0:
        fbnums.append("buzz")
    else:
        fbnums.append(i)
resoults = ""
for i in fbnums:
    resoults += str(i) + " "

print(resoults)

    
