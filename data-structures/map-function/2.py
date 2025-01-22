list2 = [10, 20, 30, 40]

def multi(y):
    return y * 2

list3 = map(multi, list2)

print(list(list2))


list1 = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, list1))) 


