#Entrada
numero = float(input('Digite um número. (Digite apenas números): '))
valor = float(numero)
if valor >= 1:
    print(f'O número {numero} é positivo.')

elif valor == 0:
    print(f'O 0 é neutro.')

else:
    print(f'O número {numero} é negativo.')