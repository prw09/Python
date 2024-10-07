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