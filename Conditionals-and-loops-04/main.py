from loguru import logger

# Login and indentation
# user is asked for email and password

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == 'piyush@gmail.com' and password == 'Piyush@1234':
    logger.info("Welcome to the webpage!")

else:
    logger.info("please correct your email or password!")

