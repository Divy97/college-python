# Write a Python program that will find square and cube of a number using function. Use
# keyword argument.

def cube(number):
    print("Cube of number is", number*number*number)


number = int(input("Enter number: "))
cube(number=number)
