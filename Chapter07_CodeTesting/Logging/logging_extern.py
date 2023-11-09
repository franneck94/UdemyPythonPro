from loguru import logger  # https://github.com/Delgan/loguru


@logger.catch
def divide_integers(a: int, b: int) -> float:
    logger.debug(f"a={a}, b={b}")
    try:
        result = a / b
        return result  # noqa: RET504
    except Exception as e:  # noqa: BLE001
        logger.log("DEBUG", str(e))
    return 0
