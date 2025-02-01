def numx2(number):
    return number * 2

def numsquared(number):
    return numx2(number) ** 2

user_number = int(input('Enter a number: '))

print(f'The squared of twice the number {user_number} is equal to {numsquared(user_number)}')