class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            value = self.current * self.step
            self.current += 1
            return value
        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
