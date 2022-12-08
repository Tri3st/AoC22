from MyMods.ReadDataFile import read_data
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
    data3 = data.split("\n")
    groups = []
    group = []
    score = 0
    for line in data2:
        s = set()
        r = Rucksack(line)
        temp = r.items
        s2 = [s.add(c) for c in temp]
        group.append(s)
        if count % 3 == 0:
            groups.append(group)
            group = []
        count += 1
    for group in groups:
        group[0].intersection_update(group[1], group[2])
        char2 = "".join(group[0])
        char1 = ord(char2)
        if 64 < char1 < 91:
            score += char1 - 38
        elif 96 < char1 < 123:
            score += char1 - 96
    print(score)
            