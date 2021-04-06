from awkwords_parser import parse
from awkwords_transformer import transform
from utils.list_utils import list_to_count_map


# ======================================================================================================================
# GENERAL TESTS

test_strings = [
    'V/N/o',
    # 'abc',
    # # 'a/b',
    # 'a/b/c',
    # '[a/b/c]',
    # # 'a/b/c/d/e/f/g',
    # 'a/b*2/c',
    # 'a/e/i^i^a',
    # '[a/e/i]^i^a',
    # '(a/e/i)^i^a',
    # '[d[a*2/e*3/o*5]]^do',
    # # '[n/k][a/e]',
    # '(n/k)[a/e]'
]

for string in test_strings:
    print("STRING:", string)

    tree = parse(string)
    print("TREE:\n" + tree.pretty())

    node = transform(tree)
    print("STRUCTURE:", str(node))
    print("EVALUATED:", node.evaluate())

    results = [str(node.evaluate()) for x in range(10000)]
    print(list_to_count_map(results))

    print('=' * 100)

# ======================================================================================================================
# check how weights work out

# result_counts = {'da': 0, 'de': 0, 'do': 0}
# text = "d[a*2/e*3/o*5]^do"
# tree = MyTransformer().transform(awkwords_parser.parse(text))
# for i in range(10000):
#     output = tree.evaluate()
#     result_counts[output] += 1
# pprint(result_counts)

# ======================================================================================================================

# SUCCESS, FAILURE = 'SUCCESS', 'FAILURE'
# results = []
#
# # Test: filters of all kinds work
# filtered_strings = ['a/b/c^a^b', '[a/b/c]^a^b', '(a/b/c)^a^b', '[a/b/c^a]^b']
# failure = False
# for string in filtered_strings:
#     tree = parse(string)
#     for i in range(1000):
#         if transform(tree).evaluate() in ['a', 'b']:
#             failure = True
# if failure:
#     results.append(FAILURE)
# else:
#     results.append(SUCCESS)
#
# # Test: weights
# string = 'a*3/b/c*2'
# tree = parse(string)
# outputs = []
# for i in range(60000):
#     outputs.append(transform(tree).evaluate()[0])
# outputs = list_to_count_map(outputs)
# print(outputs)
# expected_weights = [30000, 10000, 20000]
# resulting_weights = [outputs[output] for output in ['a', 'b', 'c']]
# failure = False
# for ew, rw in zip(expected_weights, resulting_weights):
#     if abs(ew - rw)/ew*100 > 5:
#         failure = True
# if failure:
#     results.append(FAILURE)
# else:
#     results.append(SUCCESS)
#
# print(results)
