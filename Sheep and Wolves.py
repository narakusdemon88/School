"""
Name: Jon-Erik Akashi
Date: 1/24/2022
Assignment: Mini Project 1
"""

LEFT = 1
RIGHT = 0

class Node:

    def __init__(self, internal, num_of_moves=0, direction=(0, 0), left_node=None):
        self.variables = internal
        self.num_of_moves = num_of_moves
        self.left_node = left_node
        self.direction = direction

    def is_valid(self, initialSheep, initialWolves):

        num_of_current_sheep = self.variables[0]
        num_of_current_wolves = self.variables[1]

        # check if sheep is a negative number or sheep is greater than initial
        if num_of_current_sheep < 0 or num_of_current_sheep > initialSheep:
            return False

        # check if wolves is a negative number or wolves is greater than initial
        if num_of_current_wolves < 0 or num_of_current_wolves > initialWolves:
            return False

        if num_of_current_wolves > num_of_current_sheep > 0:
            return False

        l_w = initialWolves - num_of_current_wolves
        l_s = initialSheep - num_of_current_sheep

        if l_w > l_s > 0:
            return False

        return True

    def is_solution(self):
        solution = [0] * 3
        if self.variables == tuple(solution):
            return True
        else:
            return False

    def generate_right_nodes(self, initialSheep, initialWolves):
        # We can take 1 wolf or 2 wolves, 1 sheep or 2 sheep, or 1 sheep and 1 wolf:
        possible_trip_combos = [
            (0, 1),
            (0, 2),
            (1, 0),
            (2, 0),
            (1, 1)
        ]
        all_states = []

        r_s = self.variables[0]
        r_w = self.variables[1]
        r_b = self.variables[2]
        for rider in possible_trip_combos:
            change_sheep = rider[0]
            change_wolves = rider[1]
            if r_b == LEFT:
                new_variables = (r_s - change_sheep, r_w - change_wolves, RIGHT)
            else:
                new_variables = (r_s + change_sheep, r_w + change_wolves, LEFT)
            new_state = Node(new_variables, self.num_of_moves + 1, rider, self)
            if new_state.is_valid(initialSheep, initialWolves):
                all_states.append(new_state)
        return all_states

    @classmethod
    def initial_state(cls, initialSheep, initialWolves):
        sheep = initialSheep
        wolves = initialWolves
        default_side = 1
        return cls((sheep, wolves, default_side))


def process_results(check_list, initialSheep, initialWolves):
    output = []
    already_seen = set()
    temp_results = []

    while len(check_list) > 0:

        current_left_node = check_list.pop()
        next_states = current_left_node.generate_right_nodes(initialSheep, initialWolves)

        flipped = [i for i in reversed(next_states)]

        for possible_next_state in flipped:
            possible_variables = possible_next_state.variables
            if possible_variables not in already_seen:
                already_seen.add(possible_variables)
                if possible_next_state.is_solution():
                    temp_results.append(possible_next_state)
                else:
                    check_list.append(possible_next_state)


    # tree was generated above. where path gets created
    if temp_results:

        optimal_route = temp_results[0]
        curr_lst = []
        current_left_node = temp_results[0]
        a = 0
        while current_left_node:
            current_left_node = current_left_node.left_node
            a += 1
        low = a
        for a in range(0, len(temp_results)):
            b = 0
            current_left_node = temp_results[a]
            curr_lst.append(current_left_node)
            while current_left_node:
                current_left_node = current_left_node.left_node
                b += 1
            if b < low:
                optimal_route = temp_results[a]

        while optimal_route:
            output.append(optimal_route.direction)
            optimal_route = optimal_route.left_node
        output.pop()

    return output


class SemanticNetsAgent:
    def __init__(self):
        pass

    def solve(self, initialSheep, initialWolves):
        if not isinstance(initialSheep, int):
            return "Sheep must be an integer"

        if not isinstance(initialWolves, int):
            return "Wolves must be an integer"

        initial_state = Node.initial_state(initialSheep, initialWolves)

        check_lst = [initial_state]

        order_lst = process_results(check_lst, initialSheep, initialWolves)

        return order_lst

test_agent = SemanticNetsAgent()

test_agent.solve(3, 3)