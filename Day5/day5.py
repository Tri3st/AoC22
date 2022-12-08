from MyMods.ReadDataFile import read_data
from Day5.stacks import Stacks

data = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

initial = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 """

data3 = read_data("Day5/input_day5.txt")
init = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
init2 = [['N', 'S', 'D', 'C', 'V', 'Q', 'T'], ['M', 'F', 'V'], ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
         ['D', 'Q', 'R', 'T', 'F'], ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'], ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
         ['W', 'F', 'R', 'L', 'C', 'T'], ['T', 'Z', 'N', 'S'], ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']]


def part1():
    s = Stacks(init2)
    s.calc_input(data3)
    print(s)


def part2():
    s = Stacks(init2, type_of_stack=2)
    s.calc_input(data3)
    print(s)
