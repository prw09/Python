from loguru import logger

logger.info("hello")

# Arithmetic operators

logger.info(5+6)

logger.info(5-6)

logger.info(5*6)

logger.info(5/2)

logger.info(5//2)

logger.info(5 % 2)

logger.info(5**2)


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

