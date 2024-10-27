
# 1 . User will input (3ages).Find the oldest one

num1 = input("enter num")
num2 = input("enter num")
num3 = input("enter num")

maxi = num1

if maxi < num2:
    maxi = num2
if maxi < num3:
    maxi = num3
print(maxi)


# 2 . Write a program that will convert Celsius value to Fahrenheit

temp = float(input("Enter temperature: "))
Fahrenheit = (temp * 1.8) + 32

print(Fahrenheit)
