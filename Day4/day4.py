from ReadDataFile import read_data
from Day4.section import SectionPair

data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

data2 = read_data("Day4/input_day4.txt")


def part1():
    count = 0
    #d2 = data.split("\n")
    for d in data2:
        pair1 = SectionPair(d)
        if pair1.enclosed():
            count += 1
    print(count)

def part2():
    pass
