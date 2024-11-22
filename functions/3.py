# Parâmetro --> Argumento
# Default -> aquele que você define o valor no parâmetro, deve estar sempre no final
# Non-default -> não define o valor no parâmetro

def boas_vindas(quantidade, nome='Guilherme'):
    print(f'Olá, {nome}!')
    print(f'Temos {str(quantidade)} laptops no disponíveis.')

boas_vindas(5)