from lark import Lark, Transformer

json_parser = Lark(r"""
    ?value   : dict
            | list
            | string
            | SIGNED_NUMBER                 -> number
            | "true"                        -> true
            | "false"                       -> false
            | "null"                        -> null

    string  : ESCAPED_STRING

    list    : "[" [value ("," value)*] "]"

    dict    : "{" [pair ("," pair)*] "}"
    pair    : string ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

""", start='value')


class TreeToJson(Transformer):

    def string(self, s):
        # print(s)
        # print(s[0])
        # (s,) = s
        # print(s)
        return s[0][1:-1]

    def number(self, n):
        # (n,) = n
        return float(n[0])

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


my_json_text = '{"name" : "Rijk", "age": 23, "interests" : ["programming", "stats", "music"]}'
tree = json_parser.parse(my_json_text)
print(TreeToJson().transform(tree))


