#This program creates user logins and allows them to log into the system.
#The system will also display the time they logged in.

#Author: Chia Zhi Ting
#Version 1.0
#Created on: 27/3/2019
#Stores password as plaintext

import time

users={}
option=''

def mainMenu():
    global option
    option=input("Do you have a login account? (y/n/q)")
    if option=='y':
        login()
    elif option =='n':
        createUser()
    elif option =='q':
        print("Proceeding to quit.")
    else:
        print("Invalid input! Please enter y/n/q")

def run():
    global option
    while option != 'q':
        mainMenu()
    print ("Successfully quit.")

def createUser():
    uname=input("Enter a new login name: ")
    upass = input ("Enter new password: ")
    
    if(validateCreation(uname,upass)):
        writeAccount(uname,upass)
        print("Account {} successfully created!".format(uname))
    else:
        createUser()

   
          

def validateCreation(lname,lpass):
    if lname in users:
        print("Username {} already exists!".format(lname))
        return False
    else:
        return True

def writeAccount(lname,lpass):
    outfile= open("ac.txt",'a')
    outfile.write("{}:{}".format(lname,lpass))
    outfile.write("\n")
    outfile.close()

    
def login():
    readAccount()
    uname= input("Enter login name: ")
    upass=input("Enter password: ")

    if(validateLogin(uname,upass)):
        print("User {} logged in successfully at {}".format(uname,time.strftime("%H:%M")))
    else:
        option=input("Do you wish to quit? (y/n)")
        if option == 'y':
            option ='q'
        else:
            login()
        

def validateLogin(lname,lpass):
    if lname not in users:
        print("User {} does not exist!".format(lname))
        return False
    elif users[lname]==lpass:
        return True
    else:
        print("Wrong password!")


def readAccount():
    infile=open("ac.txt")

    for line in infile:
        lname,lpass= line.split(':')
        lpass=lpass.strip('\n')
        users[lname]=lpass
        
    infile.close()

    
    
run()
