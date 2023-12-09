import numpy as np

# Get the array that contains each difference until they are reduced to all 0s.
def get_diff_array(initial_array):
    diff_array = [initial_array]
    line = initial_array
    while True:
        diff = np.diff(line)
        
        # Stop when we've reduced to 0
        if not np.any(diff):
            break

        diff_array.append(list(diff))
        line = list(diff)
    return diff_array

# Predict the next number of the set of arrays.
def predict_set(number_array):
    previous_numbers = number_array[-1]
    for numbers in reversed(number_array[:-1]):
        last_number = numbers[-1]
        first_number = numbers[0]
        numbers.append(previous_numbers[-1] + last_number)
        numbers.insert(0, first_number - previous_numbers[0])
        previous_numbers = numbers
    return number_array[0][0], number_array[0][-1]

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    sum = 0
    sum_first = 0
    for line in lines:
        split_line = line.replace('\n', '').split(" ")
        numbers = [int(number) for number in split_line]
        diff_array = get_diff_array(numbers)
        extrapolated_first, extrapolated_last = predict_set(diff_array)
        sum += extrapolated_last
        sum_first += extrapolated_first
    print(f"Sum of extrapolated: {sum}")
    print(f"Sum of first values: {sum_first}")