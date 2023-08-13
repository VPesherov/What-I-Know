collections = {
    'a': [None, '3', False],
    'b': [1],
    'h': ['65', 4, tuple()]
}


class DictUnpack:

    def __init__(self, data_dict):
        self.data_dict = data_dict

    def __iter__(self):
        self.keys = tuple(self.data_dict.keys())
        self.keys_i = -1
        self.values = []
        self.values_i = -1
        return self

    def __next__(self):
        self.values_i += 1
        if self.values_i >= len(self.values):
            self.keys_i += 1
            if self.keys_i >= len(self.keys):
                raise StopIteration
            key = self.keys[self.keys_i]
            self.values = self.data_dict[key]
            self.values_i = 0

        return self.values[self.values_i]


for item in DictUnpack(collections):
    print(item)
