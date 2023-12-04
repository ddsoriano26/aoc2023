import re

# Get the card details of each card.
def parse_card(card):
    card_number = int(re.findall(r'\d+', re.findall(r'\d+:', card)[0])[0])
    numbers = card.replace(f"Card {card_number}:", "").split("|")
    winning_numbers_string = numbers[0][1:-1].split(" ")
    my_numbers_string = numbers[1][1:].strip('\n').split(" ")

    # Convert items in arrays from string to int
    winning_numbers = []
    for number in winning_numbers_string:
        if len(number) > 0:
            try:
                winning_numbers.append(int(number))
            except:
                pass
    my_numbers = []
    for number in my_numbers_string:
        if len(number) > 0:
            try:
                my_numbers.append(int(number))
            except:
                pass
    
    return card_number, winning_numbers, my_numbers

# Count the number of matches given the numbers.
def count_matches(winning_numbers, my_numbers):
    items = 0
    for number in my_numbers:
        if (number > 0) and (number in winning_numbers):
            items += 1
    return items

# Get number of points given the numbers
def get_points(items):
    return 2**(items-1) if items > 0 else 0

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()
    sum = 0

    # Initial number of copies per card
    copies = dict(zip([i for i in range(1, len(lines) + 1)], [1] * len(lines)))
    
    i = 0
    for line in lines:
        card_number, winning_numbers, my_numbers = parse_card(line)
        matches = count_matches(winning_numbers, my_numbers)
        points = get_points(matches)
        sum += points

        # Update number of copies per card
        for copy in range(0, copies[card_number]):
            for idx in range(1, matches + 1):
                copies[card_number + idx] += 1

    print(f"Total Points: {sum}")
    
    sum = 0
    for value in list(copies.values()):
        sum += value
    print(f"Total Scratchcards: {sum}")