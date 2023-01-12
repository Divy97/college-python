# Write a Python program that will find greatest of three numbers using elif conditional
# statement.

num1 = int(input('Enter a Number1: '))
num2 = int(input('Enter a Number2: '))
num3 = int(input('Enter a Number3: '))

if num1 > num2 and num1 > num3:
    print("Number 1 is Greatest")
elif num2 > num1 and num2 > num3:
    print("Number 2 is Greatest")
else:
    print("Number 3 is Greatest")
