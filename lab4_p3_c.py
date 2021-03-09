
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


