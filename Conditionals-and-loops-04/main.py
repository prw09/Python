import logging
import math
import keyword
import datetime


# # Set up logging with a simpler format
# logging.basicConfig(format='%(message)s', level=logging.INFO)
# logger = logging.getLogger()
#
# # Login and Indentation
# # user is asked for email and password
#
# email = input("Enter your email: ")
# password = input("Enter your password: ")
#
# if email == 'piyush@gmail.com' and password == 'Piyush@1234':
#     logger.info("Welcome to the webpage!")
#
# elif email == "piyush@gmail.com" and password != 'Piyush@1234':
#     logger.info("Your entered a incorrect password!")
#     password = input("Enter password")
#
#     if password != 'Piyush@1234':
#         logger.info("Your entered a incorrect password!")
#     else:
#         logger.info("Welcome to the webpage!")
#
# else:
#     logger.info("please correct your email or password!")
#
#
# # Better version
#
# # Get email and password input
# email = input("Enter your email: ")
# password = input("Enter your password: ")
#
# # Define correct email and password
# correct_email = 'piyush@gmail.com'
# correct_password = 'Piyush@1234'
#
# # Authentication logic
# if email == correct_email and password == correct_password:
#     logger.info("Welcome to the webpage!")
#
# elif email == correct_email and password != correct_password:
#     logger.info("You entered an incorrect password!")
#     password = input("Enter password: ")
#
#     if password == correct_password:
#         logger.info("Welcome to the webpage!")
#     else:
#         logger.info("You entered an incorrect password again!")
#
# else:
#     logger.info("Please correct your email or password!")
#
#
# # Min of 3 numbers problem
#
# first_num = int(input("Enter 1st number"))
# second_num = int(input("Enter 2nd number"))
# third_num = int(input("Enter 3rd number"))
#
# if first_num < second_num and first_num < third_num:
#     logger.info(f"first_num is smallest number!, {first_num}")
#
# elif second_num < first_num and second_num < third_num:
#     logger.info(f"second_num is smallest number!, {second_num}")
#
# else:
#     logger.info(f"third_num is smallest number!, {third_num}")
#
#
# # Menu driven calculator
#
# fnum = int(input("Enter the first number"))
# snum = int(input("Enter the second number"))
#
# op = input("Enter the operations=")
#
# if op == '+':
#     print(fnum + snum)
# elif op == '-':
#     print(fnum - snum)
# elif op == '*':
#     print(fnum * snum)
# elif op == '/':
#     print(fnum / snum)
# else:
#     print("")
#
#
# print(math.factorial(5))
#
# print(keyword.kwlist)
#
# print(datetime.datetime.now())
#
# print(help('modules'))


# Loops

# # while loops
#
# n = int(input("enter number:"))
#
# i = 1
#
# while i < 11:
#     print(n*i)
#     i += 1
#
# # For loops
#
# for i in range(10):
#     print(i)
#
# for i in range(1, 20, 2):
#     print(i)
#
# # reverse numbers
# for i in range(10, 1, -1):
#     print(i)


# Problem solving

curr_pop = 10000

for i in range(10, 0, -1):
    print(curr_pop, i)
    curr_pop -= curr_pop/10




