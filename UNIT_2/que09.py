# Write a Python program that demonstrate the use of variable length argument.

def variableLength_Argument(*variableArgument):
    for i in variableArgument:
        print(i)


variableLength_Argument(1, 2, 3, 4)
