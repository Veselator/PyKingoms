import pygame

class Worker:
    def __init__(self, screen, parent, width, x, y):
        self.x = x
        self.y = y
        self.parent = parent
        self.screen = screen
        self.width = width
        self.x_restangle = self.parent.rect.x
        self.y_restangle = self.parent.rect.y
        self.image1 = pygame.image.load("images/workers1.png")
        self.image2 = pygame.image.load("images/workers2.png")
        self.currentSprite = 0
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        self.move_points = 2
        self.start_move_points = self.move_points
        self.type = "worker"
        self.boat = pygame.image.load("images/lodka.png")
    def draw(self, x_smeshenie, y_smeshenie):
        self.x_restangle += x_smeshenie
        self.y_restangle += y_smeshenie
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        if (-50 <= self.x_restangle <= 860 and -50 <= self.y_restangle <= 860):
            if self.parent.type == "reka": self.screen.blit(self.boat, (self.x_restangle, self.y_restangle))
            if self.move_points > 0: self.currentSprite += 0.03
            if self.currentSprite < 1:
                self.screen.blit(self.image1, (self.x_restangle, self.y_restangle))
            elif self.currentSprite >= 2:
                self.currentSprite = 0
                self.screen.blit(self.image1, (self.x_restangle, self.y_restangle))
            else: self.screen.blit(self.image2, (self.x_restangle, self.y_restangle))

class Skaut:
    def __init__(self, screen, parent, width, x, y):
        self.x = x
        self.y = y
        self.parent = parent
        self.screen = screen
        self.width = width
        self.x_restangle = self.parent.rect.x
        self.y_restangle = self.parent.rect.y
        self.image1 = pygame.image.load("images/skaut1.png")
        self.image2 = pygame.image.load("images/skaut2.png")
        self.currentSprite = 0
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        self.move_points = 4
        self.start_move_points = self.move_points
        self.type = "skaut"
    def draw(self, x_smeshenie, y_smeshenie):
        self.x_restangle += x_smeshenie
        self.y_restangle += y_smeshenie
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        if (-50 <= self.x_restangle <= 860 and -50 <= self.y_restangle <= 860):
            if self.move_points > 0: self.currentSprite += 0.03
            if self.currentSprite < 1:
                self.screen.blit(self.image1, (self.x_restangle, self.y_restangle))
            elif self.currentSprite >= 2:
                self.currentSprite = 0
                self.screen.blit(self.image1, (self.x_restangle, self.y_restangle))
            else: self.screen.blit(self.image2, (self.x_restangle, self.y_restangle))