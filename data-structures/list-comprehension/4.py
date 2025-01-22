from sys import getsizeof

nunmeros = [x * 10 for x in range(100)]
print(type(nunmeros))
print(getsizeof(nunmeros))

print()

numeros = (x * 10 for x in range(100))
print(type(numeros))
print(getsizeof(numeros))