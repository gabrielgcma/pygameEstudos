from turtle import up
import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

# Janela -----
largura = 640
altura = 480
# ------------

# Sons -----
pygame.mixer.music.set_volume(0.15)
musica_fundo = pygame.mixer.music.load("BoxCat Games - CPU Talk.mp3")
pygame.mixer.music.play(-1) # -1 faz com que a música fique em loop

colisao_barulho = pygame.mixer.Sound("smw_coin.wav") # Todos .Sound() precisam ser .wav
# ----------

# Posição dos elementos -----
x_cobra = int(largura/2)
y_cobra = int(altura/2)

x_maca = randint(40, 600)
y_maca = randint(50, 430)

velocidade = 10
x_controle = velocidade
y_controle = 0
# ---------------------------

# Setup do score -----
fonte = pygame.font.SysFont("couriernew", 20, True, False)
pontos = 0
# --------------------

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_incial = 5
game_over = False

def aumenta_cobra(lista_corpo):
    for par_ordenado in lista_corpo:
        pygame.draw.rect(tela, (0, 255, 0), (par_ordenado[0], par_ordenado[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_incial, x_cobra, y_cobra, lista_corpo, lista_cabeca, x_maca, y_maca, game_over, mensagem
    pontos = 0
    comprimento_incial = 5
    
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_corpo = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    game_over = False
    mensagem = f"Pontos {pontos}"

lista_corpo = []

while True:
    # definir o framerate
    relogio.tick(30)

    # Dar refresh
    tela.fill((255, 255, 255))

    # Score
    mensagem = f"Pontos: {pontos}"
    txt_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Movimentação
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0 
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0 
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
    
    x_cobra += x_controle
    y_cobra += y_controle
            
    # Elementos da tela
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    # Se a cobra colidir com a maca
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        colisao_barulho.play()
        comprimento_incial += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_corpo.append(lista_cabeca)

    if lista_corpo.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = "Game over! Pressione a tecla R para jogar novamente"
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))  
        ret_texto = texto_formatado.get_rect()

        game_over = True
        while game_over:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_corpo) > comprimento_incial:
        del lista_corpo[0]

    aumenta_cobra(lista_corpo)

    # Posicionar o score
    tela.blit(txt_formatado, (450, 20))

    pygame.display.update()

