from pathlib import Path

from logging_extern import divide_integers
from loguru import logger  # https://github.com/Delgan/loguru


# Setup the logger
filepath = Path(__file__).parent.joinpath("log_loguru.log")
logger.add(filepath, rotation="1 Week")


def main():  # noqa: ANN201
    for _ in range(3):
        print(divide_integers(10, 0))


if __name__ == "__main__":
    main()
