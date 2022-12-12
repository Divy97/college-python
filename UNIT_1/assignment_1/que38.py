# 38. Write a program to display whether string has only digits or only alphabets.

stringValue = input('Enter a string: ')

if (stringValue.isdigit()):
    print("string has Only Digits")
elif (stringValue.isalpha()):
    print("string has Only Alpha")
else:
    print("string has BOTH")
