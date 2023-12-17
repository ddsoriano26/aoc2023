from itertools import permutations, combinations

x = ".##"
# print(list(permutations(x)))
print(list(set(list(permutations(x)))))
perms = list(set(list(permutations(x))))
# print(list(combinations(x, 3)))
pos_springs = ["".join(permutation) for permutation in perms]
print(pos_springs)