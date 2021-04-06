from .single_child_node import SingleChildNode


class MandatoryNode(SingleChildNode):

    def evaluate(self) -> str:
        return self.child_result_filtered()

    def __str__(self):
        return f"MandatoryNode(child_node={self.child_node}, filter_nodes={self.filter_nodes})"

    def __repr__(self):
        return self.__str__()
