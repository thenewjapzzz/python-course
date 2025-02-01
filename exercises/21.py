list1 = [1, 2, 3, 4, 5, 6]
list2 = []

squared = lambda num: num ** 2

for k in list1:
    list2.append(squared(k))

print(list1)
print(list2)