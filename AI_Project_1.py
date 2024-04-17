import heapq
import queue
import copy


class Node:
    def __init__(self, state, parent, action, cost, heuristic):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __eq__(self, other):
          # Nodes are equal if they have the same state
        return self.state == other.state

    def __lt__(self, other):
            # Nodes are ordered by their total cost (cost + heuristic)
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def parse_state(lines):
    state = []
    for i in range(0, len(lines), 4):  # Assuming there are 4 lines per layer including the blank line
        layer = lines[i:i+3]  # Get the next three lines which represent a layer
        if len(layer) == 3:  # Ensure there are exactly three lines for the layer
            state.append([[int(tile) for tile in row.split()] for row in layer])
    return state

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    # Ensure the file has the correct number of lines for initial and goal states including blank lines
    if len(lines) != 23:
        raise ValueError("Input file does not contain the correct number of lines.")
    initial_state = parse_state(lines[:11])
    goal_state = parse_state(lines[12:23])
    return initial_state, goal_state



def write_output_file(output_path, initial_state, goal_state, solution, depth, total_nodes, fn_values):
    with open(output_path, 'w') as file:
        for line in initial_state:
            file.write(line + '\n')
        file.write('\n')
        for line in goal_state:
            file.write(line + '\n')
        file.write('\n')
        file.write(str(depth) + '\n')
        file.write(str(total_nodes) + '\n')
        file.write(' '.join(solution) + '\n')
        file.write(' '.join(map(str, fn_values)) + '\n')

def find_tile_coordinates(state, tile):
    for z, layer in enumerate(state):
        for y, row in enumerate(layer):
            for x, value in enumerate(row):
                if value == tile:
                    return (z, y, x)
    return None  # If the tile is not found, return None

def manhattan_distance(state, goal_state):
    distance = 0
    for z in range(3):
        for y in range(3):
            for x in range(3):
                tile = state[z][y][x]
                if tile != 0:  # Skip the blank tile
                    goal_z, goal_y, goal_x = find_tile_coordinates(goal_state, tile)
                    distance += abs(z - goal_z) + abs(y - goal_y) + abs(x - goal_x)
    return distance


def state_to_tuple(state):
    return tuple(tuple(tuple(row) for row in layer) for layer in state)

def a_star_search(initial_state, goal_state):
    """Performs the A* search algorithm to find a solution to the 26-puzzle problem."""

    frontier = queue.PriorityQueue()
    visited = set()
    initial_state_tuple = state_to_tuple(initial_state)
    goal_state_tuple = state_to_tuple(goal_state)

    frontier.put(Node(initial_state_tuple, None, None, 0, manhattan_distance(initial_state_tuple, goal_state)))

    while not frontier.empty():
        node = frontier.get()

        if node.state == goal_state_tuple:
            return node

        if state_to_tuple(node.state) not in visited:
            visited.add(state_to_tuple(node.state))

            for action in ["E", "W", "N", "S", "U", "D"]:
                new_state = move(node.state, action)

                if new_state is not None:
                    new_node = Node(new_state, node, action, node.cost + 1, manhattan_distance(new_state, goal_state))
                    frontier.put(new_node)

    return None

def find_blank_position(state):
    for z, layer in enumerate(state):
        for y, row in enumerate(layer):
            for x, tile in enumerate(row):
                if tile == 0:
                    return (z, y, x)
    raise ValueError("No blank space found in the state.")

def copy_state(state):
    return copy.deepcopy(state)

def move(state, action):
    """Moves the blank tile in the given direction."""
    if isinstance(state, tuple):
        state = [list(list(row) for row in layer) for layer in state]

    blank_x, blank_y, blank_z = find_blank_position(state)

    if action == "E" and blank_x < 2:
        new_state = copy_state(state)
        new_state[blank_x][blank_y][blank_z] = new_state[blank_x + 1][blank_y][blank_z]
        new_state[blank_x + 1][blank_y][blank_z] = 0
        return new_state

    elif action == "W" and blank_x > 0:
        new_state = copy_state(state)
        new_state[blank_x][blank_y][blank_z] = new_state[blank_x - 1][blank_y][blank_z]
        new_state[blank_x - 1][blank_y][blank_z] = 0
        return new_state

    elif action == "N" and blank_y < 2:
        new_state = copy_state(state)
        new_state[blank_x][blank_y][blank_z] = new_state[blank_x][blank_y + 1][blank_z]
        new_state[blank_x][blank_y + 1][blank_z] = 0
        return new_state

    elif action == "S" and blank_y > 0:
        new_state = copy_state(state)
        new_state[blank_x][blank_y][blank_z] = new_state[blank_x][blank_y - 1][blank_z]
        new_state[blank_x][blank_y - 1][blank_z] = 0
        return new_state

    elif action == "U" and blank_z < 2:
        new_state = copy_state(state)
        new_state[blank_x][blank_y][blank_z] = new_state[blank_x][blank_y][blank_z + 1]
        new_state[blank_x][blank_y][blank_z + 1] = 0
        return new_state

    elif action == "D" and blank_z > 0:
        new_state = copy_state(state)
        new_state[blank_x][blank_y][blank_z] = new_state[blank_x][blank_y][blank_z - 1]
        new_state[blank_x][blank_y][blank_z - 1] = 0
        return new_state

# Main execution
if __name__ == "__main__":
    input_file = 'Input.txt'
    output_file = 'Output1.txt'
    initial_state, goal_state = parse_input_file(input_file)
    print("Initial State:")
    for layer in initial_state:
        for row in layer:
            print(row)
        print()
    print("Goal State:")
    for layer in goal_state:
        for row in layer:
            print(row)
        print()
    solution, depth, total_nodes, fn_valu 1es = a_star_search(initial_state, goal_state)
    if solution:
        write_output_file(output_file, initial_state, goal_state, solution, depth, total_nodes, fn_values)
    else:
        print("No solution found.")
