class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.ind_outer = 0
        self.ind_inner = -1
        return self

    def __next__(self):
        while self.ind_outer <= len(self.list_of_list):
            try:
                while self.ind_inner <= len(self.list_of_list[self.ind_outer]):
                    try:
                        self.ind_inner += 1
                        return self.list_of_list[self.ind_outer][self.ind_inner]
                    except IndexError:
                        self.ind_outer += 1
                        self.ind_inner = -1
            except IndexError:
                raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert (list(FlatIterator(list_of_lists_1)) ==
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None])


if __name__ == '__main__':
    test_1()
