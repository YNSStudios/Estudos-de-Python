import random 
numero = random.randint(1, 5)
valor = int(input('Tente acertar o número. (o intervalo é de 1 a 5): '))
if valor == numero:
    print('Você acertou, parabéns !')

else:
    print('O computador venceu !')