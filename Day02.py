""" AoC 2022 Day 2: Rock Paper Scissors """

FILE_NAME = "Input.txt"
ROCK_PAPER_SCISSORS = LOSE_DRAW_WIN = "XYZ"
ELF_ROCK_PAPER_SCISSORS = "ABC"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [x.split(" ") for x in file.read().splitlines()]


def score_move(move):
    return ROCK_PAPER_SCISSORS.index(move) + 1


def find_winner(move):
    my_move = ROCK_PAPER_SCISSORS.index(move[1])
    elf_move = ELF_ROCK_PAPER_SCISSORS.index(move[0])
    outcome = (my_move - elf_move + 1) % 3
    return outcome * 3


def calculate_which_move(current_move):
    outcome = LOSE_DRAW_WIN.index(current_move[1])
    elf_move = ELF_ROCK_PAPER_SCISSORS.index(current_move[0])
    my_move = (elf_move + outcome - 1) % 3
    return ROCK_PAPER_SCISSORS[my_move]


def part1():
    current_score = 0
    for move in read_file():
        current_score += score_move(move[1])
        current_score += find_winner(move)
    return current_score


def part2():
    current_score = 0
    for move in read_file():
        my_move = calculate_which_move(move)
        current_score += score_move(my_move)
        current_score += find_winner([move[0], my_move])
    return current_score


if __name__ == '__main__':
    print(part1())
    print(part2())
