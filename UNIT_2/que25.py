# Write a Python program to find the greater one of two integer numbers using lambda
# function, conditional operator and default argument.

# greater = lambda a, b : a if a > b else b
# print(greater(5, 8))


a, b = 10, 20

greater_condition = a if a > b else b

print(greater_condition)
