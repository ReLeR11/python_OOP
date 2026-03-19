def possible_permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in possible_permutations(lst[:i] + lst[i+1:]):
                yield [lst[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]