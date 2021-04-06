from .node import Node


class RootNode(Node):

    def __init__(self, child_node):
        self.child_node = child_node

    def evaluate(self) -> str:
        return self.child_node.evaluate()

    def __repr__(self):
        return f"RootNode(child_node={self.child_node})"

    def __str__(self):
        return self.__repr__()
