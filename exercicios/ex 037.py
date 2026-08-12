numero = int(input('Digite um número: '))
print('''Você quer convertelo em: 
[1] Binário
[2] Octal
[3] Hexadecimal
Digite apenas o número.
''')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    print(bin(numero))

elif escolha == 2: 
    print(oct(numero))

elif escolha == 3:
    print(hex(numero))

else:
    print('\033[0;31;40mEscolha inválida !\033[0m')