import re

FILE_NAME = "input.txt"
SAMPLE = "sample.txt"

input_file = open(FILE_NAME, "r")
# input_file = open(SAMPLE, "r")
lines = input_file.readlines()

# for i in range(0, len(lines)):
#     line = lines[i]
#     print(line[:-1])
#     numbers = re.findall(r'\d+', line)
#     index = 0
#     for number in numbers:
#         match_obj = re.search(number, line[index:])
#         print(match_obj.group())
#         # index = match_obj.span()[1]
#         # print(match_obj.span())
#         start = match_obj.span()[0]
#         end = match_obj.span()[1]
#         if i > 0:
#             before = lines[i-1][(start-1):(end+1)]
#             print(f"Before:\t\t{before}")
#             # print(re.findall(r'\$', before))
#             print(before.strip('.' + r'\d+'))
#         current = lines[i][(start-1):(end+1)]
#         print(f"Line:\t\t{current}")
#         if i < len(lines) - 1:
#             after = lines[i+1][(start-1):(end+1)]
#             print(f"After:\t\t{after}")
#     print('\n')

# number_array = []
# number_set = set()
# for i in range(0, len(lines)):
#     line = lines[i]
#     print(line[:-1])
#     numbers = re.findall(r'\d+', line)
#     index = 0
#     for number in numbers:
#         number_array.append(number)
#         number_set.add(number)
        # match_obj = re.search(number, line[index:])
        # print(match_obj.group())
        # # index = match_obj.span()[1]
        # # print(match_obj.span())
        # start = match_obj.span()[0]
        # end = match_obj.span()[1]
        # if i > 0:
        #     before = lines[i-1][(start-1):(end+1)]
        #     print(f"Before:\t\t{before}")
        #     # print(re.findall(r'\$', before))
        #     print(before.strip('.' + r'\d+'))
        # current = lines[i][(start-1):(end+1)]
        # print(f"Line:\t\t{current}")
        # if i < len(lines) - 1:
        #     after = lines[i+1][(start-1):(end+1)]
        #     print(f"After:\t\t{after}")
    # print('\n')
# print(number_array)
# print(len(number_array))
# print(number_set)
# print(len(number_set))
# print(len(set(number_array)))

# for i in range(0, len(lines)):
#     line = lines[i]
#     print(line[:-1])
#     # stripped = line.strip('.' + r'\d+')
#     numbers = re.findall(r'[^0-9.\n]', line)
#     print(numbers)
#     index = 0
#     for number in numbers:
#         print(number)
#         # match_obj = re.search(number, line[index:])
#         idx = line.index(number)
#         print(idx)
#         # print(match_obj.group())
#     #     # index = match_obj.span()[1]
#     #     # print(match_obj.span())
#     #     start = match_obj.span()[0]
#     #     end = match_obj.span()[1]
#         if i > 0:
#             before = lines[i-1][(idx-1):(idx+2)]
#             print(f"Before:\t\t{before}")
#             print(lines[i-1][:-1])
#     #         # print(re.findall(r'\$', before))
#     #         print(before.strip('.' + r'\d+'))
#         current = lines[i][(idx-1):(idx+2)]
#         print(f"Line:\t\t{current}")
#         if i < len(lines) - 1:
#             after = lines[i+1][(idx-1):(idx+2)]
#             print(f"After:\t\t{after}")
#             print(lines[i+1][:-1])
#     print('\n')

for line in lines:
    # print(line)
    numbers = re.findall(r'\d+', line)
    # print(numbers)
    if not len(set(numbers)) == len(numbers):
        print(len(set(numbers)) == len(numbers))