from enum import Enum


class Color(Enum):
    IS_WALL = [0, 0, 0, 1]
    IS_NOT_WALL = [0.9, 0.9, 0.9, 1]
    IS_HOVERED = [0.8, 0.8, 0.8, 1]
    IS_START = [0, 1, 0, 1]
    IS_END = [1, 0, 0, 1]


if __name__ == "__main__":
    print(Color.IS_NOT_WALL.value)
