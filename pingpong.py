
from pygame import *
from random import *
from time import time as timer 

class GameSprite (sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset (self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite): 
    def update_L(self): #МЕТОД ДЛЯ УПРАВЛЕНИЯ ЛЕВОЙ РАКЕТКОЙ W/S
        keys = key.get_pressed()
        if keys[K_S] and self.rect.x > 5:
            self.rect.Y -= self.speed
        if keys[K_W] and self.rect.x < width - 50:
            self.rect.y += self.speed

    def update_L(self): #МЕТОД ДЛЯ УПРАВЛЕНИЯ ПРАВОЙ РАКЕТКОЙ UP/DOWN
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.x < width - 50:
            self.rect.y += self.speed

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption("Пинг-Понг")
back = (200, 255, 255)
window.fill(back)

game = True
finish = False
FPS = 60
clock = time.Clock()

font.init()
font1 = font.SysFont('Arial', 36)
lose1 = font1.render('Игрок 1 проиграл!', True, (255, 0, 0))
lose2 = font1.render('Игрок 2 проиграл!', True, (255, 0, 0))