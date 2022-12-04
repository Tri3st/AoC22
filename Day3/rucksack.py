

class Rucksack():
    def __init__(self, items):
        self.items = items
        self.comp_size = int(len(items) // 2)
        self.comp1 = ""
        self.comp2 = ""
        self.shared_item = ""
        self.score = 0
        self.calc()
    
    def calc(self):
        self.comp1 = self.items[:self.comp_size]
        self.comp2 = self.items[self.comp_size:]
        self.shared_item = [it for it in self.comp1 if it in self.comp2]
        shared1 = self.shared_item[0]
        score1 = ord(shared1)
        if 64 < score1 < 91:
            self.score = score1 - 38
        elif 96 < score1 < 123:
            self.score = score1 - 96

    def __str__(self):
        return "%d" % self.score
        
    