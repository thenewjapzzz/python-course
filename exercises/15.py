def pot(x, y=2):
    return x ** y

x = int(input('Enter the base number: '))
y = (input('Enter the exponent number: '))

if y:
    print(f'The result of the power is {pot(x, int(y))}')
else:
    print(f'The result of the power is {pot(x)}')