numero = float(input('Digite um número: '))
numero_1 = float(input('Digite um número: '))

if numero < numero_1:
    status = f'{numero_1} é maior.'
elif numero_1 < numero:
    status = f'{numero} é maior.'
else:
    status = 'Os números são iguais.'

print(status)