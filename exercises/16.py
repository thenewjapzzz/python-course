def fat(n):
    if n <= 1: return 1
    return n * fat(n - 1)

user_number = int(input('Enter a number: '))
print(f'The fatorial of {user_number} is equl {fat(user_number)}')