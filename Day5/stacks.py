# class Stacks
import re
class Stacks:

    def __init__(self, data_input, type_of_stack=1):
        """
                data = stacks data in text format
                containing rows of data .. in the form of:
                        [M]     [B]             [N]
                [T]     [H]     [V] [Q]         [H]
                [Q]     [N]     [H] [W] [T]     [Q]
                [V]     [P] [F] [Q] [P] [C]     [R]
                [C]     [D] [T] [N] [N] [L] [S] [J]
                [D] [V] [W] [R] [M] [G] [R] [N] [D]
                [S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
                [N] [M] [F] [D] [R] [C] [W] [T] [M]
                 1   2   3   4   5   6   7   8   9

                 type_of_stack : 1 - move container 1 by 1 (part1)
                                 2 - move containers at once (part2)
        """
        self.stack_arrays = data_input
        self.nr_of_stacks = len(self.stack_arrays)
        self.type_of_stack = type_of_stack

    def calc_input(self, data):
        # data_lines = data.split("\n")
        for line in data:
            x = re.search("^\\D*(\\d+).*(\\d).*(\\d)$", line)
            nr_of_moves = int(x.group(1))
            from_stack = int(x.group(2)) - 1
            to_stack = int(x.group(3)) - 1
            print("before : ", self.stack_arrays)
            print(f"{nr_of_moves} {from_stack + 1} {to_stack + 1}")
            if self.type_of_stack == 1:
                self.make_move(nr_of_moves, from_stack, to_stack)
            else:
                self.make_move2(nr_of_moves, from_stack, to_stack)
            print("after : ", self.stack_arrays, "\nnr of colums: ", len(self.stack_arrays), "\n\n\n")

    def make_move(self, nr, fr, to):
        for i in range(nr):
            self.stack_arrays[to].append(self.stack_arrays[fr][len(self.stack_arrays[fr])])
            self.stack_arrays[fr].pop()

    def make_move2(self, nr, fr, to):
        temp_lst = self.stack_arrays[fr][(len(self.stack_arrays[fr]) - nr):(len(self.stack_arrays[fr]))]
        print(temp_lst)
        for _ in range(nr):
            self.stack_arrays[fr].pop()
        self.stack_arrays[to].extend(temp_lst)

    def __str__(self):
        res = ""
        for i in range(len(self.stack_arrays)):
            res += self.stack_arrays[i][len(self.stack_arrays[i]) - 1]
        return f"{res}"
