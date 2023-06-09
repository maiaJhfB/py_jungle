import pygame
import math
# import Fases

#classe dos botões
class Button1():
    def __init__(self, x, y, largura, altura,pos):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.clicked = False
        self.pos = pos
    def verificar_clique(self):
        action = False
        pos_x,pos_y = pos
        if self.x - (self.largura/2) <= pos_x <= self.x + (self.largura/2) and self.y - (self.altura/2) <= pos_y <= self.y + (self.altura/2): 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
        return action

class Fases():
    def __initt__(self):
        pass
    def ver_fase(self,level,pos):
        botao1 = False
        botao2 = False
        botao3 = False
        botao4 = False
        if level == 21 or level == 25 or level == 31:
            bt1 = Button1(220,547,136,166,pos)
            bt2 = Button1(476,544,132,168,pos)
            bt3 = Button1(359,764,138,172,pos)
            botao1 = bt1.verificar_clique()
            botao2 = bt2.verificar_clique()
            botao3 = bt3.verificar_clique()
            #talves setar aqui o botao4 como falso 
            print(botao1,botao2,botao3)
            return botao1,botao2,botao3
        
pygame.init()
timer = pygame.time.Clock()
#medidas da janela                ------------------- OLhar o minuto final do video para entender como utilizar isto como uma class em outros arquivos(video dos botões)------------------------------
janela_altura = 1000 
janela_largura = 707
tela = []
fonte = pygame.font.Font('imagem/myFont.ttf', 32)
fps = 60
screen = pygame.display.set_mode((janela_largura,janela_altura))
pygame.display.set_caption('teste na aba')
level = 21
tela = (pygame.image.load(f'imagem/{level}.png'))    #usar de base para verificar os diretórios
pontuacao = 0
acerto = 10
erro = 0
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    screen.blit(tela,(0,0))
    pos = pygame.mouse.get_pos()
    fs = Fases()
    if 7 <= level <= 20 or level == 24 or 29<= level <= 30 or 34 <= level <= 36:
        botao1,botao2,botao3,botao4 = fs.ver_fase(level,pos)
    elif level == 21 or level == 25 or level == 31:
        botao1,botao2,botao3 = fs.ver_fase(level,pos)
    elif level == 26:
        botao1,botao2,botao3 = fs.ver_fase(level,pos)
    # print(pos)
    if level == 21:
        if botao1 == True:
           pontuacao = pontuacao + erro
           level = 25
    elif botao2 == True:
        pontuacao = pontuacao + erro
        level = 25
    elif botao3 == True:
        pontuacao = pontuacao + acerto
        level = 25
    
    if level == 25:
        if botao1 == True:
           pontuacao = pontuacao + erro
           level = 31
    elif botao2 == True:
        pontuacao = pontuacao + erro
        level = 31
    elif botao3 == True:
        pontuacao = pontuacao + acerto
        level = 31
    
    if level == 31:
        if botao1 == True:
           pontuacao = pontuacao + erro
           level = 21
    elif botao2 == True:
        pontuacao = pontuacao + erro
        level = 21
    elif botao3 == True:
        pontuacao = pontuacao + acerto
        level = 21
    
    tela = (pygame.image.load(f'imagem/{level}.png'))
    screen.blit(tela,(0,0))
    print(pontuacao)
    
    #if botao1 == True:
        #level += 1
        #tela = (pygame.image.load(f'imagem/{level}.png'))
        #screen.blit(tela,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.update()
pygame.quit()

