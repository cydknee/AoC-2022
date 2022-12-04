""" AoC 2022 Day 3: Rucksack Reorganization """

FILE_NAME = "Input.txt"
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [x for x in file.read().splitlines()]


def split_bag_into_compartments(bags):
    return [[bag[:len(bag)//2], bag[len(bag)//2:]] for bag in bags]


def compare_compartments(bag):
    compartment_one, compartment_two = bag
    rogue_items = []
    for item in compartment_one:
        if item in compartment_two and item not in rogue_items:
            rogue_items.append(item)
    return rogue_items


def compare_bags(bags):
    bag_one, bag_two, bag_three = bags
    for item in bag_one:
        if item in bag_two and item in bag_three:
            return item


def calculate_scores(rogue_items):
    score = 0
    for item in rogue_items:
        score += ALPHABET.index(item) + 1
    return score


def part1():
    incorrect_items = []
    bags = split_bag_into_compartments(read_file())
    for bag in bags:
        incorrect_items.extend(compare_compartments(bag))
    return calculate_scores(incorrect_items)


def part2():
    groups = []
    bags = read_file()
    for count in range(0, len(bags), 3):
        current_group = bags[count:count+3]
        groups.append(compare_bags(current_group))
    return calculate_scores(groups)


if __name__ == '__main__':
    print(part1())
    print(part2())
