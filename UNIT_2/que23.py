# Write a Python program that will check whether number inputted is prime number or
# not.

def isPrime(number):
    if number == 1:
        print("not prime")
    elif number > 1:
        flag = False
        for i in range(2, number):
            if (number % i == 0):
                flag = True
                break
        if (flag == True):
            print("Not Prime")
        else:
            print("Prime")


number = int(input("enter a number: "))
isPrime(number)
