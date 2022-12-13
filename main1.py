class FlatIterator:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.list_iter = iter(self.multi_list)
        self.inside_list = []
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if len(self.inside_list) == self.counter:
            self.inside_list = None
            self.counter = 0
            while not self.inside_list:
                self.inside_list = next(self.list_iter)
        return self.inside_list[self.counter]


def flat_generator(list_of_list):
    for sub_list in list_of_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    inside_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], ]

    print('Iterator_enter')
    for item in FlatIterator(inside_list):
        print(item)

    print('Comprihension_enter')
    flat_list = [item for item in FlatIterator(inside_list)]
    print(flat_list)

    print('Generator_enter')
    for item in flat_generator(inside_list):
        print(item)
