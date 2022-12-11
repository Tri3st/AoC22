# class File
class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name}"


# class Dir

class Dir:

    def __init__(self, name=""):
        self.name = name
        self.contents = []

    def __str__(self):
        res = ""
        for content in self.contents:
            res += f"|- {content}\n"
        return res
