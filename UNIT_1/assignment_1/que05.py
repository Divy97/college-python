# Create a Python program that will have one list with values = ['Navratri’, ‘Diwali’,
# ‘Holi’, ‘Rakshabandhan’,’Bakri Id’, ‘Muharram’ ]. Perform following operations:
# • Print whole list
# • Print only first element of list
# • Prints elements starting from 2nd till 3rd
# • Prints elements starting from 2nd element till last
# • Print whole list 4 times using appropriate operator

festivalList = ['Navratri', 'Diwali', 'Holi',
                'Rakshabandhan', 'Bakri Id', 'Muharram']

print("LIST: ", festivalList)
print("First element is ", festivalList[0])
print("element from 2nd till 3rd", festivalList[2:4])
print("element from 2nd till last", festivalList[2:])
print("List 4 times ", festivalList*4)
