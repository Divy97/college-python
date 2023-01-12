# Write a Python program that will ask the user to input their name and age. Check
# whether a user is eligible to caste their vote or not.

age = int(input('Enter your age: '))


if age > 18:
    print("eligible to caste vote")
else:
    print("not eligible to caste vote")
