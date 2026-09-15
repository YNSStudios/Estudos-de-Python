import random

print("\033[0;31m=\033[0;34m=\033[0m" * 14)
print("\033[0;32mJokenpo Computacional\033[0m")
print("\033[0;31m=\033[0;34m=\033[0m" * 14)

print("""Digite apenas o número
Pedra
papel
Tesoura
""")

lista = ["pedra", "papel", "tesoura"]

escolha = input("Esolha: ").lower()
pc_escolha = random.choice(lista)
combinações = {"pedra" > "tesoura", "tesoura" > "papel", "papel" > "pedra"}
if escolha in lista:
    if pc_escolha > escolha:
        status = f"\033[0;31m{pc_escolha}, o computador ganhou !\033[0m"
    elif escolha > pc_escolha:
        status = f"\033[0;32mParabéns, você ganhou ! {pc_escolha}.\033[0m"
    else:
        status = f"{pc_escolha}, deu empate."

    print(status)

else:
    print("\033[0;31mEscolha inválida, tente novamente mais tarde.\033[0m")
