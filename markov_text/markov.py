#!/usr/bin/python
import random 
textfile = open("readytext.txt","r")
results = open("results.txt",mode="w") 
text = textfile.read()
words = text.split(" ") 
words.append(".")
wdict = dict()
counter = 100
#print(type(text))
#print(words)
fin_words = []
for word in words:
    if ("." in word) or( "?" in word):
        fin_words.append(word)
    wtor = []
    for i in range(words.count(word)):
        c = words.index(word)
        wtor.extend(words[c+1])
        wtor.extend(words[c+2])

        words.remove(word) 
    wdict[word] = wtor  
print(wdict)
#print(fin_words) 
keys = [k for k in wdict.keys()]
r_key = random.choice(keys)
print(r_key.capitalize() ,file=results)
#print(wdict["lovely"])
while counter > 0: 
    try:
        nextw = random.choice(wdict[r_key])
    except IndexError:
        continue
    if r_key in fin_words:
        print(nextw.capitalize(),file=results,end=" ")
    else:
        print(nextw ,file=results,end=" ")
    r_key = nextw
    counter -= 1
textfile.close()
results.close()
        
