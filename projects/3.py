'''
Criar um programa que gere 3 listas de acordo com a necessidade 
logo abaixo:

lista1 = funcionários que tem carro e trabalham de noite
lista2 = funcionários que tem carrro e trabalham durante o dia
lista3 = funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro) & set(turno_noite) # intersection
lista2 = set(tem_carro) & set(turno_dia) # intersection
lista3 = set(funcionarios) - set(tem_carro) # difference

print(list(lista1))
print(list(lista2))
print(list(lista3))