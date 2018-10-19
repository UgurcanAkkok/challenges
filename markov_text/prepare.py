#!/usr/bin/python
transcript = open("transcript.txt",mode="r")
ts_lines = transcript.readlines() 
ready_text = open("readytext.txt",mode="w")
for l in ts_lines:
    if "[" in l:
        l = "\n"
    l = l.replace(")","").replace("(","").replace("\n","")
    words = l.split(" ")
    for w in words :
        if w.isupper() or "[" in w:
            pass
        else:
            print(w,file=ready_text,end=" ")
transcript.close()
ready_text.close()

