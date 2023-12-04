import re

def get_numbers(previous, current, next):
    numbers_in_line = re.findall(r'\d+', current)
    # print(numbers_in_line)
    numbers_to_remove = []
    remove_indices = []
    numbers_to_add = []

    idx = 0
    # print(f"previous line:\t{previous}")
    # print(f"current line:\t{current}")
    # print(f"next line:\t{next}")
    if len(numbers_in_line) != len(set(numbers_in_line)):
        print(f"Multiple occurences: {current}")
        print(numbers_in_line)
        print(set(numbers_in_line))
        print(f"previous line:\t{previous}")
        print(f"current line:\t{current}")
        print(f"next line:\t{next}")
    for number in numbers_in_line:
    # for x in range(0, len(numbers_to_remove)):
        # number = numbers_to_remove[x]
        match_object = re.search(number, current[idx:])
        # print(current[idx:])
        # print(number)
        indices = match_object.span()
        # print(f"start:\t{idx + indices[0]}")
        # print(f"end:\t{idx + indices[1]}")

        start_index = max(idx + indices[0], 1) - 1
        end_index = min(idx + indices[1] + 1, len(current))
        special_chars = ""

        if previous:
            prev_line = previous[start_index:end_index]
            # print(f"previous:\t{prev_line}")
            # print(f"{prev_line.strip(r'.').strip(r'[0-9]+')}")
            stripped_prev = "".join([char for char in prev_line if not char.isdigit()]).strip(r'.')
            special_chars += stripped_prev

        curr_line = current[start_index:end_index]
        # print(f"current:\t{curr_line}")
        # stripped = curr_line.strip(r'.')
        # stripped = re.findall(r'\d+', stripped)
        stripped = "".join([char for char in curr_line if not char.isdigit()]).strip(r'.')
        # stripped = "".join([char for char in stripped if not char == '.'])
        special_chars += stripped
        # print(f"stripped: {stripped}")

        if next:
            next_line = next[start_index:end_index]
            # print(f"next:\t\t{next_line}")
            stripped_next = "".join([char for char in next_line if not char.isdigit()]).strip(r'.')
            special_chars += stripped_next

        # print(f"NUMBER: {number}")
        if len(special_chars) == 0:
            numbers_to_remove.append(number)
            # print(f"DO NOT INCLUDE IN SUM")
            # remove_indices.append(x)
            # print(f"No special chars for {number}")
            # print(numbers_to_remove)
        else:
            # print(f"special chars: {special_chars}")
            # print(f"INCLUDE IN SUM")
            numbers_to_add.append(int(number))
            # print(f"Number: {int(number)}")

        idx += indices[1]
    
    return numbers_to_remove
    # return len(numbers_in_line), remove_indices
    # return numbers_to_add


if __name__ == "__main__":
    FILE_NAME = "input.txt"
    # FILE_NAME = "sample.txt"
    # FILE_NAME = "input-trunc.txt"

    input_file = open(FILE_NAME, "r")
    # input_file = open(SAMPLE, "r")
    all = input_file.read()
    # print(all)
    input_file.close()
    # print(all)
    input_file = open(FILE_NAME, "r")
    # input_file = open(SAMPLE, "r")
    lines = input_file.readlines()
    all_numbers = re.findall(r'\d+', all)
    all_num_length = len(all_numbers)

    total = 0
    for i in range(0, len(lines)):
        index = 0
        if i == 0:
            # remove_numbers = get_numbers(None, lines[i], lines[i+1])
            remove_numbers = get_numbers(None, lines[i], lines[i+1])
        elif i == len(lines) - 1:
            remove_numbers = get_numbers(lines[i-1], lines[i], None)
        else:
            remove_numbers = get_numbers(lines[i-1], lines[i], lines[i+1])

        # if len(remove_numbers) > 0:
        #     print(f"numbers to remove: {remove_numbers}")

        for number in remove_numbers:
            all_numbers.remove(number)
            # total += number
        
    # print(all_numbers)
    new_numbers = [eval(num) for num in all_numbers]
    # print(new_numbers)
    # print(sum(new_numbers))

    sum = 0
    for num in all_numbers:
        # print(sum)
        sum += int(num)
    print(f"Initial computed sum: {sum}")
    # print(all_num_length)
    # print(len(new_numbers))

    print(f"Total = {total}")