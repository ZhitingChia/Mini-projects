# Simple calculator v1.2
# Author: Chia Zhi Ting
# Created on 13/3/2019

#This calculator program allows you to perform basic computations on two numbers
# as well as to convert a decimal number to its binary equivalent.

import math

def multiply(x,y):
    print(str(x)+" multiplied by "+str(y)+" is",end=' ')
    value=int(x)*int(y)
    print(str(value)+".")
    return value;

def getSqrt(x):
    print("The square root of "+ str(x)+" is",end=' ')
    value = math.sqrt(x)
    print(str(value)+".")

def subtract(x,y):
    print(str(y)+" deducted from "+str(x)+" results in",end=' ')
    value = x-y
    print(str(value)+'.')

def divide(x,y):
    print(str(x)+" divided by "+str(y)+ " is",end=' ')
    value=x/y
    print(str(value)+'.')

def add(x,y):
    print(str(x)+" added to "+str(y)+" is",end=' ')
    value=x+y
    print(str(value)+'.')

#This function calculates the binary equivalent  
def getBinary(x,y):
    print("The "+str(y)+"-bit binary equivalent of "+str(x)+" is ",end=' ')
    for i in range(y-1,-1,-1):
        #print(i)
        print((x>>i)&1,end='')
    print()

#A function to test the individual functions   
def test():
    multiply(3,4)
    getSqrt(169)
    subtract(21,14)
    divide(21,7)
    add(14,16)
    getBinary(231,8)
    getBinary(1,8)
    getBinary(10,8)
    getBinary(7,8)
    

def menu():
    print("Simple Calculator v 1.2")
    print("Designed by Zhiting")
    print("---------------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Square root")
    print("6. Get binary")
    print("9. Quit")
    option=input("Your option:")
    return option

def run():
    option=0
    while option!=9:
        option=int(menu())
        if option ==1:
            num1=input("Enter the first number:")
            num2=input("Enter the second number:")
            add(int(num1),int(num2))
            
        elif option==2:
            num1=input("Enter the first number:")
            num2=input("Enter the second number:")
            subtract(int(num1),int(num2))
            
        elif option==3:
            num1=input("Enter the first number:")
            num2=input("Enter the second number:")
            divide(int(num1),int(num2))
            
        elif option==4:
            num1=input("Enter the first number:")
            num2=input("Enter the second number:")
            multiply(int(num1),int(num2))
           
        elif option==5:
            num=input("Enter the number:")
            getSqrt(float(num))
            
        elif option==6:
            num=input("Enter the number to be converted to binary:")
            bits=input("Enter no. of bits:")
            getBinary(int(num),int(bits))
            
        elif option==9:
            print("Successfully quit simple calculator.")
            
        else:
                print("Invalid option")

        print()

#test()
run()
        

