from lark import Transformer

from .nodes.string_node import StringNode
from .nodes.optional_node import OptionalNode
from .nodes.mandatory_node import MandatoryNode
from .nodes.separated_node import SeparatedNode
from .nodes.chain_node import ChainNode
from .nodes.weight_node import WeightNode
from .nodes.filter_node import FilterNode
from .nodes.root_node import RootNode
from .nodes.category_node import CategoryNode


class AwkwordsTransformer(Transformer):

    def string(self, tokens):
        return StringNode(string=tokens[0])

    def sep(self, tokens):
        return SeparatedNode(children_nodes=tokens)

    def man(self, tokens):
        return MandatoryNode(child_node=tokens[0], filter_nodes=tokens[1:])

    def opt(self, tokens):
        return OptionalNode(child_node=tokens[0], filter_nodes=tokens[1:])

    def chain(self, tokens):
        return ChainNode(children_nodes=tokens)

    def weight(self, tokens):
        return WeightNode(weight=int(tokens[0]))

    def filter(self, tokens):
        return FilterNode(string=tokens[0])

    # def root(self, tokens):
    #     return RootNode(child_node=tokens[0])
    #
    # def cat(self, tokens):
    #     return CategoryNode(category_name=tokens[0])


def transform(tree):
    return AwkwordsTransformer().transform(tree)
