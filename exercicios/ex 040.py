print('Digite [1] para calcular a nota final das unidades e [2] para calcular uma unidade só.')
rumo = int(input('Digite o que você quer fazer: '))
if rumo == 1:
    print('Digite apenas números.')
    unidades = int(input('Sua escola ultiliza 3 ou 4 unidades: '))

    if unidades in [3, 4]:
        notas = []
        for i in range(unidades):
            nota = float(input(f'[{1 + i}] Digite sua nota:'))
            notas.append(nota)

        if unidades == 3:
            if 0 >= sum(notas) <= 10:
                print(f'Sua nota foi de \033[0;31m{sum(notas)}, infelizmente você foi reprovado.\033[0m')

            elif 10.1 <= sum(notas) <= 14:
                print(f'Sua nota foi de \033[0;34m{sum(notas)}, infelizmente você está de recuperação.\033[0m')

            else:
                print(f'Sua nota foi de \033[0;32m{sum(notas)}, parabéns você foi aprovádo.\033[0m')

        else:
            if 0 <= sum(notas) <= 15:
                print(f'Sua nota foi de \033[0;31m{sum(notas)}, infelizmente você foi reprovado.\033[0m')

            elif 15.1 <= sum(notas) <= 19.9:
                print(f'Sua nota foi de \033[0;34m{sum(notas)}, infelizmente você está de recuperação.\033[0m')

            else:
                print(f'Sua nota foi de \033[0;32m{sum(notas)}, parabéns você foi aprovádo.\033[0m')
    else:
        print('\033[0;31mValor inválido, tente novamente.\033[0m')

elif rumo == 2:
    while True:
        prova = float(input('De 0 a 10. Quanto voce tirou na prova: '))
        if 0 <= prova <= 10:
            nota = prova
            break
        else:
            print('\033[0;31mNota inválida.\033[0m')

    while True:        
        trabalho = float(input('De 0 a 10. Digite sua nota do trabalho:'))
        if 0 <= trabalho <= 10:
            nota_trabalho = trabalho
            break

        else:
            print('\033[0;31mNota inválida.\033[0m')

    while True:

        caderno = int(input('De 0 a 5. Quantas atividades você entegou: '))
        if 0 <= caderno <= 5:
            nota_caderno = caderno * 2
            break

        else:
            print('\033[0;31mValor inválido.\033[0m')

    media = (nota + nota_trabalho + nota_caderno) / 3

    print(f'Sua media foi de {media:.2f}.')