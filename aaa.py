import pygame
from random import randint
from datetime import datetime
pygame.init()

white = (255,255,255)
blue = (0,0,250)
green = (0, 250, 0)# (107,142,35)
red = (255,69,0)
black = (1,1,1)
orange = (255,110,0)

largura = 640
altura = 480
tamanho = 10
raio_bala = 10
velocidade = 3
fps=60




tempo_inicio = (datetime.now().minute,datetime.now().second)
relogio = pygame.time.Clock()

fundo=pygame.display.set_mode((largura,altura))



def player(pos_x,pos_y,valor_vida):
    pygame.draw.rect(fundo,blue,[pos_x,pos_y,tamanho,tamanho])
# fim def player()

def balas(matriz_balas,limite_balas):
    for i in range(limite_balas):
        lista_balas=[]
        area_bala_x = randint(1,3)
        area_bala_y = randint(1,3)
        if area_bala_x == 1:
            bala_x = randint(0-(raio_bala*2),0)
        elif area_bala_x == 2:
            bala_x = randint(640,640+(raio_bala*2))
        else:
            if area_bala_y == 1 or area_bala_y == 2:
                bala_x = randint(0,640)
        if area_bala_y == 1:
            bala_y = randint(0-(raio_bala*2),0)
        elif area_bala_y == 2:
            bala_y = randint(480,480+(raio_bala*2))
        else:
            if area_bala_x == 1 or area_bala_x ==2:
                bala_y = randint(0,480)
        if area_bala_x == 3 and area_bala_y == 3:
            continue
        # bala_x = randint(0,640)
        # bala_y = randint(0,480)
        if bala_x <= 0:
            velocidade_bala_x = randint(1,3)
        elif bala_x >= 640:
            velocidade_bala_x = randint(-3,1)
        else:
            velocidade_bala_x = randint(-3,3)
        if bala_y <= 0:
            velocidade_bala_y = randint(1,3)
        elif bala_y >= 480:
            velocidade_bala_y = randint(-3,1)
        else:
            velocidade_bala_y = randint(-3,3)

        lista_balas.append(bala_x)
        lista_balas.append(bala_y)
        lista_balas.append(velocidade_bala_x)
        lista_balas.append(velocidade_bala_y)
        matriz_balas.append(lista_balas)
    limite_balas = 0
    return limite_balas
# fim def balas()

def vida(valor_vida):
    vida_x = 10
    vida_y = 10
    for  i in range(valor_vida):
        pygame.draw.rect(fundo,red,[vida_x + 15*i,vida_y,tamanho,tamanho])
# fim def vida()

def game_over(tempo_inicio):
    tempo_final = (datetime.now().minute,datetime.now().second)
    minuto_final = tempo_final[0] - tempo_inicio[0]
    segundo_final = tempo_final[1] - tempo_inicio[1]
    if segundo_final < 0:
        segundo_final += 60
        minuto_final -= 1
    fundo.fill(black)
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    label = myfont.render('game over',1,white)
    label2 = myfont.render('tempo {0:02}:{1:02}'.format(minuto_final,segundo_final),1,white)
    fundo.blit(label, (40,100))
    fundo.blit(label2, (40,200))
    pygame.display.flip()
    a=0
    while True:
        a+=1
        print(a)
        teclas = pygame.key.get_pressed()
        print(teclas)
        sair = False
        pygame.quit()
        quit()

 # or pressed[pygame.K_f]

def jogo():
    sair = True
    pos_x = randint(0,(largura-tamanho)/10)*10
    pos_y = randint(0,(altura-tamanho)/10)*10
    valor_vida=8
    matriz_balas=[]
    limite_balas=10



    while sair:
        pygame.display.set_caption('bullet hell % d ' % relogio.get_fps())

        if valor_vida < 1:
            game_over(tempo_inicio)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    valor_vida += 4
                if event.key == pygame.K_f:
                    valor_vida = 0
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
        if pressed[pygame.K_LSHIFT]:
            velocidade = 1
        else:
            velocidade = 3

        if pos_x >= 640-tamanho:
            pos_x = randint(0,(largura-tamanho)/10)*10
            pos_y = randint(0,(altura-tamanho)/10)*10
            valor_vida -= 1
        if pos_x <= 0:
            pos_x = randint(0,(largura-tamanho)/10)*10
            pos_y = randint(0,(altura-tamanho)/10)*10
            valor_vida -= 1
        if pos_y >= 480-tamanho:
            pos_x = randint(0,(largura-tamanho)/10)*10
            pos_y = randint(0,(altura-tamanho)/10)*10
            valor_vida -= 1
        if pos_y <= 0:
            pos_x = randint(0,(largura-tamanho)/10)*10
            pos_y = randint(0,(altura-tamanho)/10)*10
            valor_vida -= 1

        fundo.fill(white)



        if valor_vida>=1:
            player(pos_x,pos_y,valor_vida,)
        if limite_balas > 0:
            balas(matriz_balas,limite_balas)
        if len(matriz_balas) <= 25:
            limite_balas = 50
        else:
            limite_balas = 0

        print(len(matriz_balas))

        contador = 0
        for i in matriz_balas:
            pygame.draw.circle(fundo,orange,(i[0],i[1]),raio_bala)
            if i[2] == 0 and i[3] == 0:
                i[2] = randint(-3,3)
                i[3] = randint(-3,3)
            i[0] += i[2]
            i[1] += i[3]
            if i[0] < -10 or i[0] > 650:
                del matriz_balas[contador]
            elif i[1] < -10 or i[1] > 490:
                del matriz_balas[contador]
            if (pos_x + tamanho >= i[0] >=  pos_x and pos_y + tamanho >= i[1] >= pos_y) or (pos_x + tamanho >= i[0] + raio_bala >=  pos_x and pos_y + tamanho >= i[1] >= pos_y) or (pos_x + tamanho >= i[0] - raio_bala >=  pos_x and pos_y + tamanho >= i[1] >= pos_y) or (pos_x + tamanho >= i[0] >=  pos_x and pos_y + tamanho >= i[1] + raio_bala >= pos_y) or (pos_x + tamanho >= i[0] >=  pos_x and pos_y + tamanho >= i[1] - raio_bala >= pos_y):
                del matriz_balas[contador]
                valor_vida -= 1
            contador += 1

        vida(valor_vida)
        relogio.tick(fps)
        pygame.display.update()
#fim def jogo()

jogo()


pygame.quit()
quit()
