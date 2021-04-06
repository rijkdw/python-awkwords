from .node import Node


class ChainNode(Node):

    def __init__(self, children_nodes: list):
        self.children_nodes = children_nodes

    def evaluate(self) -> str:
        return ''.join([node.evaluate() for node in self.children_nodes])

    def __str__(self):
        return f"ChainNode(children_nodes={self.children_nodes})"

    def __repr__(self):
        return self.__str__()
