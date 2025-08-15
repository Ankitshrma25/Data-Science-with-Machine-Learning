import logging

## Logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmenticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result


def Subtract(a,b):
    result=a-b
    logger.debug(f"Adding {a}-{b}={result}")
    return result


def multiply(a,b):
    result=a*b
    logger.debug(f"Adding {a}*{b}={result}")
    return result


def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Adding {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not possible")
        return None



add(10,12)
Subtract(19,2)
divide(2,2)