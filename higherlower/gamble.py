#!/usr/bin/python
import numpy.random as nmr
print("Welcome to Higher Lower Gambling game! ",flush=True)
score = 0
cur_num = nmr.randint(0,11)
print("Your score is",score)
print(cur_num)
while True:  
    guess = input("\n"+"High or Low(h/l|q)?\n>>")
    next_num = nmr.randint(0,11)
    while next_num == cur_num:    
        next_num = nmr.randint(0,11)
    if cur_num < next_num :
        answer = "h"
    elif cur_num > next_num:
        answer = "l"
    if guess.lower() == "q":
        print("Your score is",score)
        break
    elif guess.lower() == answer:
        print(next_num,"\nWow! You guessed it right.")
        score +=1 
        print("Your score is",score)
        cur_num = next_num
        continue
    else:
        print(next_num,"\nNot a lucky day my friend.")
        score -=2
        print("Your score is",score)
        cur_num = next_num
        continue
