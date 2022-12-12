""" AoC 2022 Day 10: Cathode-Ray Tube """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y for y in x.split(" ")] for x in file.read().splitlines()]


def check_interesting_cycles(cycles, x):
    if cycles in [20, 60, 100, 140, 180, 220]:
        signal = x * cycles
        return signal
    return 0


def execute_program(program):
    cycles = 1
    signal = 0
    x = 1
    for command in program:
        cycles += 1
        signal += check_interesting_cycles(cycles, x)
        if command[0] == 'addx':
            cycles += 1
            x += int(command[1])
            signal += check_interesting_cycles(cycles, x)
    return signal


def render_screen(program):
    cycles = 0
    sprite_position = 1
    crt = [[], [], [], [], [], []]
    for command in program:
        cycles += 1
        crt = draw_pixel(cycles, sprite_position, crt)
        if command[0] == 'addx':
            cycles += 1
            crt = draw_pixel(cycles, sprite_position, crt)
            sprite_position += int(command[1])
    for row in crt:
        print("".join(row))


def draw_pixel(cycles, sprite_position, crt):
    crt_row = (cycles-1) // 40
    current_crt_position = (cycles - 1) - (crt_row*40)
    if current_crt_position == sprite_position - 1 or current_crt_position == sprite_position or current_crt_position == sprite_position + 1:
        crt[crt_row].append("█")
    else:
        crt[crt_row].append(" ")
    return crt


def part1():
    return execute_program(read_file())


def part2():
    render_screen(read_file())


if __name__ == '__main__':
    print(part1())
    part2()

