nu = int(input('Digite um número inteiro de 0 a 9999: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print('''Seu número tem: {} unidades
tem: {} Dezenas
tem: {} Centenas
e tem: {} Milhares '''.format(u, d, c, m))