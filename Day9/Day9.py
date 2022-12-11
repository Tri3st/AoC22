"""Day 9"""
from Day9.map import HeadTail, TenHeadTail
from MyMods.ReadDataFile import read_data

data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

data2 = read_data("Day9/Day9.txt")


def part1():
	ht = HeadTail()
	print(ht)
	for line in data:
		ht.walk(line)
	print(ht)


def part2():
	data3 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")
	advhead = TenHeadTail()
	print(advhead)
	for line in data3:
		advhead.walk(line)
	print(advhead)