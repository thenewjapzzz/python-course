even_or_odd = lambda num: 'Even' if num % 2 == 0 else 'Odd'
user_number = int(input('Enter a number: '))

print(f'The number {user_number} is {even_or_odd(user_number)}')