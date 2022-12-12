""" AoC 2022 Day 11: Monkey in the Middle """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y.strip() for y in x.splitlines()] for x in file.read().split("\n\n")]


def create_monkey_dictionary(monkey_notes):
    monkey_list = []
    for note in monkey_notes:
        items = note[1].split(":")[1].strip()
        items = [int(x) for x in items.split(",")]
        monkeys = {
            "monkey": int(note[0].replace(":", "").split()[-1:][0]),
            "items": items,
            "operation": [note[2].split()[-2], note[2].split()[-1]],
            "test": int(note[3].split()[-1:][0]),
            "true": int(note[4].split()[-1:][0]),
            "false": int(note[5].split()[-1:][0]),
            "inspected": 0
        }
        monkey_list.insert(monkeys["monkey"], monkeys)
    return monkey_list


def monkey_turn(monkey_dict, lower_worry_levels):
    mod = find_mod(monkey_dict)
    for monkey in monkey_dict:
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            new_worry_level = inspect_item(item, monkey)
            if lower_worry_levels:
                new_worry_level = after_inspection(new_worry_level)
            new_worry_level %= mod
            test_result = test_worry_level(new_worry_level, monkey)
            monkey_dict = throw_item(test_result, new_worry_level, monkey, monkey_dict)

    return monkey_dict


def find_mod(monkey_dict):
    mod = 1
    for monkey in monkey_dict:
        mod *= monkey["test"]
    return mod


def inspect_item(item, monkey):
    operation = monkey["operation"][0]
    multiplier = monkey["operation"][1] if monkey["operation"][1].isnumeric() else item
    return eval(str(item) + operation + str(multiplier))


def after_inspection(worry_level):
    return worry_level // 3


def test_worry_level(worry_level, monkey):
    return True if worry_level % monkey["test"] == 0 else False


def throw_item(test_result, new_worry_item, monkey, monkey_dict):
    if test_result:
        monkey_dict[monkey["true"]]["items"].append(new_worry_item)
    else:
        monkey_dict[monkey["false"]]["items"].append(new_worry_item)
    monkey["inspected"] += 1
    return monkey_dict


def find_monkey_business(monkey_dict):
    monkey_business = []
    for monkey in monkey_dict:
        monkey_business.append(monkey["inspected"])
    monkey_business.sort()
    return monkey_business[-2] * monkey_business[-1]


def part1():
    monkey_dict = create_monkey_dictionary(read_file())
    for _ in range(0, 20):
        monkey_dict = monkey_turn(monkey_dict, True)
    most_inspected = find_monkey_business(monkey_dict)
    return most_inspected


def part2():
    monkey_dict = create_monkey_dictionary(read_file())
    for _ in range(0, 10000):
        monkey_dict = monkey_turn(monkey_dict, False)
    most_inspected = find_monkey_business(monkey_dict)
    return most_inspected


if __name__ == '__main__':
    print(part1())
    print(part2())
