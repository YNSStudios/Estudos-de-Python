import random 
lista = [] 
valor = int(input('Digite quantos nomes você tem. (digite apenas numeto ex: 1, 2, etc..) ')) 
for i in range(valor): 
    nome = str(input(f'Digite o nome do aluno {i+1}: ')) 
    lista.append(nome) 

print(f'O nome dos alunos são {lista}.')