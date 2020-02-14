import pygame
import random

pygame.init()


resolucao  =(500, 500)

screen = pygame.display.set_mode(resolucao)

preto = (255, 255, 255)


class Snake:
    cor = (0, 0, 0)
    tamanho = (10, 10)
    velocidade = 0.1

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]

        self.direcao  = "direita"

    def blit(self, screen):
        for posicao in self.corpo:
            screen.blit(self.textura, posicao)

    def andar(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        if self.direcao == "direita":
            self.corpo[0] = (x + self.velocidade, y)
        elif self.direcao == "esquerda":
            self.corpo[0] = (x - self.velocidade, y)
        elif self.direcao == "cima":
            self.corpo[0] = (x, y - self.velocidade)
        elif self.direcao == "baixo":
            self.corpo[0] = (x, y + self.velocidade)



class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)




snake  = Snake()
frutinha = Frutinha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    snake.andar()

    screen.fill(preto)
    frutinha.blit(screen)
    snake.blit(screen)

    

    pygame.display.update()