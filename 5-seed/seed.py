from itertools import groupby
from typing import Any

class Seed:
    def __init__(self, seed):
        self.seed = seed
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temperature = None
        self.humidity = None
        self.location = None

    def __str__(self) -> str:
        return f"Seed:\t\t{self.seed}\nSoil:\t\t{self.soil}\nFertilizer:\t{self.fertilizer}\nWater:\t\t{self.water}\nLight:\t\t{self.light}\nTemperature:\t{self.temperature}\nHumidity:\t{self.humidity}\nLocation:\t{self.location}\n...................."

    def set_prop(self, prop, value):
        if prop == "soil":
            self.soil = value
        elif prop == "fertilizer":
            self.fertilizer = value
        elif prop == "water":
            self.water = value
        elif prop == "light":
            self.light = value
        elif prop == "temperature":
            self.temperature = value
        elif prop == "humidity":
            self.humidity = value
        elif prop == "location":
            self.location = value

    def get(self, prop):
        if prop == "soil":
            return self.soil
        elif prop == "fertilizer":
            return self.fertilizer
        elif prop == "water":
            return self.water
        elif prop == "light":
            return self.light
        elif prop == "temperature":
            return self.temperature
        elif prop == "humidity":
            return self.humidity
        elif prop == "location":
            return self.location
        else:
            return None

# This is where we'll store the info per seed as Seed class.
almanac = []

# Extract source, dest, and range.
def extract_info(line):
    split_line = line.split(' ')
    source_start = int(split_line[1])
    dest_start = int(split_line[0])
    rng = int(split_line[2])
    return source_start, dest_start, rng

# Extract the source and dest properties.
def extract_props(line):
    props_array = line.split(' ')[0].split("-to-")
    source = props_array[0]
    dest = props_array[1]
    return source, dest

# Add properties to array.
def add_to_array(info):
    source, dest = extract_props(info[0])
    source_values = [item.__dict__[source] for item in almanac]
    print(f"processing {source} {dest}")

    for line in info[1:]:
        source_start, dest_start, rng = extract_info(line)
        # print(line)

        for value in source_values:
            if value in range(source_start, source_start + rng):
                dest_num = dest_start + (value - source_start)
                # print(value)
                # print(dest_num)
                if source == "seed":
                    match = list(filter(lambda x: x.seed == value, almanac))[0]
                    match.set_prop(dest, dest_num)
                else:
                    match = list(filter(lambda x: x.__dict__[source] == value, almanac))
                    if match:
                        match[0].set_prop(dest, dest_num)

    # Take care of numbers not included
    for item in almanac:
        if item.__dict__[dest] == None:
            item.set_prop(dest, item.__dict__[source])

# Group inputs into smaller arrays for easier manipulation and traversing.
def organize_inputs(lines):
    new_array = []
    for key, group in groupby(lines, lambda x: x == "\n"):
        if not key:
            new_array.append([str.strip('\n') for str in list(group)])
    return new_array

# Get initial list of seeds, as ranges
def get_seeds(seeds):
    start = seeds[0]
    seeds_full = [start]

    for i in range(1, len(seeds)):
        if i % 2 == 0:
            start = seeds[i]
            seeds_full.append(seeds[i])
        else:
            # print("Getting seeds")
            # for j in range(1, seeds[i]):
            #     seeds_full.append(start + j)
            seeds_full.append(start + seeds[i])

    return seeds_full

# Recursion?
def part2():
    global almanac
    almanac = []

    # input_file = open("input.txt", "r")
    input_file = open("sample.txt", "r")
    lines = input_file.readlines()
    input_arrays = organize_inputs(lines[1:])

    # Get seeds and store them in the almanac
    seeds_strings = lines[0].strip("seeds: ").split(" ")
    # Part 1 getting seeds
    seeds = [int(seed) for seed in seeds_strings]
    # Part 2 getting seeds
    seeds = get_seeds(seeds)
    print(seeds)
    
    lowest_location = -1
    i = 0
    while lowest_location:
        for seed in seeds:
            almanac.append(Seed(seed))
        
        # Organize remaining inputs
        input_arrays = organize_inputs(lines[1:])
        # print(input_arrays)

        # Add remaining properties
        for blocks in input_arrays:
            add_to_array(blocks)
        # print(almanac)
        locations = [item.__dict__["location"] for item in almanac]
        # for item in almanac:
        #     print(item)
        # print(locations)
        # print(min(seeds))
        print(f"Min: {min(locations)}")

        # if min(locations) == 0:
        #     break

        if (lowest_location > 0 and lowest_location < min(locations)) or (lowest_location == 0):
            break
        else:
            # print("No")
            # print(f"Current: {lowest_location}")
            # print(f"Next: {min(locations)}")
            pass

        match = list(filter(lambda x: x.location == min(locations), almanac))[0]
        # print("MATCH")
        # print(f"{match}")
        new_seeds = []
        lowest_loc_index = seeds.index(match.seed)
        print(lowest_loc_index)
        print(lowest_loc_index % 2 == 0)
        if lowest_loc_index % 2 == 0:
            new_seeds.append(seeds[lowest_loc_index] + 1)
            # print(seeds)
            # print(lowest_loc_index)
            new_seeds.append(seeds[lowest_loc_index + 1] - 1)
        else:
            # midpoint = int((seeds[lowest_loc_index - 1] + seeds[lowest_loc_index])/2)
            # new_seeds.append(midpoint)
            # new_seeds.append(seeds[lowest_loc_index])
            new_seeds.append(seeds[lowest_loc_index - 1] + 1)
            new_seeds.append(seeds[lowest_loc_index] - 1)
        # Refresh seeds
        seeds = new_seeds
        # print("refreshing seeds")
        # print(seeds)
        # Refresh almanac
        almanac = []
        lowest_location = min(locations)
        # print(f"current lowest location: {lowest_location}")

        # i += 1

        # if i == 5:
        #     break

    print(f"Lowest location for Part 2: {lowest_location}")

if __name__ == "__main__":
    # input_file = open("input.txt", "r")
    input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    # Get seeds and store them in the almanac
    seeds_strings = lines[0].strip("seeds: ").split(" ")
    # Part 1 getting seeds
    seeds = [int(seed) for seed in seeds_strings]
    # Part 2 getting seeds
    seeds = get_seeds(seeds)
    # print(seeds)
    for seed in seeds:
        almanac.append(Seed(seed))
    
    # Organize remaining inputs
    input_arrays = organize_inputs(lines[1:])
    # print(input_arrays)

    # Add remaining properties
    # for blocks in input_arrays:
    #     add_to_array(blocks)
    # print(almanac)
    locations = [item.__dict__["location"] for item in almanac]
    # for item in almanac:
    #     print(item)
    # print(locations)
    # print(min(seeds))
    # print(min(locations))

    input_file.close()
    
    part2()
    # test = Seed(1)
    # print(test.__dict__)