"""Day 8"""
from MyMods.ReadDataFile import read_data
from Day8.Forest import Forest

data = """30373
25512
65332
33549
35390"""


def part1():

	f = Forest(data.split("\n"))
	print(f)
	print(f.visible)


def part2():
	pass
