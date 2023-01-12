# Write a Python program to find whether year entered by the user is leap year or not and
# display the appropriate message.

def checkLeapYear(year):
    if ((year % 400 == 0) or
       (year % 100 != 0) and
       (year % 4 == 0)):
        print("Given Year is a leap Year")
    else:
        print("Given Year is not a leap Year")


year = int(input("Enter the number: "))
checkLeapYear(year)
