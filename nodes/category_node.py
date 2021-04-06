from .node import Node


class CategoryNode(Node):

    def __init__(self, category_name):
        self.category_name = category_name

    def evaluate(self) -> str:
        return self.category_name

    def __repr__(self):
        return f"CategoryNode(category_name={self.category_name})"

    def __str__(self):
        return self.__repr__()
