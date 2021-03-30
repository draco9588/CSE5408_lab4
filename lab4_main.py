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