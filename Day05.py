""" AoC 2022 Day 5: Supply Stacks """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        crates, moves = file.read().split("\n\n")
    return crates, moves


def put_crates_in_stacks(crates):
    crate_stacks = [[x for x in i] for i in crates.splitlines()]
    total_number_of_stacks = int((max([len(i) for i in crate_stacks]) + 1) / 4)
    stacks = [[] for _ in range(total_number_of_stacks)]

    for stack in crate_stacks[:-1]:
        for crate in range(0, len(stack)):
            if stack[crate].isalpha():
                stack_number = int((crate - 1) / 4)
                stacks[stack_number].insert(0, stack[crate])
    return stacks


def remove_text_from_move_list(moves):
    return [[int(y.replace("move", "").replace(" ", "")) for x in z.split("to") for y in x.split("from")] for z in moves.splitlines()]


def crate_mover(crates, moves, is_crate_mover_9001):
    for move in moves:
        number_of_crates, original_stack, new_stack = move
        crates_to_move = []

        for i in range(0, number_of_crates):
            crates_to_move.append(crates[original_stack - 1].pop())

        if is_crate_mover_9001: crates_to_move.reverse()
        crates[new_stack - 1].extend(crates_to_move)
    return crates


def top_of_each_stack(crates):
    return "".join([crate[-1] for crate in crates])


def part1_and_part2(is_crate_mover_9001):
    crates, moves = read_file()
    crates = put_crates_in_stacks(crates)
    moves = remove_text_from_move_list(moves)
    crates = crate_mover(crates, moves, is_crate_mover_9001)
    return top_of_each_stack(crates)


if __name__ == '__main__':
    print(part1_and_part2(False))
    print(part1_and_part2(True))
