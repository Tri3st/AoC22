# DirTree.py

class Node:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size})"


class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def totalSize(self):
        # calculate total size of directory and child directories
        pass

    def add(self, item):
        self.children.append(item)

    def __str__(self):
        return f"dir {self.name}"


class DirTree:
    def __init__(self):
        self.root = Tree("dir /")
        self.depth = 1
        self.current_place = self.root

    def command(self, command):
        command = command.split(" ")
        print(command)
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == "..":
                    self.depth -= 1
                else:
                    self.depth += 1
        elif command[1] == 'ls':
            pass
        else:
            if command[0] == 'dir':
                x = Tree(command[1])
            else:
                x = Node(command[1], command[0])
            self.root.add(x)

    def dir_exists(self, dir_name):
        for child in self.root.children:
            if child.name == dir_name and isinstance(child, Tree):
                return True
        return False

    def return_dir(self, name):
        pass

    def __str__(self):
        res = "- /\n"
        for child in self.root.children:
            print("type : ", type(child))
            spaces = " " * self.depth
            name = None
            if isinstance(child, Node):
                name = f"{spaces} - {child.name} ({child.size})"
            else:
                name = f"{spaces} - {child.name.upper()}"
            res += f"{name} (type: {type(child)})\n"
        return res
