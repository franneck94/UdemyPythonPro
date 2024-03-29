from logging import Logger
from typing import Generic
from typing import TypeVar


T = TypeVar("T")


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log("Set " + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log("Get " + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info("%s: %s", self.name, message)


def main() -> None:
    lv1 = LoggedVar(1, "Jan", Logger("a"))  # noqa
    lv2 = LoggedVar(1.0, "Jan", Logger("b"))  # noqa


if __name__ == "__main__":
    main()
