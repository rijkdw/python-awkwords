from .node import Node


class WeightNode(Node):

    def __init__(self, weight):
        self.weight = weight

    def evaluate(self) -> str:
        raise Exception("WeightNode asked to evaluate()")

    def __str__(self):
        return f"WeightNode(weight={self.weight})"

    def __repr__(self):
        return self.__str__()
