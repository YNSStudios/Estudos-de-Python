numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))
numero_3 = float(input('Digite mais um número: '))

menor = numero_1

if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
    print(f'O menor número é: {menor}')

elif numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3
    print(f'O menor número é: {menor}')

else:
    print(f'O menor número é: {menor}')