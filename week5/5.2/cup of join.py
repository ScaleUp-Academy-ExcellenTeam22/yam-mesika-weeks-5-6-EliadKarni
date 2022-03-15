"""
Cup of join.
By: Eliad Karni.

The feature receive lists and returns a list of the lists contents.
Each list's values separated by the received sep char, which its default value is '-'.

I've used the help of the websites:
double list comprehension -> https://stackoverflow.com/questions/1198777/double-iteration-in-list-comprehension
"""


def join(*args, sep='-') -> list:
    """
    The function split each list in the received
    :param args: lists of values wanted to be splitted.
    :param sep: separate variable which will be between each list values.
    :return: list of each list's contents separated by sep value.
    """
    separated_list = [var for contained_list in args for var in contained_list + [sep]]
    separated_list.pop()
    return separated_list


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
