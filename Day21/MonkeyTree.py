class Monkey:
    def __init__(self, monkey_id, data=""):
        self.monkey_id = monkey_id
        self.name = data
        self.job = -1

    def __str__(self):
        return f'({self.monkey_id}) {self.name}'


class MonkeyTree:
    def __init__(self, data):
        self.leaf1 = None
        self.leaf2 = None
        self.op = ""
        self.value = -1

    def add_data(self, data):
        if len(data) == 1:
            self.value = int(data)
        else:
            tmp = data.split(" ")
        left = MonkeyTree(data[0])
        right = MonkeyTree(data[2])
        self.leaf1 = left
        self.leaf2 = right
        self.op = data[1]

    def is_leaf(self):
        return self.leaf1.value != -1 and self.leaf2.value != -1

    def __str__(self):
        return f"leaf / root \\ leaf"
