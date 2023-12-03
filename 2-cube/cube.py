import re

FILE_NAME = "input.txt"
SAMPLE = "sample.txt"
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Parse per color.
def get_color_array(sets, color):
    pattern = r'\d+ ' + color
    color_array = re.findall(pattern, sets)
    return color_array

# Check if the sets of a color are greater than max for that color.
def check_max(sets, color, max):
    color_array = get_color_array(sets, color)
    for set in color_array:
        num = re.findall(r'\d+', set)
        num = int(num[0])
        if num > max:
            return True
    return False

# Get the maximum number of cubes in a color per game.
def get_max(color_array):
    number_array = []
    for color in color_array:
        number = re.findall(r'\d+', color)
        number_array.append(int(number[0]))
    return max(number_array)

if __name__ == "__main__":
    input_file = open(FILE_NAME, "r")
    # input_file = open(SAMPLE, "r")
    lines = input_file.readlines()
    sum = 0
    for line in lines:
        game_number = int(re.findall(r'\d+', re.findall(r'\d+:', line)[0])[0])
        if check_max(line, "red", MAX_RED):
            continue
        if check_max(line, "blue", MAX_BLUE):
            continue
        if check_max(line, "green", MAX_GREEN):
            continue
        sum += game_number
    print(f"Part One: {sum}")

    sum_power = 0
    for line in lines:
        power = 1
        for color in ["red", "blue", "green"]:
            color_array = get_color_array(line, color)
            power *= get_max(color_array)
        sum_power += power
    print(f"Part Two: {sum_power}")