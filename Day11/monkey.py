# class Monkey
class Monkey:

    def __init__(self, name):
        self.name = name
        self.items = []
        self.operation = ""
        self.test = {
            'test': -1,
            't': -1,
            'f': -1
        }

    def add_item(self, val):
        self.items.append(val)

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
            if op == "+":
                result = item + op2
            else:
                if op2 == "square":
                    result = item * item
                else:
                    result = item * op2
            result = result // 3
            print("result : ", result)
            if result % int(self.test['test']) == 0:
                results.append((int(self.test['t']), item))
            else:
                results.append((int(self.test['f']), item))
        self.items = []
        return results

    def __str__(self):
        array = ""
        for x in self.items:
            array += f"{str(x)},"
        array = array[:len(array) - 1]
        return f"{self.name}: {array}"


