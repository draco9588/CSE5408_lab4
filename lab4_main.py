"""
CSU San Bernardino
CSE 5408 Spring 2021
Lab 04 Version Control System GitHub-advance 
Group 1
Cameron Wood: p1, p2 
Ricardo Torres: p3, p4
Pablo Fernando: p5
"""

#Cameron Wood Lab 4 string reverse

str1 = str(input("Enter a word or statement: "))
print(str1, ": (Forwards)")
str2 = str1 [::-1]
print(str2, " (Reverse)")


prime = int(input("Enter a positive number: "))

if prime > 1:
    for j in range(2,prime):
        if (prime % j) == 0:
            print(prime, ": is not a prime number.")
            break
    else:
        print(prime, ": is a prime number.")
else:
    print(prime, ": is a prime number.")
    # -*- coding: utf-8 -*-

"""
Created on Tue Mar  7 11:55:27 2021
CSE 5408 lab 4 problem 3 section c
convert 12 hour to 24 hour time
First a time in 12 hour will be initialized and saved 
then converted to 24 hour time.
@author: rjtor
"""

def get_time():
    from time import localtime
    timeInTwelve = localtime()
    return timeInTwelve

def convert_time(givenTime): 
    from time import strftime
    result = strftime(" %H:%M:%S", givenTime )
    print(result)


print("print time in 12 hour mode.")
xTime = get_time()
print(xTime)

print("print time in 24 hour mode.")
convert_time(xTime)
"""
Created on Tue Mar  9 12:50:00 2021
CSE 5408 lab 4 problem 3 section d
This is to calculate the fibonacci sum with the given user input
To calculate sum formula will find all fibonacci numbers then add them up
There are more cost effective ways but this way was simplist to understand
@author: rjtor
"""

def cal_sum(num) : 
    if (num <= 0) : 
        return 0
   
    fibNum =[0] * (num+1) 
    fibNum[1] = 1
   
    # Initialize result 
    sm = fibNum[0] + fibNum[1] 
   
    # Add remaining terms 
    for i in range(2,num+1) : 
        fibNum[i] = fibNum[i-1] + fibNum[i-2] 
        sm = sm + fibNum[i] 
          
    return sm 

#test

print("Fibonacci sum calculator:")
user_input = int(input("Enter the number you wished sumed: "))
result = (cal_sum(user_input))
print("Here is the result:")
print(result)

#pablo
import re
p= input("Enter your password")
x = True
while x:
    if (len(p)<7):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[!@#$%^&*]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("The password is secure.")
        x=False
        break

if x:
    print("Password is not secure, please try again.")
