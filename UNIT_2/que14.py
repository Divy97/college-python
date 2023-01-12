# Write a Python program that will ask the user to input a three digit number and make
# sum of that and display the sum.

number = int(input("Enter 3 digit number: "))


def sumOfDigits(number):
    add = 0
    while (number > 0):
        rem = int(number % 10)
        add = add + rem
        number = number/10
    return add


def reverse(number):
    reversed_num = 0
    while number != 0:
        rem = number % 10
        reversed_num = reversed_num * 10 + rem
        number = number // 10
    print("Reversed Number: " + str(reversed_num))


print("Sum of digits is:", sumOfDigits(number))
reverse(number)
