# Determine the number of possibilites to win a given race.
def get_wins(race_time, record_distance):
    wins = 0
    for time in range(1, race_time):
        wins += 1 if time * (race_time - time) > record_distance else 0
    return wins

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    time_array = list(filter(lambda x: x != '', lines[0].strip("Time:").strip('\n').split(" ")))
    distance_array = list(filter(lambda x: x != '', lines[1].strip("Distance:").strip('\n').split(" ")))

    error_margin = 1
    for race_time, record_distance in zip(time_array, distance_array):
        error_margin *= get_wins(int(race_time), int(record_distance))
    print(f"Margin of error: {error_margin}")

    big_time = "".join(time_array)
    big_distance = "".join(distance_array)
    print(f"Number of ways to win: {get_wins(int(big_time), int(big_distance))}")