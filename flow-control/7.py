# Outer loop
 # Inner loop

for x in range(1, 6):
    print(f'Produto {x}')
    for y in range(5):
        print(f'Pruduto {x} - Descrição {y}')


n = 5
for k in range(n):
    for j in range(n):
        print('x' if j + k >= n - 1 else ' ', end='')
    print()