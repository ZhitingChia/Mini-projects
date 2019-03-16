# Pi Calculator v1.1
# Author: Chia Zhi Ting
# Guided by: Black Dog i-Tech Series vol.37
# Created: 14/03/2019

# This program calculates pi with the flexibility of setting the precision.
# It is dependent on the Chudnovsky Algorithm
# Something to commemorate pi-day

# You may try calculating pi to 1000 decimal places
# but beware of having your computer being locked up in calculating Pi
# if you go too high.

from decimal import Decimal, getcontext
import math
import time
import colorama

from colorama import Fore
colorama.init()

numDigits = int(input("Enter amount of decimal places to calculate Pi to "))
getcontext().prec= numDigits

start =time.time()

def computePi(n):
    #initialise t,pi, deno(denominator) and k
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    c = 640320


    for k in range(n):
        t = Decimal(-1)**k *(math.factorial(Decimal(6)*k))
        t *= 13591409 + 54510134*k
        deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))
        deno *= c**(3*k)
        pi += Decimal(t)/Decimal(deno)
        
    pi*= Decimal(12)/Decimal(c**Decimal(1.5))
    pi=1/pi
    return str(pi)
    

print(computePi(1))
timeTaken = time.time()-start
msg = '\nTime taken: '+ str(timeTaken)
print(Fore.RED, msg, end = '')
print (Fore.RED, 'seconds')











