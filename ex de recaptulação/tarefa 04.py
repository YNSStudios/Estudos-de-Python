ano_atual = 2026

print("\033[1mDigite apenas seu nome\033[0m")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
ano = int(input("Digite o ano do seu nascimento: "))

idade = ano_atual - ano

print(
    "\033[1mDigite uma senha forte, ela deve conter no minimo uma letra maiuscula e 8 números, e não pode conter seu nome nela. \033[1;31mNão adicione caracteres especiais.\033[0m"
)

senha = input("Digite sua senha: ")

tem_numero = senha.isalnum()
sem_nome = nome.lower() in senha.lower()
tem_8digitos = len(senha) >= 8

if tem_numero == True and sem_nome == False and tem_8digitos == True:
    comfirmacao = input("Comfirme sua senha: ")

    if comfirmacao == senha:
        print("\033[1;32mSenha criada com sucesso!\033[0m")
        
        if idade <= 17:
            status = "\033[0;31mAcesso Restrito - Usuário Menor de Idade\033[0m"

        elif 18 >= idade <= 64:
            status = "\033[0;32mAcesso Total - Usuário Adulto\033[0m"

        elif idade >= 65:
            status = "\0330;32mAcesso Total - Usuário Sênior\033[0m"

        else:
            print("\033[1;31;40mInválido !\033[0m")

        print("=-" * 8)
        print("Análise do usuário.")
        print("=-" * 8)
        print(f"Nome: {nome.strip().capitalize()} {sobrenome.strip().title()}")
        print(f"Status da conta: {status}")
        print(f"""Informações adicionais: 
Número de letras no nome completo: {len(nome.replace(' ', '')) + len(sobrenome.replace(' ', ''))}
Contém "Silva" no nome: {'Sim' if 'silva' in sobrenome.lower() else 'Não'}
Idade: {idade}
""")

    else:
        print("\033[31mSenha Fraca ou Inválida!\033[0m")

else:
    print("\033[31mSenha Fraca ou Inválida!\033[0m")
