from enum import Enum
from itertools import groupby
import operator
import numpy as np

MAX_ROW = 0
MAX_COL = 0

class Pipe(Enum):
    VERTICAL = 0b1001
    HORIZONTAL = 0b0110
    LBEND = 0b1100
    JBEND = 0b1010
    SEVEN = 0b0011
    FBEND = 0b0101
    NONE = 0b0000

class Connection(Enum):
    NORTH = 0b1000
    EAST = 0b0100
    WEST = 0b0010
    SOUTH = 0b0001

# Get the next connection of the pipe.
def connect_next(pipe, connection):
    new = pipe.value ^ connection.value
    if new in [connection.value for connection in Connection]:
        return Connection(new)
    else:
        return None

# Get the opposite direction of a connection.
def opposite(connection):
    match connection:
        case Connection.NORTH:
            return Connection.SOUTH
        case Connection.SOUTH:
            return Connection.NORTH
        case Connection.WEST:
            return Connection.EAST
        case Connection.EAST:
            return Connection.WEST
        case _:
            return None

# Convert string to its appropriate pipe type.
def convert_type(pipe_string):
    match pipe_string:
        case "|":
            return Pipe.VERTICAL
        case "-":
            return Pipe.HORIZONTAL
        case "L":
            return Pipe.LBEND
        case "J":
            return Pipe.JBEND
        case "7":
            return Pipe.SEVEN
        case "F":
            return Pipe.FBEND
        # case ".":
        #     return Pipe.NONE

# Change coordinates
def change_coords(connection, coords):
    match connection:
        case Connection.NORTH:
            return (max(0, coords[0] - 1), coords[1])
        case Connection.SOUTH:
            return (min(MAX_ROW, coords[0] + 1), coords[1])
        case Connection.EAST:
            return (coords[0], min(MAX_COL, coords[1] + 1))
        case Connection.WEST:
            return (coords[0], max(0, coords[1] - 1))

# Get consecutive numbers in numpy array.
# Code from unutbu on Stack Overflow.
def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    # input_file = open("sample2.txt", "r")
    # input_file = open("sample3.txt", "r")
    lines = input_file.readlines()
    # l = input_file.readline()
    lines = [line.strip('\n') for line in lines]
    MAX_ROW = len(lines) - 1
    MAX_COL = len(lines[0]) - 1
    index_1D = "".join(lines).find("S")
    # Find the location (coordinates) of "S" in the lines array.
    coordinates = (int(index_1D / len(lines)), index_1D % len(lines))

    # Get 2 initial connections of the loop
    current_pipe = ""
    path_pipe = ["S"]
    s_connections = []
    coords_connections = []
    directions = []
    for direction in Connection:
        new_coordinates = change_coords(direction, coordinates)
        if new_coordinates != coordinates:
            pipe = lines[new_coordinates[0]][new_coordinates[1]]
            if pipe != ".":
                coords_connections.append(new_coordinates)
                s_connections.append(pipe)
                directions.append(direction)
                pipe = convert_type(pipe)
    # Initialize arrays to store path information
    path_directions = [None, directions[0]]
    path_coords = [coordinates, coords_connections[0]]
    # path_pipe is already initiated
    # From one connected pipe, find the whole path
    current_pipe = s_connections[0]
    coords = coords_connections[0]
    direction = directions[0]
    while current_pipe != "S":
        path_pipe.append(current_pipe)
        pipe = convert_type(current_pipe)
        direction = opposite(direction)
        direction = connect_next(pipe, direction)
        path_directions.append(direction)
        coords = change_coords(direction, coords)
        path_coords.append(coords)
        current_pipe = lines[coords[0]][coords[1]]
        s_connections.append(current_pipe)
    print(f"Farthest distance: {len(path_pipe) / 2}")

    # print(path_coords)
    arranged_coords = sorted(path_coords)
    # print(arranged_coords)
    # for coords1, coords2 in list(zip(path_coords, arranged_coords)):
    #     print(f"{coords1}------------{coords2}")
    points_in_loop = 0
    for key, group in groupby(arranged_coords, operator.itemgetter(0)):
        line_coords = (sorted(list(group)))
        indices = np.array([x[1] for x in line_coords])
        print(f"Indices: {indices}")
        consecutive_indices = consecutive(indices)
        print(consecutive(indices))
        j = 0
        consecutive_flag = False
        while j < len(consecutive_indices):
            print(j)
        # for arr in consecutive_indices:
            if consecutive_flag:
                arr = consecutive_indices[j][1:]
            else:
                arr = consecutive_indices[j]
            print(arr)
            if len(arr) % 2 == 1:
                index = np.where(indices == arr[len(arr) - 1])[0][0]
                print(f"value is: {arr[len(arr) - 1]}")
                print(f"index is: {index}")
                if index % 2 == 0:
                    points_in_loop += indices[index + 1] - arr[0] - 1
                else:
                    points_in_loop += arr[0] - indices[index - 1] - 1
                # print(f"consec: {consecutive_indices[j]}")
                # np.delete(consecutive_indices, j, 0)
                consecutive_flag = True
                # consecutive_indices[j + 1].remove(0)
                # j += 1
            else:
                consecutive_flag = False
            print("----------------------------")
            j += 1
        # for i in range(0, len(line_coords), 2):
        #     print(i)
        #     edge_left = line_coords[i][1]
        #     edge_right = line_coords[i + 1][1]
        #     points_in_loop += edge_right - edge_left - 1
        # arranged_coords.append(sorted(list(group)))
    print(f"Points inside loop: {points_in_loop}")