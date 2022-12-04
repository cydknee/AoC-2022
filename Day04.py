""" AoC 2022 Day 4: Camp Cleanup """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in file.read().splitlines()]


def create_area(area):
    area_sections = []
    for i in range(area[0], area[1]+1, 1):
        area_sections.append(i)
    return area_sections


def check_fully_contained_area(areas):
    area_one, area_two = set(create_area(areas[0])), set(create_area(areas[1]))
    if area_one.issubset(area_two) or area_one.issuperset(area_two):
        return 1
    return 0


def check_partially_contained_area(areas):
    area_one, area_two = set(create_area(areas[0])), set(create_area(areas[1]))
    if area_one.isdisjoint(area_two):
        return 0
    return 1


def part1():
    assignment_pairs = 0
    for area_pair in read_file():
        assignment_pairs += check_fully_contained_area(area_pair)
    return assignment_pairs


def part2():
    assignment_pairs = 0
    for area_pair in read_file():
        assignment_pairs += check_partially_contained_area(area_pair)
    return assignment_pairs


if __name__ == '__main__':
    print(part1())
    print(part2())
