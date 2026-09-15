ano_atual = 2026

print("\033[1m=== CADASTRO DE USUÁRIO ===\033[0m")
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
ano = int(input("Digite o ano do seu nascimento: "))
idade = ano_atual - ano

print(
    "\033[1mDigite uma senha forte (mínimo 8 caracteres, sem seu nome e apenas letras/números).\033[0m"
)
senha = input("Digite sua senha: ")

# Validações da senha
tem_numero = senha.isalnum()
tem_nome = nome.lower() in senha.lower()  # True se O NOME ESTIVER na senha
tem_8digitos = len(senha) >= 8

# Valida se é alfanumérica, se NÃO tem o nome e se tem 8+ dígitos
if tem_numero and not tem_nome and tem_8digitos:
    confirmacao = input("Confirme sua senha: ")

    if confirmacao == senha:
        print("\033[1;32mSenha criada com sucesso!\033[0m")

        # Análise de Idade Corrigida
        if idade < 18:
            status = "\033[0;31mAcesso Restrito - Usuário Menor de Idade\033[0m"
        elif 18 <= idade <= 64:
            status = "\033[0;32mAcesso Total - Usuário Adulto\033[0m"
        else:  # Qualquer idade a partir de 65
            status = "\033[0;32mAcesso Total - Usuário Sênior\033[0m"

        # Nome completo para checagem de Silva
        nome_completo = f"{nome} {sobrenome}".strip()

        print("=-" * 12)
        print("    Análise do Usuário")
        print("=-" * 12)
        print(f"Nome: {nome.strip().capitalize()} {sobrenome.strip().title()}")
        print(f"Status da conta: {status}")
        print(f"""Informações adicionais: 
Número de letras no nome completo: {len(nome_completo.replace(" ", ""))}
Contém "Silva" no nome: {'Sim' if 'silva' in nome_completo.lower() else 'Não'}
Idade: {idade} anos
""")
    else:
        print("\033[31mAs senhas não coincidem!\033[0m")
else:
    print(
        "\033[31mSenha Fraca ou Inválida! Não atende aos requisitos de segurança.\033[0m"
    )
