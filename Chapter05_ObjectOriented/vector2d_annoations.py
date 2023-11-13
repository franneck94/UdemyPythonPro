"""Own implementation of a 2D vector class.
"""
from __future__ import annotations

from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float value for x and y!")

    def __call__(self) -> None:
        print("Calling the __call__ method!")

    def __repr__(self) -> str:
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __abs__(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, other_vector: object) -> bool:
        if not isinstance(other_vector, Vector2D):
            return False
        return self.x == other_vector.x and self.y == other_vector.y

    def __lt__(self, other_vector: Vector2D) -> bool:
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        return abs(self) < abs(other_vector)

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other: Vector2D | float) -> float | Vector2D:
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        if not isinstance(other, float):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> Vector2D:
        if not isinstance(other, float):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x / other, self.y / other)


def main() -> None:
    # v1 = Vector2D(1.0, 1.0)
    # v1 / "2"
    pass


if __name__ == "__main__":
    main()
