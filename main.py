# configurações iniciais
import pygame
import random, time
from pygame.locals import *

# Inicializando
pygame.init()



# Definindo a taxa de atualização da tela
FPS = pygame.time.Clock()

# Definindo variaveis que serão utilizadas no jogo.
delta = 0
pontos, tentativas, controle, vel_jogador = 0, 3, 10, 500
start = True

# Criando a tela, definindo o tamanho e o nome.
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo_teste")

# cores RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definindo as fontes e as informações.
font = pygame.font.SysFont('Verdana', 60)
font_menor = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, BLACK)

# Definindo as imagens do jogo.
imagem_jogador = pygame.image.load("goleiro.png")
imagem_bola = pygame.image.load("bola.png")
imagem_fundo = pygame.image.load("campo.jpg")

# Passando as informações onde o Jogador e a bola será inserido na tela, assim como a hitbox de ambos.
jogador = pygame.Rect((largura / 2, 400), (60, 60))
bola = pygame.Rect((largura / 2, 0), (30, 30))


# Loop infinito para iniciar o jogo.
while start:
    # Verificando se o jogador apertou o X para fechar o jogo.
    for event in pygame.event.get():
        if event.type == QUIT:
            start = False
        
    # Inserindo as informações, jogador e a bola na tela.        
    pontuacao = font_menor.render(str(f'Pontos: {pontos}'), True, BLACK)
    chances = font_menor.render(str(f'Tentativas: {tentativas}'), True, BLACK)
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(pontuacao, (10, 10))
    tela.blit(chances, (450, 10))
    tela.blit(imagem_jogador, jogador)
    tela.blit(imagem_bola, bola)
    
    # Verificando se o jogador pressionou esquerda ou direita.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jogador.x -= vel_jogador * delta
    elif keys[pygame.K_RIGHT]:
        jogador.x += vel_jogador * delta
    
    # Verificando se o jogador conseguiu pegar a bola.
    if jogador.colliderect(bola):
        pontos += 1
        bola.top = 0
        bola.center = random.randint(30, 370), 0
    
    # Gerando nova localização para a bola
    bola.move_ip(0, controle)
    
    # Aumentando a velocidade do jogador e da bola.
    if controle < 20:
        if pontos == controle:
            controle += 1
            vel_jogador += 100

    # Verificando se o jogador deixou a bola passar.
    if bola.bottom > 600:
        tentativas -= 1
        bola.top = 0
        bola.center = random.randint(30, 370), 0
    
    # Informando ao jogador que ele perdeu.
    if tentativas < 1:
        tela.fill(RED)
        tela.blit(game_over, (115, 250))
        
        
    
    pygame.display.flip()

    FPS.tick(30)
    delta = FPS.tick(60) / 1000
pygame.quit()
