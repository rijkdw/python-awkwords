from .node import Node


class FilterNode(Node):

    def __init__(self, string: str):
        self.string = string

    def evaluate(self) -> str:
        raise Exception("FilterNode asked to evaluate()")

    def __str__(self):
        return f"FilterNode(string={self.string})"

    def __repr__(self):
        return self.__str__()