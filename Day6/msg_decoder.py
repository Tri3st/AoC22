# Message Decoder
class Decoder:

    def __init__(self, data):
        self.data = data
        self.count = 0
        while True:
            start = self.count
            end = self.count + 14
            self.block = self.data[start:end]
            if not self.check_block2(self.block):
                self.count += 1
            else:
                break
        self.data = self.data[self.count:]
        self.marker = self.count + 14

    def check_block(self, block):
        b = {block[0], block[1], block[2], block[3]}
        return len(b) == 4

    def check_block2(self, block):
        b = {block[0], block[1], block[2], block[3], block[4], block[5], block[6], block[7], block[8], block[9],
             block[10], block[11], block[12], block[13]}
        return len(b) == 14
