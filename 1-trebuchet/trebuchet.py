import re

# "Global" variables
FILE_NAME = "input.txt"
SAMPLE = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
SECOND_SAMPLE = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

# Convert word digits into number digits.
def convert_to_digits(input_string):
    conversion_dictionary = {
        "one": 1,
        "ONE": 1,
        "two": 2,
        "TWO": 2,
        "three": 3,
        "THREE": 3,
        "four": 4,
        "FOUR": 4,
        "five": 5,
        "FIVE": 5,
        "six": 6,
        "SIX": 6,
        "seven": 7,
        "SEVEN": 7,
        "eight": 8,
        "EIGHT": 8,
        "nine": 9,
        "NINE": 9,
        "zero": 0,
        "ZERO": 0,
    }
    new_string = input_string
    match_object = re.search(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)', new_string)
    digit_list = []
    i = 0
    while i < len(input_string):
        match_object = re.search(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)', input_string[i:])
        if input_string[i].isdigit():
            new_string += input_string[i]
            digit_list.append(input_string[i])
        else:
            match_object = re.search(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)', input_string[i:])
            if match_object != None:
                indices = match_object.span()
                digits = get_digits(input_string[i:indices[0]])
                # add digits to list
                digit_list += digits
                # convert word digit and add to list
                digit_match = match_object.group()
                digit_list.append(str(conversion_dictionary[digit_match]))
                # move index, i.e. skip other digits
                i += indices[0]
        i += 1
    return digit_list

# Extract digits of a string.
def get_digits(input_string):
    digit_array = list(filter(lambda x: x.isdigit(), input_string))
    return digit_array

# Get first and last items of a digit array and return as int.
def first_last(digit_list):
    return int(digit_list[0] + digit_list[-1])

if __name__ == "__main__":
    input_file = open(FILE_NAME, "r")
    lines = input_file.readlines()
    # lines = SECOND_SAMPLE
    sum = 0
    line_num = 0
    for line in lines:
        converted_string = convert_to_digits(line)
        sum += first_last(converted_string)
    print(sum)