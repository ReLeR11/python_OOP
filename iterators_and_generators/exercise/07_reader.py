def read_next(*args):
    for item in args:
        yield from item


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
