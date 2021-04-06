def indentify(string: str) -> str:
    tab = '  '
    current_indent_level = 0
    output_string = ''
    for letter in string:
        if letter in '([{':
            current_indent_level += 1
            output_string += letter + '\n' + tab*current_indent_level
        elif letter in ')]}':
            current_indent_level -= 1
            output_string += '\n' + tab*current_indent_level + letter
        elif letter in ';,':
            output_string += letter + '\n' + tab*current_indent_level
        else:
            output_string += letter
    return output_string


if __name__ == '__main__':
    print(indentify("Tree(a=12, b=[a,b,c], c=c)"))
