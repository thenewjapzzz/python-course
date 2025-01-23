class Funcionarios:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

usuario1 = Funcionarios('Guilherme', 'Sato')
usuario2 = Funcionarios('Larsisa', 'Colucci')

print(usuario1.nome, usuario1.sobrenome)
print(usuario2.nome, usuario2.sobrenome)