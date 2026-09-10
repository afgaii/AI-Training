import logger


logger.logger.info("Starting the calculation module.")
def add(a: int, b: int) -> int:
    """add two numbers together"""
    return a + b


def sub(a: int, b: int) -> int:
    """subtract two numbers"""
    return a - b

logger.logger.info("Calculation module is ready.")