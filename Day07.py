""" AoC 2022 Day 7: No Space Left On Device """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [x.split(" ") for x in file.read().splitlines()]


def calculate_folder_sizes(commands):
    dir_stack = []
    finished_directories = []
    for command in commands:
        if command[0] == "$" and command[1] == "cd" and command[2] != "..":
            dir_stack.append([command[2], 0])
        elif command[0] == "$" and command[1] == "cd" and command[2] == "..":
            finished_directories.append(dir_stack.pop())
        elif command[0].isnumeric():
            for directory in dir_stack:
                directory[1] += int(command[0])
    finished_directories.extend(dir_stack)
    return finished_directories


def directories_less_than_100k(folder_sizes):
    total = 0
    for folder in folder_sizes:
        if folder[1] < 100000:
            total += folder[1]
    return total


def free_space_needed(folder_sizes):
    folder_sizes.sort(key=lambda x: x[1], reverse=True)
    largest_folder = int(folder_sizes[0][1])
    return 30000000 - (70000000 - largest_folder)


def find_directory_large_enough_to_delete(folder_sizes, space_needed):
    for i in range(0, len(folder_sizes)):
        if folder_sizes[i][1] >= space_needed > folder_sizes[i + 1][1]:
            return folder_sizes[i]


def part1():
    folder_sizes = calculate_folder_sizes(read_file())
    return directories_less_than_100k(folder_sizes)


def part2():
    folder_sizes = calculate_folder_sizes(read_file())
    space_needed = free_space_needed(folder_sizes)
    folder_to_delete = find_directory_large_enough_to_delete(folder_sizes, space_needed)
    return folder_to_delete[1]


if __name__ == '__main__':
    print(part1())
    print(part2())
