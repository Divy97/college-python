# Write a Python program that asks the user to input any five integer numbers and check
# whether number is odd number or even number and display the count of even and odd
# number

evenCount = 0
oddCount = 0
for i in range(0, 5):
    number = int(input("Enter 5 numbers: "))
    if number % 2 == 0:
        evenCount = evenCount + 1
    else:
        oddCount = oddCount + 1

print("Total Even number: ", evenCount)
print("Total Odd number: ", oddCount)
