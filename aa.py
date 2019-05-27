import pygame
from random import randint

white = (255,255,255)
blue = (30,144,255)
green = (107,142,35)
red = (255,69,0)
black = (1,1,1)

pygame.init()

largura = 640
altura = 480
tamanho = 10
pos_x = randint(0,(largura-tamanho)/10)*10
pos_y = randint(0,(altura-tamanho)/10)*10
velocidade_x = 0
velocidade_y = 0
relogio = pygame.time.Clock()
fundo=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('sanake')
sair = True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade_x = -tamanho
                velocidade_y=0
            if event.key == pygame.K_RIGHT:
                velocidade_x = tamanho
                velocidade_y = 0
            if event.key == pygame.K_UP:
                velocidade_y = -tamanho
                velocidade_x = 0
            if event.key == pygame.K_DOWN:
                velocidade_y = tamanho
                velocidade_x = 0
        print(event)
    if velocidade_x != 0 or velocidade_y != 0:
        if pos_x >= 640-tamanho:
            pos_x = 640-tamanho
        if pos_x <= 0:
            pos_x = 0.1
            velocidade_x = 0
        if pos_y >= 480-tamanho:
            pos_y = 480-tamanho
        if pos_y <= 0:
            pos_y = 0
    fundo.fill(white)
    pygame.draw.rect(fundo,black,[pos_x,pos_y,tamanho,tamanho])
    pos_x += velocidade_x
    pos_y += velocidade_y
    relogio.tick(40)
    pygame.display.update()

pygame.quit()
quit()
