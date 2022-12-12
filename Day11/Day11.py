"""Day 11"""
import re

from Day11.monkey import Monkey, Zoo
from MyMods.ReadDataFile import read_data

data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n")


def part1():
    nr_of_monkeys = 4
    zoo = Zoo()
    for i in range(nr_of_monkeys):
        zoo.add_monkey(Monkey(f"Monkey {i}", i))

    for i in range(nr_of_monkeys):
        print("i : ", i)

        zoo.monkeys[i].starting_items(data[(i * 7) + 1][18:])
        zoo.monkeys[i].operation2(data[(i * 7) + 2][23:])
        test = []
        for j in range(3):
            s = re.search(r"(\d+)", data[(i * 7) + 3 + j])
            test.append(s.groups()[0])
        zoo.monkeys[i].test2(test)

        print(zoo.monkeys[i])
        jobs = zoo.monkeys[i].do_round()
        print(jobs)
        zoo.do_jobs(jobs)

        print("after : ", zoo.monkeys[i])
    print(zoo)


def part2():
    pass
