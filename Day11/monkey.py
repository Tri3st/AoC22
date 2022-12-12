# class Monkey
class Monkey:

    def __init__(self, name, monkey_id):
        self.name = name
        self.id = monkey_id
        self.items = []
        self.operation = ""
        self.test = {
            'test': -1,
            't': -1,
            'f': -1
        }

    def add_item(self, val):
        self.items.append(val)

    def remove_item(self):
        self.items.pop(0)

    def starting_items(self, items):
        items2 = items.split(", ")
        self.items = [int(x) for x in items2]

    def operation2(self, operation):
        self.operation = operation

    def test2(self, test):
        self.test['test'] = test[0]
        self.test['t'] = test[1]
        self.test['f'] = test[2]

    def do_round(self):
        print(self.operation)
        print(self.test)
        op = self.operation.split(" ")
        op2 = op[1]
        if op2 != "old":
            op2 = int(op[1])
        else:
            op2 = "square"
        print(self.test)
        result = 0
        results = []
        for item in self.items:
            if op[0] == "+":
                result = item + int(op2)
            else:
                if op2 == "square":
                    result = item * item
                else:
                    result = item * op2
            result = result // 3
            print("result : ", result)
            if result % int(self.test['test']) == 0:
                results.append((self.id, int(self.test['t']), result))
            else:
                results.append((self.id, int(self.test['f']), result))
        return results

    def __str__(self):
        array = ""
        for x in self.items:
            array += f"{str(x)},"
        array = array[:len(array) - 1]
        return f"{self.name}: {array}"


# class ZOO
class Zoo:
    def __init__(self):
        self.monkeys = []

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

    def do_jobs(self, jobs):
        for job in jobs:
            self.monkeys[job[1]].add_item(job[2])
            self.monkeys[job[0]].remove_item()

    def __str__(self):
        res = ""
        for i in range(len(self.monkeys)):
            res += f"Monkey {i} : {self.monkeys[i]}\n"
        return res
