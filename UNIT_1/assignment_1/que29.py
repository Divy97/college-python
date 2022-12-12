# 29. Write a program to accept a filename from the user print the extension of that.

fileName = input("Enter a file name: ")

fileExtension = fileName.split(".")
print("Extension of a given file is:", fileExtension[-1])
