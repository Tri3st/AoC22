"""Day 8"""
from Day8.Forest import Forest
from MyMods.ReadDataFile import read_data

data = """30373
25512
65332
33549
35390""".split("\n")

data2 = read_data("Day8/Day8.txt")


def part1():
	f1 = Forest(data2)
	print(f"visible : {f1.visible}")
	print(f"centric : {f1.highest_centric}")


def part2():
	pass