import re


class Valve:
    def __init__(self, data_line):
        data = data_line.split(";")
        pattern1 = r"^.*([A-Z]{2}).*=([0-9]+)$"
        pattern2 = r"[A-Z]{2}"
        s1 = re.findall(pattern1, data[0])
        s2 = re.findall(pattern2, data[1])
        self.name = s1[0][0]
        self.flow = int(s1[0][1])
        self.connect = s2

    def __str__(self):
        return f"[{self.name}] ({self.flow}) -> {self.connect}"
