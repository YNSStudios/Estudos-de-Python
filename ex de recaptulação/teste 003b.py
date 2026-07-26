while True:
    nome = input('Qual é o seu nome: ')
    dia = input('Digite o dia em que você nasceu: ')
    verificação = dia.isnumeric()
    if verificação == True:
        nv_dia = int(dia)
        if nv_dia in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]:
            mes = input('Digite o mês em que você nasceu: ')
            ano = input('Digite seu ano de nascimento: ')
            verificação = ano.isnumeric()
            if verificação == True:
                comfirmação = input('Obrigado por participar, seu ano de nascimento é {}, seu mês é {}, do dia {}, correto ? (sim ou não ?)'.format(ano, mes, dia))   
                if comfirmação in ['sim', 's', 'Sim', 'correto', 'certo']:
                    print('obrigado por participar {}'.format(nome)) 
                    break

                else:
                    print('Tente novamente !')
            else:
                print('Isso não é um número !')    
        else:
            print('o dia não está no intervalo de 1 mês !')
    else:
        print('Isso não é um número !')