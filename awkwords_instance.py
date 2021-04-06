from pprint import pprint

from .awkwords_parser import parse
from .awkwords_transformer import transform


class AwkwordsInstance:

    def __init__(self, main_string='', category_dict={}):
        # validate inputs


        self.main_string = main_string
        self.category_dict = category_dict

        # do the test for convoluted-ness
        temp = self.transformed_main_string

    @property
    def transformed_main_string(self) -> str:
        rep_max = 100
        transformed_main_string = self.main_string
        for i in range(rep_max):
            for name, body in self.category_dict.items():
                transformed_main_string = transformed_main_string.replace(name, f"[{body}]")
        # if there are still category names in the main_string, then this is too convoluted.
        for name in self.category_dict.keys():
            if name in transformed_main_string:
                raise Exception(f"Too many replacement iterations performed.  Offender={name}")
        return transformed_main_string

    def generate(self, number_words=1, sentencify=False):
        tree = transform(parse(self.transformed_main_string))
        words = [tree.evaluate() for i in range(number_words)]
        if number_words == 1:
            return words[0]
        return words

    @staticmethod
    def validate_categories(category_dict):
        for name, body in category_dict.items():
            if name.upper() != name:
                raise Exception(f"Provided category name \"{name}\" is not uppercase.")


if __name__ == '__main__':
    category_dict = {
        'V': 'a/e/i',
        'C': 'k/t/b/p/s',
        'X': '(C)V(C)'
    }
    print('\n'.join(AwkwordsInstance(
        main_string='X(X)(X)',
        category_dict=category_dict
    ).generate(number_words=100)))
