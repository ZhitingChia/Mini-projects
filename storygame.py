#Story Game
#Author: Chia Zhi Ting
#Created on: 21/3/2019

import time

def menu():
    print("----------------------------------------------------------")
    print("The story game")
    print("----------------------------------------------------------")
    print("Welcome to the story game.")
    print("1. New game")
    print("2. Add to story")
    print("3. Read Story")
    print("4. Quit")

def write(sentence):
    s=open("story.txt",'a')
    s.write("{}\n".format(sentence))
    s.close()

def start():
    s=open("story.txt",'w')
    write("She was strong.\nShe was beautiful.\nBut humans were her only weakness.")        
    s.close()
    


def read():
    print("-----------------------------------------------------------")
    print("Story")
    print("-----------------------------------------------------------")
    s=open("story.txt")
    lines= s.readlines()

    for lines in lines:
        print(lines,end="")
        time.sleep(.5)
        
    s.close()

def run():
    choice='0'

    while choice != '4':
        menu()
        choice=input("Enter your choice: ")
        if choice=='1':
            start()
        elif choice =='2':
            sentence=input("Enter a sentence to add to the story: ")
            write(sentence)
        elif choice =='3':
            read()
        elif choice =='4':
            exit()
        else:
            print("Invalid input! Please enter your choice (1-4): ")


run()
            
