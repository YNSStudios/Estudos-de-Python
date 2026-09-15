from time import sleep

soma = 0
contaguem = 0

for i in range(1, 500, 2):

    if i % 3 == 0:

        soma += i
        contaguem += 1
        
print(f'A soma de todos os números é: {soma}, e a contaguem deles são {contaguem}.')