from lark import Lark

# WORKS UP TO SEPARATION -- DO NOT EDIT ===========================================================
# awkwords_parser = Lark(r"""
#
#     string  : WORD
#
#     sep     : (string ("/" string)+)|(chain ("/" chain)+)
#
#     man     : "[" chain "]"
#     opt     : "(" chain ")"
#
#     ?chain  : (string|sep|man|opt)+
#
#     %import common.WORD
#     %import common.INT
#
# """, start='chain')
# =================================================================================================


# WORKS FOR FILTERING -- DO NOT EDIT ==============================================================
# awkwords_parser = Lark(r"""
#
#     string  : WORD
#     number  : INT
#
#     filter  : "^" WORD
#     weight  : "*" INT
#
#     sep     : ((string weight? ("/" string weight?)+) | (chain weight? ("/" chain weight?)+)) filter*
#     man     : "[" chain "]" filter*
#     opt     : "(" chain ")" filter*
#
#     ?expr   : string|sep|man|opt
#
#     ?chain  : (expr)+
#
#     %import common.WORD
#     %import common.INT
#
# """, start='chain')
# =================================================================================================

# WORKS FOR EVERYTHING -- DO NOT EDIT ==============================================================
# awkwords_parser = Lark(r"""
#
#     string  : WORD
#     number  : INT
#
#     filter  : "^" WORD
#     weight  : "*" INT
#
#     sep     : ((string weight? ("/" string weight?)+) | (chain weight? ("/" chain weight?)+)) filter*
#     man     : "[" chain "]" filter*
#     opt     : "(" chain ")" filter*
#
#     ?chain  : (string|sep|man|opt)+
#
#     %import common.WORD
#     %import common.INT
#
# """, start='chain')
# =================================================================================================

awkwords_parser = Lark(r"""

    string  : WORD | ("ɐ".."ʯ")+ | ("ð".."θ")+
    number  : INT

    filter  : "^" WORD
    weight  : "*" INT

    sep     : ((string weight? ("/" string weight?)+) | (chain weight? ("/" chain weight?)+)) filter*
    man     : "[" chain "]" filter*
    opt     : "(" chain ")" filter*

    ?chain  : (string|sep|man|opt)+

    %import common.WORD
    %import common.INT

""", start='chain')


def parse(text):
    return awkwords_parser.parse(text)
