from itertools import permutations, combinations
import re
from dataclasses import dataclass, field

@dataclass
class Spring:
    arrangement: str
    criteria: list[int] = field(default_factory=list)

    def __str__(self) -> str:
        return f"Arrangement: {self.arrangement}\nCriteria: {self.criteria}\n"

springs = []

# This assumes that the arranged springs are composed of '#'s as springs, and '.' as non-springs.
def check_combo(arranged_springs, arrangements):
    single_arranged = "".join(arranged_springs)

# Determine if the permutation is possible given the restricted positioning.
def is_possible(original, permutation):
    # print(re.sub(r'#|\?', '*', original))
    # print(re.sub(r'#|\?', '*', permutation))
    return re.sub(r'#|\?', '*', original) == re.sub(r'#|\?', '*', permutation)

# Count remaining '#'s needed for the arrangement.
def count_remaining(arrangement, criteria):
    total_required = sum(criteria)
    current_springs = arrangement.count('#')
    return total_required - current_springs

# Get permutations, but restrict to position of the '.'s.
def permutate(arrangement, count):
    # replaced = arrangement.replace('?', '#', count)
    # print(f"Replaced: {replaced}")
    match_object = re.match(r'[?]+', arrangement)
    print(match_object)
    all_finds = re.findall(r'[?]+', arrangement)
    print(all_finds)
    # perms = combinations(replaced, len(replaced))
    # # perms = ["".join(perm) for perm in perms]
    # for perm in perms:
    #     print(perm)
    # print(perms)
    # for perm in permutations(replaced, 2):
    #     print(perm)
    # for perm in list(set(permutations(replaced))):
    #     perm_string = "".join(list(perm))
    #     perm_string = perm_string.replace('?', '.')
    #     print(perm_string)
    #     print(is_possible(arrangement, perm_string))
    #     if is_possible(arrangement, perm_string):
    #         print(perm_string)

# x = ".##"
# # print(list(permutations(x)))
# print(list(set(list(permutations(x)))))
# perms = list(set(list(permutations(x))))
# # print(list(combinations(x, 3)))
# pos_springs = ["".join(permutation) for permutation in perms]
# print(pos_springs)

# print(is_possible("...###...?#?#?...", "...###...?#?##..."))
# print(count_remaining("...###...?#?#?...", [3, 2, 1]))

if __name__ == "__main__":
    # input_file = open("input.txt", "r")
    input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    for line in lines:
        split_line = line.split(' ')
        spring = Spring(split_line[0], [int(num) for num in split_line[1].split(',')])
        springs.append(spring)

    for spring in springs:
        print(spring)
        remaining = count_remaining(spring.arrangement, spring.criteria)
        permutate(spring.arrangement, remaining)
        print('\n')