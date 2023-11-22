class Monkey:
    def __init__(self, data):
        tmp_data = data.split(": ")
        self.name = tmp_data[0]
        tmp_data2 = tmp_data[1].split(" ")
        if len(tmp_data2) > 1:
            self.op = {
                'num1': int(tmp_data2[0]),
                'num2': int(tmp_data2[2]),
                'op': tmp_data2[1]
            }
            self.type = "OP"
        else:
            self.job = int(tmp_data2[0])
            self.type = "NUM"
        self.type = None
        self.job = None

    def __str__(self):
        if self.type == 'NUM':
            return f'{self.name}: {self.job}'
        else:
            return f'{self.name}: {self.op["num1"]} {self.op["op"]} {self.op["num2"]}'