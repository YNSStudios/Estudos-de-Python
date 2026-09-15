import random

print("\033[0;31m=\033[0;34m=\033[0m" * 14)
print("\033[0;32mJokenpo Computacional\033[0m")
print("\033[0;31m=\033[0;34m=\033[0m" * 14)

print("""Digite apenas o número
[0] Pedra
[1] tesoura
[2] papel
[5] Encerrar
""")

lista = {"pedra": 0, "tesoura": 1, "papel": 2}

lista_vitorias_u = []
lista_vitorias_C = []
lista_empates = []

while True:

    while True:    

        escolha = input("Digite sua escolha: ")
        if escolha.isnumeric():

            escolha = int(escolha)
            break
        elif escolha.isspace():
            print("\033[31mDigite um valor valido\033[0m")

    if escolha in [0, 1, 2]:

        computador = random.randint(0, 2)

        if (
            escolha == lista["pedra"]
            and computador == lista["tesoura"]
            or escolha == lista["papel"]
            and computador == lista["pedra"]
            or escolha == lista["tesoura"]
            and computador == lista["papel"]
        ): 
            print(f"\033[0;32mVocê ganhou !\033[0m")
            lista_vitorias_u.append(1)

        elif (
            computador == lista["pedra"]
            and escolha == lista["tesoura"]
            or computador == lista["papel"]
            and escolha == lista["pedra"]
            or computador == lista["tesoura"]
            and escolha == lista["papel"]
        ):
            print(f"\033[0;31mComputador ganhou !\033[0m")
            lista_vitorias_C.append(1)

        elif escolha == computador:

            print(f"\033[0;33mDeu empate !\033[0m")
            lista_empates.append(1)

        else:
            print("\033[0;31mResultado inválido, tente novamente ! \033[0m")

    elif escolha == 5:
        print(
            f"Você ganhou {sum(lista_vitorias_u)} e o computador {sum(lista_vitorias_C)} e deu empate {sum(lista_empates)}"
        )
        break

    else:
        print("\033[0;31mResultado inválido, tente novamente ! \033[0m")
