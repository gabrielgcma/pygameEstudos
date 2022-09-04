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
# ---------------------------

# Setup do score -----
fonte = pygame.font.SysFont("couriernew", 20, True, False)
pontos = 0
# --------------------

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

def aumenta_cobra(lista_corpo):
    for par_ordenado in lista_corpo:
        pygame.draw.rect(tela, (0, 255, 0), (par_ordenado[0], par_ordenado[1], 20, 20))

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
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20
            
    # Elementos da tela
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    # Se a cobra colidir com a maca
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        colisao_barulho.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_corpo.append(lista_cabeca)

    aumenta_cobra(lista_corpo)

    # Posicionar o score
    tela.blit(txt_formatado, (450, 20))

    pygame.display.update()

