cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']

# adiciona um item ao fim da lista
cidades.append('Jacareí')
print(cidades)

# remove o item desejado 
cidades.remove('Rio de Janeiro')
print(cidades)

# insere a cidade no index desejado
cidades.insert(1, 'São José dos Campos')
print(cidades)

# remove o item da posição desejada
cidades.pop(0)
print(cidades)

# ordena em ordem alfabética
cidades.sort()
print(cidades)