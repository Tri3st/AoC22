# class Monkey
import re


class Monkey:

    def __init__(self, mid, m_type):
        self.id = mid
        self.items = []
        self.operation = ''
        self.test = {
            'test': -1,
            't': -1,
            'f': -1
        }
        self.count = 0
        self.m_type = m_type

    def init_operation(self, operation):
        self.operation = operation

    def init_test(self, test):
        self.test.update(**test)

    def init_starting_items(self, items):
        self.items = [x for x in items]

    def add_item(self, val):
        self.items.append(val)

    def throw_item(self):
        """
        Args:
            type: 1 for part 1
                  2 for part 2 (no dividing by 3 anymore)
        """
        item = self.items.pop(0)
        if self.operation[1] == 'old':
            comp = item
        else:
            comp = int(self.operation[1])
        if self.operation[0] == '+':
            item += comp
        else:
            item *= comp
        if self.m_type == 1:
            item = int(item / 3)
        if item % self.test['test'] == 0:
            to_monkey = self.test['t']
        else:
            to_monkey = self.test['f']
        self.count += 1
        return to_monkey, item

    def has_items(self):
        return len(self.items) > 0

    def __str__(self):
        array = ','.join([str(x) for x in self.items])
        return f"Monkey {self.id}: {array}"
