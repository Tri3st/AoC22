# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = {(x, y), }
        self.buffer = {'x': 0, 'y': 0}

    def move(self, dirc):
        if dirc == 'R':
            self.x += 1
        elif dirc == 'L':
            self.x -= 1
        elif dirc == 'U':
            self.y -= 1
        else:
            # dir == 'D'
            self.y += 1
        self.history.add((self.x, self.y))

    def buffer_add(self, dirc):
        if dirc == 'R':
            self.buffer['x'] += 1
        elif dirc == 'L':
            self.buffer['x'] -= 1
        elif dirc == 'U':
            self.buffer['y'] -= 1
        else:
            # dir == 'D'
            self.buffer['y'] += 1

    def buffer_flush(self):
        self.x += self.buffer['x']
        self.y += self.buffer['y']
        self.buffer = {'x': 0, 'y': 0}
        self.history.add((self.x, self.y))

    def distance_with_p(self, point):
        return max([abs(point.x - self.x), abs(point.y - self.y)])

    def __str__(self):
        return f"({self.x},{self.y})"


# HeadTail class
class HeadTail:

    def __init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        self.start = Point(0, 0)

    def walk(self, instr):
        instr = instr.split(" ")
        dirc = instr[0]
        dist = int(instr[1])
        for _ in range(dist):
            self.head.move(dirc)
            print(f"H({self.head}) T({self.tail}) distance: {self.head.distance_with_p(self.tail)}")
            if self.head.distance_with_p(self.tail) > 1:
                self.tail.buffer_flush()
            self.tail.buffer_add(dirc)

    def __str__(self):
        return f"H{self.head} T{self.tail} s{self.start}\n{self.tail.history}({len(self.tail.history)})"


# HeadTail class
class TenHeadTail:

    def __init__(self):
        self.head = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0),
                     Point(0, 0), Point(0, 0), Point(0, 0)]
        self.start = Point(0, 0)

    def walk(self, instr):
        instr = instr.split(" ")
        dirc = instr[0]
        dist = int(instr[1])
        print(f"direction : {dirc}, distance : {dist}")
        for _ in range(dist):
            self.head[0].move(dirc)

            res = f"H0 - {self.head[0]} "
            for i in range(1, 10):

                if self.head[i].distance_with_p(self.head[i - 1]) > 1:
                    self.head[i].buffer_flush()
                if self.head[i].distance_with_p(self.head[i - 1]) > 0:
                    self.head[i].buffer_add(dirc)
                res += f"H{i} - {self.head[i]} "
            print(res)

    def __str__(self):
        return f"H{self.head[0]} T{self.head[9]} s{self.start}\n{self.head[9].history}({len(self.head[9].history)})"

