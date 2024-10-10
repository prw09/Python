import logging

# Set up logging with a simpler format
logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger()


# Login and Indentation
# user is asked for email and password

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == 'piyush@gmail.com' and password == 'Piyush@1234':
    logger.info("Welcome to the webpage!")

elif email == "piyush@gmail.com" and password != 'Piyush@1234':
    logger.info("Your entered a incorrect password!")
    password = input("Enter password")

    if password != 'Piyush@1234':
        logger.info("Your entered a incorrect password!")
    else:
        logger.info("Welcome to the webpage!")

else:
    logger.info("please correct your email or password!")


# Better version

# Get email and password input
email = input("Enter your email: ")
password = input("Enter your password: ")

# Define correct email and password
correct_email = 'piyush@gmail.com'
correct_password = 'Piyush@1234'

# Authentication logic
if email == correct_email and password == correct_password:
    logger.info("Welcome to the webpage!")

elif email == correct_email and password != correct_password:
    logger.info("You entered an incorrect password!")
    password = input("Enter password: ")

    if password == correct_password:
        logger.info("Welcome to the webpage!")
    else:
        logger.info("You entered an incorrect password again!")

else:
    logger.info("Please correct your email or password!")
