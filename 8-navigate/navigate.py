from dataclasses import dataclass, field
import parse

@dataclass
class Node:
    """Class to set the path of each node."""
    input_string: str
    node: str = ""
    L: str = ""
    R: str = ""

    def __post_init__(self):
        format_string = "{} = ({}, {})"
        parsed_nodes = list(parse.parse(format_string, self.input_string))
        self.node = parsed_nodes[0]
        self.L = parsed_nodes[1]
        self.R = parsed_nodes[2]

    def __str__(self) -> str:
        return f"Node is: {self.node}, L-->{self.L}, R-->{self.R}"
    
    def get(self, direction):
        if direction == "L":
            return self.L
        elif direction == "R":
            return self.R
        
@dataclass
class NodeWeighted:
    """This isn't really a 'weighted' node, but this is a node that stores its nearest Z's."""
    node: str
    z_steps: list[tuple] = field(default_factory=list)
        
# Function to check if all nodes end with a Z.
def all_end_nodes(nodes):
    for node in nodes:
        if node[2] == "Z":
            continue
        else:
            return False
    return True
    
# print(Node("AAA = (BBB, CCC)"))

# # Count required steps 
# def count_steps():

network = []

def part1():
    # input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    input_file = open("sample2.txt", "r")
    lines = input_file.readlines()
    path = lines[0].strip('\n')

    # Fill the network
    for line in lines[2:]:
        network.append(Node(line.strip('\n')))
    # print(path)
    # print(network)

    # Part 1
    i = 0
    source = "AAA"
    counter = 1
    while 1:
        if i == len(path):
            i = 0
            continue

        node = list(filter(lambda x: x.node == source, network))[0]
        dest = node.get(path[i])

        if dest == "ZZZ":
            break
        else:
            source = dest

        i += 1
        counter += 1
    print(f"Steps required: {counter}")
    input_file.close()

if __name__ == "__main__":
    # Part 2
    # input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    # input_file = open("sample2.txt", "r")
    input_file = open("sample3.txt", "r")
    lines = input_file.readlines()
    path = lines[0].strip('\n')

    # Fill the network
    network = []
    for line in lines[2:]:
        network.append(Node(line.strip('\n')))
    for node in network:
        print(node)
    print("----------------------")

    i = 0
    # source = "AAA"
    sources = [node.node for node in list(filter(lambda x: x.node[2] == 'A', network))]
    # print(sources)
    counter = 1
    # while 1:
    #     if i == len(path):
    #         i = 0
    #         continue

    #     nodes = [list(filter(lambda x: x.node == source, network))[0] for source in sources]
    #     # print(nodes)
    #     # break
    #     dest_nodes = [node.get(path[i]) for node in nodes]
    #     # print(dest_nodes)
    #     if all_end_nodes(dest_nodes):
    #         break
    #     else:
    #         sources = dest_nodes

    #     i += 1
    #     if i % 10000000 == 0:
    #         print(dest_nodes)
    #     counter += 1

    # print(f"Steps required: {counter}")

    weighted_nodes = []
    for node in sources:
        weighted_nodes.append(NodeWeighted(node))
    # print(weighted_nodes)
    print(sources)
    for src in sources:
        # print(source)
        j = 0
        source = src
        i = 0
        while 1:
            counter = 1
            # source = src
            while 1:
                if i == len(path):
                    i = 0
                    continue

                node = list(filter(lambda x: x.node == source, network))[0]
                print(node)
                dest = node.get(path[i])
                print(f"dest node: {dest}")
                print(all_end_nodes([dest]))

                if all_end_nodes([dest]):
                    source_node = list(filter(lambda x: x.node == src, weighted_nodes))[0]
                    source_node.z_steps += [(dest, counter + 1)]
                    print("breaking inner loop")
                    break
                else:
                    source = dest

                i += 1

                # if counter == 10:
                #     break
                counter += 1

            source = dest
            
            print("inner loop broken")

            if j == 2:
                break

            j += 1
    print(weighted_nodes)