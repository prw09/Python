from loguru import logger

logger.info("hello")

# Arithmetic operators

logger.info(5 + 6)

logger.info(5 - 6)

logger.info(5 * 6)

logger.info(5 / 2)

logger.info(5 // 2)

logger.info(5 % 2)

logger.info(5 ** 2)

# Relational operators

logger.info(5 > 6)

logger.info(5 < 6)

logger.info(5 == 6)

logger.info(5 != 6)

# Logical operators

logger.info(1 and 0)

logger.info(1 or 0)

logger.info(not 0)

logger.info(not 1)

# Bitwise operators

logger.info(2 & 3)

logger.info(2 | 3)

logger.info(3 ^ 3)  # If same then it is 0

logger.info(3 ^ 2)  # if different then it is 1

logger.info(~3)

logger.info(~3)

# assignment operator

a = 2  # here = is an assignment operator

a %= 2

# membership operator

logger.info("f" in "DELHI")

# problem 01
# find the sum of 3 digits numbers entered by the user

num = int(input("Enter the 3-digits number"))

a = num % 10

num = num // 10

b = num % 10

num = num // 10

c = num % 10

num = num // 10

d = a, b, c

logger.info(f"The number is {d}")


def sum_of_digits():
    try:
        # Take input from the user and validate it's a three-digit number
        num = int(input("Enter a 3-digit number: "))
        if 100 <= num <= 999:
            # Extract each digit using modulus and integer division
            a = num % 10
            b = (num // 10) % 10
            c = (num // 100) % 10

            # Calculate the sum of the digits
            digit_sum = a + b + c

            # Print the digits and their sum
            print(f"The digits are: {c}, {b}, {a}")
            print(f"The sum of the digits is: {digit_sum}")
        else:
            print("Please enter a valid 3-digit number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


# Call the function
sum_of_digits()
