def reverse_text(txt):
    index = len(txt) - 1

    while index >= 0:
        yield txt[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
