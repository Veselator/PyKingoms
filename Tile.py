import pygame
from random import randint

class Tile:
    def __init__(self, screen, x, y, type, width, building, unit):
        self.is_researched = False
        self.x = x
        self.y = y
        self.type = type
        self.screen = screen
        self.width = width
        self.rect = pygame.Rect((self.x * self.width, self.y * self.width, width, width))
        self.red = randint(22, 25)
        self.green = randint(200, 220)
        self.color = (self.red, self.green, 0)
        self.is_podsvechena = False
        self.building = building
        self.unit = unit
        self.generate_landshaft()
    def generate_landshaft(self):
        if self.type == "grass":
            self.images = [pygame.image.load("images/grass1.png"), pygame.image.load("images/grass1.png"), pygame.image.load("images/grass1.png"), pygame.image.load("images/grass2.png"),
                           pygame.image.load("images/grass3.png"), pygame.image.load("images/grass4.png"), pygame.image.load("images/grass5.png"), pygame.image.load("images/grass6.png"),
                           pygame.image.load("images/grass7.png"), pygame.image.load("images/grass8.png"), pygame.image.load("images/grass9.png"), pygame.image.load("images/grass9.png"),
                           pygame.image.load("images/grass1.png"), pygame.image.load("images/grass1.png"), pygame.image.load("images/grass2.png"), pygame.image.load("images/grass5.png")]
        elif self.type == "sand":
            self.images = [pygame.image.load("images/sand1.png"), pygame.image.load("images/sand2.png"), pygame.image.load("images/sand3.png"), pygame.image.load("images/sand4.png"),
                           pygame.image.load("images/sand5.png"), pygame.image.load("images/sand3.png"), pygame.image.load("images/sand3.png"), pygame.image.load("images/sand2.png")]
        elif self.type == "forest":
            self.images = [pygame.image.load("images/forest1.png"), pygame.image.load("images/forest2.png"), pygame.image.load("images/forest3.png"), pygame.image.load("images/forest4.png"),
                           pygame.image.load("images/forest5.png"), pygame.image.load("images/forest6.png"), pygame.image.load("images/forest2.png"), pygame.image.load("images/forest5.png")]
        elif self.type == "mountain":
            self.images = [pygame.image.load("images/mountain1.png"), pygame.image.load("images/mountain2.png"), pygame.image.load("images/mountain3.png"), pygame.image.load("images/mountain1.png")]
        elif self.type == "village":
            self.images = [pygame.image.load("images/village.png"), pygame.image.load("images/village2.png"), pygame.image.load("images/village3.png"), pygame.image.load("images/village4.png")]
        elif self.type == "reka":
            self.images = [pygame.image.load("images/reka1.png")]
        self.target_image = randint(0, len(self.images) - 1)
        self.tuman_image = pygame.image.load("images/tuman.png")
    def change_landshaft(self, type):
        self.type = type
        self.generate_landshaft()
    def draw(self, x_smesh, y_smesh, mouse_pos):
        self.rect.x += x_smesh
        self.rect.y += y_smesh
        if(-50<=self.rect.x<=860 and -50<=self.rect.y<=860):
            if self.is_researched:
                if self.is_podsvechena and self.rect.collidepoint(mouse_pos): pygame.draw.rect(surface=self.screen, color=(12, 125, 0), rect=self.rect)
                elif self.is_podsvechena: pygame.draw.rect(surface=self.screen, color=(19, 145, 61), rect=self.rect)
                elif self.rect.collidepoint(mouse_pos): pygame.draw.rect(surface=self.screen, color=(10, 190, 10), rect=self.rect)
                else: self.screen.blit(self.images[self.target_image], (self.rect.x, self.rect.y))#pygame.draw.rect(surface=self.screen, color=self.color, rect=self.rect)
            else: self.screen.blit(self.tuman_image, (self.rect.x, self.rect.y))
