import random 

lista_de_alunos = []

while True:
    print('Digite apenas números !')
    alunos = input('Quantos alunos você quer cadastrar: ')
    verificacao = alunos.isnumeric()
    if verificacao == True:

        valor = int(alunos)
        for i in range(valor):
            nome = input(f'Qual o nome do aluno {i + 1}: ')
            lista_de_alunos.append(nome)

        entrada = input('Como você quer receber. 1-Mostrar todos os alunos, 2-Sortear um aluno, 3-Encerrar: ')

        fixo = 1

        sorteio = random.choice(lista_de_alunos)

        while True:
            if entrada.capitalize() in ['1',  'Mostrar todos os alunos', 'mostrar']:
                        for i in range(fixo):
                            print(lista_de_alunos)
                        break
            
            elif entrada.capitalize() in ['2',  'Sortear um aluno', 'sortear'] :
                print(f'O aluno escolhido foi: {sorteio}. ')
                break
    
            elif entrada.capitalize() in ['3', 'Encerrar'] :
                print('Cadastro encerrado com sucesso !')
                break
    
            else:
                print('Valos inválido !')

    else:
        print('Isso não é um número !')