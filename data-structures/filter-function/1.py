valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

# com uma linha de código
print(list(filter(lambda x: x > 20, valores)))