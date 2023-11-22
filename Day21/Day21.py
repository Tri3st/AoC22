"""Day 21"""
from Monkey import Monkey
from MyMods.ReadDataFile import read_data

tmp_data = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".split("\n")

def part1():
	for line in tmp_data:
		m = Monkey(line)

def part2():
	pass