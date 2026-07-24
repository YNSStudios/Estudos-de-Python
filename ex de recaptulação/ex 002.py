#Entrada
numero = str(input('Digite um número. (Digite apenas números): '))
comfirmacao = numero.isnumeric()
if comfirmacao == True:
    valor = float(numero)
    if valor >= 1:
        print(f'O número {numero} é positivo.')

    elif valor == 0:
        print(f'O 0 é neutro.')

else:
    print(f'o número {numero} é negativo')