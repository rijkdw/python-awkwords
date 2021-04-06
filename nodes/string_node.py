from .node import Node


class StringNode(Node):

    def __init__(self, string: str):
        self.string = string

    def evaluate(self) -> str:
        return self.string

    def __str__(self):
        return f"StringNode(string={self.string})"

    def __repr__(self):
        return self.__str__()
