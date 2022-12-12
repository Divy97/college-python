# 30. Write a program to convert the temperature from degree centigrade to Fahrenheit.[C = ((F32)*5)/9]

temperatureInCentigrade = float(
    input("Enter temperature in degree centigrade: "))
centigradeToFahrenheit = (temperatureInCentigrade * 1.8) + 32

print("Temperature in Fahrenheit: ", centigradeToFahrenheit, "F")
