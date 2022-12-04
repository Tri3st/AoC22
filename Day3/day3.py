from ReadDataFile import read_data
from Day3.rucksack import Rucksack


data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

data2 = read_data("Day3/input_day3.txt")

def part1():
    total = 0
    # data2 = data.split("\n")
    for line in data2:
        ruck = Rucksack(line)
        total = total + int(ruck.score)
        print("shared letter :", ruck.shared_item)
        print("score this round : ", ruck.score)
    print("total : ",total)


def part2():
    total = 0
    count = 1
    data2 = data.split("\n")
    groups = []
    for line in data2:
        group = []
        for _ in range(3):
            r = Rucksack(line)
            s = set((r.items))
            group.append(s)
        groups.append(group)
    for group in groups:
        group[0].intersection(group[1], group[2])
        print(group[0])
            