import pygame
from random import randint

pygame.init()

white = (255,255,255)
blue = (200,200,250)
green = (107,142,35)
red = (255,69,0)
black = (1,1,1)

largura = 640
altura = 480
tamanho = 10


relogio = pygame.time.Clock()

fundo=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('bullet hell')

def player(pos_x,pos_y):
    pygame.draw.rect(fundo,white,[pos_x,pos_y,tamanho,tamanho])

# def item(itemXY):
#     for XY in itemXY:
#         pygame.draw.circle(fundo,green,[XY[0],XY[1]],5)

def jogo():
    sair = True
    velocidade = 3
    pos_x = randint(0,(largura-tamanho)/10)*10
    pos_y = randint(0,(altura-tamanho)/10)*10
    item_x = randint(0,(largura-tamanho)/10)*10
    item_y = randint(0,(altura-tamanho)/10)*10
    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair=False
            print(event)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            pos_x += -velocidade
        if pressed[pygame.K_d]:
            pos_x += velocidade
        if pressed[pygame.K_w]:
            pos_y += -velocidade
        if pressed[pygame.K_s]:
            pos_y += velocidade


        if pos_x >= 640-tamanho:
            pos_x = 640-tamanho
        if pos_x <= 0:
            pos_x = 0
        if pos_y >= 480-tamanho:
            pos_y = 480-tamanho
        if pos_y <= 0:
            pos_y = 0
        fundo.fill(black)
        itemXY = []
        player(pos_x,pos_y)
        # item(item_x,item_y)
        relogio.tick(60)
        pygame.display.update()
#fim def jogo()

jogo()

pygame.quit()
quit()
