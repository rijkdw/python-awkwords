from random import choice

from .single_child_node import SingleChildNode


class OptionalNode(SingleChildNode):

    def evaluate(self) -> str:
        if choice([True, False]):
            return self.child_result_filtered()
        else:
            return ''

    def __str__(self):
        return f"OptionalNode(child_node={self.child_node})"

    def __repr__(self):
        return self.__str__()
