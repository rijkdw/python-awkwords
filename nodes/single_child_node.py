from .node import Node


class SingleChildNode(Node):

    def __init__(self, child_node: Node, filter_nodes: list):
        self.child_node = child_node
        self.filter_nodes = filter_nodes

    @property
    def illegal_results(self):
        return [node.string for node in self.filter_nodes]

    def child_result_filtered(self):
        result = self.child_node.evaluate()
        while result in self.illegal_results:
            result = self.child_node.evaluate()
        return result
