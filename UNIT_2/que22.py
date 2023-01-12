# Write a Python program that will ask the user to input a 3 digit number and reverse it.

def reverse(number):
    reversed_num = 0
    while number != 0:
        rem = number % 10
        reversed_num = reversed_num * 10 + rem
        number = number // 10
    print("Reversed Number: " + str(reversed_num))


reverse(321)
