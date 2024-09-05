import types


def flat_generator(list_of_lists):
    ind_outer = 0
    ind_inner = 0
    while ind_outer <= len(list_of_lists):
        try:
            while ind_inner <= len(list_of_lists[ind_outer]):
                try:
                    yield list_of_lists[ind_outer][ind_inner]
                    ind_inner += 1
                except IndexError:
                    ind_outer += 1
                    ind_inner = 0
        except IndexError:
            break


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
