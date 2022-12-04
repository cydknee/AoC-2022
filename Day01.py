""" AoC 2022 Day 1: Calorie Counting """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [sum([int(y) for y in x.splitlines()]) for x in file.read().split("\n\n")]


def part1():
    return max(read_file())


def part2():
    return sum(sorted(read_file())[-3:])


if __name__ == '__main__':
    print(part1())
    print(part2())
