import numpy as np

from .node import Node
from .weight_node import WeightNode
from .filter_node import FilterNode
from awkwords.utils.prob_utils import normalise_to_unity


class SeparatedNode(Node):

    def __init__(self, children_nodes: list):
        self.children_nodes = children_nodes

    def evaluate(self) -> str:

        def choose_and_evaluate():
            return np.random.choice(a=choose_from, size=1, p=normalise_to_unity(weights))[0].evaluate()

        not_filter_nodes = [node for node in self.children_nodes if type(node) is not FilterNode]
        choose_from, weights = [], []
        index = 0
        while index < len(not_filter_nodes):
            if index < len(not_filter_nodes) - 1 and type(not_filter_nodes[index+1]) is WeightNode:
                choose_from.append(not_filter_nodes[index])
                weights.append(not_filter_nodes[index + 1].weight)
                index += 2
            else:
                choose_from.append(not_filter_nodes[index])
                weights.append(1)
                index += 1
        illegal_results = [node.string for node in self.children_nodes if type(node) is FilterNode]
        result = choose_and_evaluate()
        while result in illegal_results:
            result = choose_and_evaluate()
        return result

    def __str__(self):
        return f"SeparatedNode(children_nodes={self.children_nodes})"

    def __repr__(self):
        return self.__str__()
