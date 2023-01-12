# Write a Python program that will calculate the Basic Salary of an employee where :
# HRA is 10% of Basic Salary
# DA is 20% of Basic Salary
# TA is 10% of Basic Salary
# PF is 20 % of Basic Salary
# Also calculate the net salary of the employee.

basic_salary = int(input("Enter basic salary: "))
HRA = (basic_salary * 10) / 100
DA = (basic_salary * 20) / 100
TA = (basic_salary * 10) / 100
PF = (basic_salary * 20) / 100

net_salary = (basic_salary + HRA + DA + TA - PF)
print("net salary is:", net_salary)
