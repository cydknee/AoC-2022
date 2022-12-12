""" AoC 2022 Day 12: Hill Climbing Algorithm """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y for y in x] for x in file.read().splitlines()]


def find_start_and_end(grid):
    start_x, start_y, end_x, end_y = 0, 0, 0, 0
    for y_coord, row in enumerate(grid):
        for x_coord, letter in enumerate(row):
            if letter == "S":
                start_x = x_coord
                start_y = y_coord
                grid[y_coord][x_coord] = "a"
            elif letter == "E":
                end_x = x_coord
                end_y = y_coord
                grid[y_coord][x_coord] = "z"
    return [start_y, start_x], [end_y, end_x], grid


def breadth_first_search(grid, start, end):
    distance_to_start, distance_to_nearest_a = 0, 0
    found_nearest_a = False
    queue = [(0, end[0], end[1])]
    visited = {(end[0], end[1])}

    while queue:
        distance, y_coord, x_coord = queue.pop()
        for adjacent_y, adjacent_x in [(y_coord + 1, x_coord), (y_coord - 1, x_coord), (y_coord, x_coord + 1), (y_coord, x_coord - 1)]:
            if adjacent_y < 0 or adjacent_x < 0 or adjacent_y >= len(grid) or adjacent_x >= len(grid[0]):
                continue
            if (adjacent_y, adjacent_x) in visited:
                continue
            if ord(grid[adjacent_y][adjacent_x]) - ord(grid[y_coord][x_coord]) < -1:
                continue

            if adjacent_y == start[0] and adjacent_x == start[1]:
                distance_to_start = distance + 1
            if grid[adjacent_y][adjacent_x] == "a" and not found_nearest_a:
                distance_to_nearest_a = distance + 1
                found_nearest_a = True

            visited.add((adjacent_y, adjacent_x))
            queue.insert(0, (distance + 1, adjacent_y, adjacent_x))
    return distance_to_start, distance_to_nearest_a


def part1_and_part2():
    start, end, grid = find_start_and_end(read_file())
    distance = breadth_first_search(grid, start, end)
    return distance


if __name__ == '__main__':
    print(part1_and_part2()[0])
    print(part1_and_part2()[1])
