# Write a Python program to find the sum of all numbers stored in a list.

list = []

length = int(input("Enter length of the list: "))
print("Enter values")
for i in range(0, length):
    element = int(input())
    list.append(element)


def addition(list):
    add = 0
    for i in list:
        add = add + i
    return add


print("Sum is:", addition(list))
