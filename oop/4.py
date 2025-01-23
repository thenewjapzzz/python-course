class Funcionarios:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

usuario1 = Funcionarios('Guilherme', 'Sato')
usuario2 = Funcionarios('Larsisa', 'Colucci')

print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))  