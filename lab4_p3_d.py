# -*- coding: utf-8 -*-
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