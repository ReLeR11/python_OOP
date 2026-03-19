class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary_tuple = tuple(dictionary.items())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.dictionary_tuple):
            value = self.dictionary_tuple[self.current]
            self.current += 1
            return value
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

