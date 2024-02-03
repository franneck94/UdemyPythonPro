import logging
from pathlib import Path


# Mode: DEBUG: Detailed debug information
# Mode: INFO: Things working as intended
# Mode: WARNING: Something unexpected happened
# Mode: ERROR: The software cannot perform some function
# Mode: CRITICAL: Program crashes for example

# Setup the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Formatter, FileHandler
formatter = logging.Formatter(
    "%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"
)
filepath = Path(__file__).parent.joinpath("log_standard.log")
file_handler = logging.FileHandler(filepath)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def divide_integers(a: int, b: int) -> None | float:
    try:
        logger.info(f"a={a}, b={b}")  # noqa: G004
        result = a / b
        return result  # noqa: RET504, TRY300
    except ZeroDivisionError as e:
        logger.exception(f"Exception was raised: {e}")  # noqa: G004, TRY401
        return None


def main() -> None:
    for _ in range(3):
        print(divide_integers(10, 0))


if __name__ == "__main__":
    main()
