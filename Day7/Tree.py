# class Tree

class Node:
    def __init__(self, val):
        """
            Nodes in a tree. Value is a dict.
                - name = name of dir
            Nodes with no children are leaves
                - name = name of file
                - size = size of file
        """
        self.value = val
        self.branches = []

    def add_child(self, val):
        self.branches.append(Node(val))


class Tree:

    def __init__(self):
        self.root = Node("{ name: '/'}")

    def add_child(self, val):
        self.add_child(val)


    def __str__(self):
        return f"test"

