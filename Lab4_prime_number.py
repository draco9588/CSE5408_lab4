# Cameron Wood Lab 4 Prime number

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