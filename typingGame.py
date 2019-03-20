#Simple Typing Speed test
# Author: Chia Zhi Ting
# Created on 20/3/2018

#The game selects a word from a list and the user has to type in the word.
#If the spelling is right, the number of passed rounds increases.
#Else the number of failed round will be incremented by one. 

import random
import time

words=["Trigometry","Asympotic","Linear","Gradient","Paramedics","Rabbit","Corsair","Tissue","Pomelo","Smartphones","Ambulance","Cryptography"]

print("Welcome to the typing game.")
print("---------------------------------------------")

stage=0
right=0
wrong=0
cont='0'

while cont != 'q':
    print("Stage {}".format(stage))
    
    index=random.randint(0,len(words)-1)
    print("Type the word ", words[index])
    start=time.time()
    userWord=input("Word: ")
    end= time.time()-start

    if userWord == words[index]:
        right=right+1
        print("Win!")
        
    else :
        wrong=wrong+1
        print("Lose!")
        
    stage=stage+1
    
    print("Time taken to answer: {0:.2f} seconds".format(end))
    print("Stage {} Rounds Passed: {}, Rounds Failed: {}".format(stage,right,wrong))
    
    cont= input("Enter q to quit and any other key to continue.")
    print("------------------------------------------------")
