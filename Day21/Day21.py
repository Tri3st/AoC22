"""Day 21"""
from Day21.MonkeyTree import MonkeyTree
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
	monkeys = MonkeyTree("root")
	monkeys_list = {}
	for line in tmp_data:
		tmp_line = line.split(":")
		values = tmp_line[1].strip().split(" ")
		monkeys_list[tmp_line[0]] = int(values[0]) if len(values) == 1 else values
	print(monkeys_list)
	while True:
		monkeys.add_data()

def part2():
	pass
