countries = {
    'Brazil': 'Brasília',
    'Japan': 'Tokyo',
    'Germany': 'Berlim',
    'Colômbia': 'Bogotá'
}

user_country = input('Enter a country: ')

if user_country in countries:
    print(f'The capital of {user_country} is {countries[user_country]}')
else:
    print('Sorry, we dont have an informations about the capital of this country ')