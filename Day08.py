""" AoC 2022 Day 8: Treetop Tree House """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return file.read().splitlines()


def loop_through_trees(tree_map):
    highest_scenic_score = 0
    visible_tree_count = 0
    row_length = len(tree_map[0])
    for y in range(1, len(tree_map)-1):
        for x in range(1, row_length-1):
            current_tree = int(tree_map[y][x])
            visible_tree_count += check_tree_visible(int(current_tree), int(x), int(y), tree_map)
            viewing_distance = get_viewing_distance(int(current_tree), x, y, tree_map)
            scenic_score = calc_scenic_score(viewing_distance)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
    return visible_tree_count, highest_scenic_score


def check_tree_visible(current_tree, x_coord, y_coord, tree_map):
    if check_horizontal_visibility(current_tree, 0, x_coord, y_coord, tree_map) or \
            check_horizontal_visibility(current_tree, x_coord + 1, len(tree_map), y_coord, tree_map) or \
            check_vertical_visibility(current_tree, 0, y_coord, x_coord, tree_map) or \
            check_vertical_visibility(current_tree, y_coord + 1, len(tree_map), x_coord, tree_map):
        return True
    return False


def check_horizontal_visibility(current_tree, start_range, end_range, y_coord, tree_map):
    for current_position in range(start_range, end_range):
        if int(tree_map[y_coord][current_position]) >= current_tree:
            return False
    return True


def check_vertical_visibility(current_tree, start_range, end_range, x_coord, tree_map):
    for current_position in range(start_range, end_range):
        if int(tree_map[current_position][x_coord]) >= current_tree:
            return False
    return True


def count_edges(tree_map):
    x = len(tree_map[0])
    y = len(tree_map)
    return (x * 2) + ((y-2)*2)


def check_horizontal_viewing_distance(current_tree, y_coord, tree_map, range_start, range_end, step):
    viewing_distance = 0
    for current_position in range(range_start, range_end, step):
        if int(tree_map[y_coord][current_position]) < current_tree:
            viewing_distance += 1
        else:
            viewing_distance += 1
            return viewing_distance
    return viewing_distance


def check_vertical_viewing_distance(current_tree, x_coord, tree_map, range_start, range_end, step):
    viewing_distance = 0
    for current_position in range(range_start, range_end, step):
        if int(tree_map[current_position][x_coord]) < current_tree:
            viewing_distance += 1
        else:
            viewing_distance += 1
            return viewing_distance
    return viewing_distance


def get_viewing_distance(current_tree, x_coord, y_coord, tree_map):
    left = check_horizontal_viewing_distance(current_tree, y_coord, tree_map, x_coord-1, -1, -1)
    right = check_horizontal_viewing_distance(current_tree, y_coord, tree_map, x_coord+1, len(tree_map[0]), 1)
    above = check_vertical_viewing_distance(current_tree, x_coord, tree_map, y_coord-1, -1, -1)
    below = check_vertical_viewing_distance(current_tree, x_coord, tree_map, y_coord+1, len(tree_map), 1)
    return [above, below, left, right]


def calc_scenic_score(viewing_distance):
    scenic_score = viewing_distance[0] * viewing_distance[1] * viewing_distance[2] * viewing_distance[3]
    return scenic_score


def part1():
    tree_map = read_file()
    visible_central_trees = loop_through_trees(tree_map)[0]
    edges = count_edges(tree_map)
    return visible_central_trees + edges


def part2():
    scenic_score = loop_through_trees(read_file())[1]
    return scenic_score


if __name__ == '__main__':
    print(part1())
    print(part2())
