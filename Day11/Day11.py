"""Day 11"""
import re
from .monkey import Monkey
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
    If false: throw to monkey 1""".split("\n\n")

m_round = 0
monkeys = []

try:
    f = open('Day11/Day11.txt', "r")
    data2 = f.read().split("\n\n")
    f.close()
except Exception as e:
    print("Oops. there was an error : %s" % e.__str__())


def populate_monkeys(datafile, m_type):
    global monkeys
    for data_line in datafile:
        data_line2 = data_line.split("\n")
        pattern1 = re.compile(r"^\w+\s?(?P<id>\d+):$")
        re1 = pattern1.findall(data_line2[0])
        mid = re1[0]
        pattern2 = re.compile(r"(\d{1,2})+")
        re2 = pattern2.findall(data_line2[1])
        items = [int(x) for x in re2]
        pattern3 = re.compile(r"Operation: new = old ([+*-/])\s(\d+|old)")
        re3 = pattern3.findall(data_line2[2])
        operation = re3[0]
        pattern4 = re.compile(r"Test: divisible by (\d+)")
        test = {}
        re4 = pattern4.findall(data_line2[3])
        test['test'] = int(re4[0])
        pattern5 = re.compile(r"If true: throw to monkey (\d+)")
        re5 = pattern5.findall(data_line2[4])
        pattern6 = re.compile(r"If false: throw to monkey (\d+)")
        re6 = pattern6.findall(data_line2[5])
        test['test'] = int(re4[0])
        test['t'] = int(re5[0])
        test['f'] = int(re6[0])
        # monkey type: 1 for part 1 and 2 for part 2
        m = Monkey(mid, m_type=m_type)
        m.init_test(test)
        m.init_operation(operation)
        m.init_starting_items(items)
        monkeys.append(m)


def print_monkeys():
    global m_round, monkeys
    print(f"Monkeys == Round {m_round}")
    for monkey in monkeys:
        print(monkey)


def do_round():
    global m_round, monkeys
    for monkey in monkeys:
        while monkey.has_items():
            result = monkey.throw_item()
            monkeys[result[0]].add_item(result[1])
    m_round += 1


def part1():
    populate_monkeys(data, m_type=1)

    print_monkeys()
    while m_round < 20:
        do_round()

    print_monkeys()

    print("final results :")
    results = []
    for monkey in monkeys:
        print(f"Monkey {monkey.id} inspected {monkey.count} items")
        results.append(monkey.count)
    results.sort(reverse=True)
    print(results[0] * results[1])


def part2():
    populate_monkeys(data2, m_type=2)

    print_monkeys()
    while m_round < 10000:
        do_round()

    print_monkeys()

    print("final results :")
    results = []
    for monkey in monkeys:
        print(f"Monkey {monkey.id} inspected {monkey.count} items")
        results.append(monkey.count)
    results.sort(reverse=True)
    print(results[0] * results[1])

