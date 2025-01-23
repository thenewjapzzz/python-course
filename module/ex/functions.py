def to_find(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return 1
    return -1
