'''
Criar um programa que dependendo da temperatura (em celcius) do
steak ele retornará o ponto de cozimento em porguguês. O usuário
deverá fornecer a temperatura

120° -> 48° - Rare (selada)
130° -> 54° - Medium rare (ao ponto para mal)
140° -> 60° - Medium (ao ponto)
150° -> 65° - Medium wll (ao ponto para mais)
160° -> 71° - Well done (bem passada)
'''

temperatura = int(input('Qual a temperatura da carne: '))

if temperatura < 48:
    print('cozinhar por mais alguns minutos')
elif temperatura >= 48 and temperatura < 54:
    print('selada')
elif temperatura >= 54 and temperatura < 60:
    print('ao ponto para mal')
elif temperatura >= 60 and temperatura < 65:
    print('ao ponto')
elif temperatura >= 65 and temperatura < 71:
    print('ao ponto para mais')
elif temperatura >= 71 and temperatura < 100:
    print('bem passada')
else:
    print('carne queimada')