""" AoC 2022 Day 9: Rope Bridge """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y for y in x.split(" ")] for x in file.read().splitlines()]


def move_rope(moves):
    knot_9_visited = []
    knot_1_visited = []
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    for move in moves:
        for _ in range(0, int(move[1])):
            match move[0]:
                case "R": rope[0][1] += 1
                case "L": rope[0][1] -= 1
                case "U": rope[0][0] -= 1
                case "D": rope[0][0] += 1
            for x in range(0, 9):
                rope[x + 1] = calc_move(rope[x], rope[x + 1])

            if rope[9] not in knot_9_visited:
                knot_9_visited.append(rope[9])
            if rope[1] not in knot_1_visited:
                knot_1_visited.append(rope[1])

    return len(knot_1_visited), len(knot_9_visited)


def calc_move(head, knot):
    new_move = knot.copy()
    x_diff = head[1] - knot[1]
    y_diff = head[0] - knot[0]

    if abs(y_diff) == 2 and x_diff == 0:
        new_move[0] = knot[0] + 1 if y_diff > 0 else knot[0] - 1
    elif y_diff == 0 and abs(x_diff) == 2:
        new_move[1] = knot[1] + 1 if x_diff > 0 else knot[1] - 1
    elif(abs(y_diff) == 2 and abs(x_diff) in [2, 1]) or (abs(y_diff) in [2, 1] and abs(x_diff) == 2):
        new_move[0] = knot[0] + 1 if y_diff > 0 else knot[0] - 1
        new_move[1] = knot[1] + 1 if x_diff > 0 else knot[1] - 1
    return new_move


def part1_and_part2():
    return move_rope(read_file())


if __name__ == '__main__':
    print(part1_and_part2()[0])
    print(part1_and_part2()[1])
