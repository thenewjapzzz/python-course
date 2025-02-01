cars = ['BMW X6', 'BMW i5', 'BMW i8']

car = input('Enter a car you want to buy: ')

if car in cars:
    print('This car is available')
else:
    print('This car is not available')