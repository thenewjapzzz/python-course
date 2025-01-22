list1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

list2 = map(multi, list1)

print(list(list2)) 