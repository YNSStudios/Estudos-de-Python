import pygame
import random


# 1. INICIA O PYGAME
# Liga os módulos principais da biblioteca.
pygame.init()


# 2. DEFINE O TAMANHO DA TELA
largura = 800
altura = 600


# 3. CRIA A JANELA DO JOGO
# A janela terá 800 pixels de largura e 600 de altura.
tela = pygame.display.set_mode((largura, altura))


# 4. DEFINE O TÍTULO DA JANELA
pygame.display.set_caption('Jogo da Cobrinha')


# 5. DEFINE ALGUMAS CORES
# As cores são escritas em RGB:
# vermelho, verde e azul.
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)


# 6. DEFINE O TAMANHO DE CADA BLOCO DA COBRA
# Cada parte da cobra terá 20x20 pixels.
tamanho_bloco = 20


# 7. CRIA UM RELÓGIO PARA CONTROLAR A VELOCIDADE DO JOGO
relogio = pygame.time.Clock()


# 8. DEFINE A VELOCIDADE DO JOGO
# Esse número representa quantos ciclos por segundo o jogo tenta executar.
velocidade = 10


# 9. DEFINE A POSIÇÃO INICIAL DA COBRA
# largura // 2 pega o centro horizontal da tela.
# altura // 2 pega o centro vertical da tela.
cobra_x = largura // 2
cobra_y = altura // 2


# 10. DEFINE O MOVIMENTO INICIAL
# Como começa em 0, a cobra fica parada até o jogador apertar uma tecla.
movimento_x = 0
movimento_y = 0


# 11. CRIA A LISTA QUE VAI GUARDAR O CORPO DA COBRA
# Cada item dessa lista será uma posição [x, y].
corpo_cobra = []


# 12. DEFINE O TAMANHO INICIAL DA COBRA
tamanho_cobra = 1


# 13. CRIA UMA POSIÇÃO ALEATÓRIA PARA A COMIDA
# randrange gera valores de 20 em 20.
# Isso mantém a comida alinhada com os blocos da cobra.
comida_x = random.randrange(0, largura, tamanho_bloco)
comida_y = random.randrange(0, altura, tamanho_bloco)


# 14. VARIÁVEL QUE CONTROLA SE O JOGO CONTINUA ABERTO
rodando = True


# 15. LOOP PRINCIPAL DO JOGO
# Enquanto "rodando" for True, o jogo continua funcionando.
while rodando:


    # 16. PEGA TODOS OS EVENTOS
    # Exemplos:
    # apertar tecla
    # clicar
    # fechar janela
    for evento in pygame.event.get():


        # 17. VERIFICA SE O USUÁRIO FECHOU A JANELA
        if evento.type == pygame.QUIT:
            rodando = False


        # 18. VERIFICA SE ALGUMA TECLA FOI PRESSIONADA
        if evento.type == pygame.KEYDOWN:


            # 19. MOVIMENTO PARA A ESQUERDA
            if evento.key == pygame.K_LEFT:

                movimento_x = -tamanho_bloco
                movimento_y = 0


            # 20. MOVIMENTO PARA A DIREITA
            elif evento.key == pygame.K_RIGHT:

                movimento_x = tamanho_bloco
                movimento_y = 0


            # 21. MOVIMENTO PARA CIMA
            elif evento.key == pygame.K_UP:

                movimento_x = 0
                movimento_y = -tamanho_bloco


            # 22. MOVIMENTO PARA BAIXO
            elif evento.key == pygame.K_DOWN:

                movimento_x = 0
                movimento_y = tamanho_bloco


    # 23. ATUALIZA A POSIÇÃO DA COBRA
    # += soma o movimento à posição atual.
    cobra_x += movimento_x
    cobra_y += movimento_y


    # 24. VERIFICA SE A COBRA SAIU DA TELA
    if (
        cobra_x < 0
        or cobra_x >= largura
        or cobra_y < 0
        or cobra_y >= altura
    ):

        rodando = False


    # 25. LIMPA A TELA
    # Pinta tudo de preto antes de desenhar novamente.
    tela.fill(preto)


    # 26. DESENHA A COMIDA
    # pygame.draw.rect desenha um retângulo.
    pygame.draw.rect(
        tela,
        vermelho,
        [comida_x, comida_y, tamanho_bloco, tamanho_bloco]
    )


    # 27. GUARDA A POSIÇÃO ATUAL DA CABEÇA
    cabeca = [cobra_x, cobra_y]


    # 28. ADICIONA A NOVA POSIÇÃO NA LISTA DO CORPO
    corpo_cobra.append(cabeca)


    # 29. REMOVE O EXCESSO DO CORPO
    # Se a lista ficar maior que o tamanho permitido,
    # remove a posição mais antiga.
    if len(corpo_cobra) > tamanho_cobra:

        del corpo_cobra[0]


    # 30. VERIFICA SE A COBRA BATEU NO PRÓPRIO CORPO
    # corpo_cobra[:-1] pega tudo menos a cabeça atual.
    for parte in corpo_cobra[:-1]:

        if parte == cabeca:

            rodando = False


    # 31. DESENHA TODAS AS PARTES DA COBRA
    for parte in corpo_cobra:

        pygame.draw.rect(
            tela,
            verde,
            [parte[0], parte[1], tamanho_bloco, tamanho_bloco]
        )


    # 32. VERIFICA SE A COBRA COMEU A COMIDA
    if cobra_x == comida_x and cobra_y == comida_y:


        # 33. CRIA UMA NOVA POSIÇÃO PARA A COMIDA
        comida_x = random.randrange(
            0,
            largura,
            tamanho_bloco
        )

        comida_y = random.randrange(
            0,
            altura,
            tamanho_bloco
        )


        # 34. AUMENTA O TAMANHO DA COBRA
        tamanho_cobra += 1


    # 35. ATUALIZA O QUE APARECE NA JANELA
    pygame.display.update()


    # 36. CONTROLA A VELOCIDADE DO LOOP
    # Aqui o jogo tenta rodar a 10 ciclos por segundo.
    relogio.tick(velocidade)


# 37. ENCERRA O PYGAME
pygame.quit()