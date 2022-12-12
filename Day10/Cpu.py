class Cpu:
    def __init__(self):
        self.stack = []
        self.x = 1

    def do_op(self, data):
        print(data)
        data2 = data.split(" ")
        if len(data2) > 1:
            # addx
            self.stack.append(self.x)
            self.x += int(data2[1])
            self.stack.append(self.x)
        else:
            # noop
            self.stack.append(self.x)

    def calc_signal(self):
        res = (self.stack[19] * 20) + (self.stack[59] * 60) + (self.stack[99] * 100)
        res2 = (self.stack[139] * 140) + (self.stack[179] * 180) + (self.stack[218] * 220)
        return res + res2

    def __str__(self):
        return f"20 - {self.stack[19]}\n60 - {self.stack[59]}\n100 - {self.stack[99]}\n140 - {self.stack[139]}\n" \
               f"180 - {self.stack[179]}\n220 - {self.stack[218]}"
