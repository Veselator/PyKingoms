import pygame

class Castle:
    def __init__(self, width, screen, parent):
        self.width = width
        self.image = pygame.image.load("images/castle.png")
        self.screen = screen
        self.parent = parent
        self.x_restangle = self.parent.x * self.width
        self.y_restangle = self.parent.y * self.width
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, width, width))
        self.type = "castle"
    def draw(self, x_smeshenie, y_smeshenie):
        self.x_restangle += x_smeshenie
        self.y_restangle += y_smeshenie
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        if(-50<=self.x_restangle<=860 and -50<=self.y_restangle<=860): self.screen.blit(self.image, (self.x_restangle, self.y_restangle))

class Lesopilnya:
    def __init__(self, width, screen, parent):
        self.width = width
        self.image = pygame.image.load("images/lesopilnya.png")
        self.screen = screen
        self.parent = parent
        self.x_restangle = self.parent.x * self.width
        self.y_restangle = self.parent.y * self.width
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, width, width))
        self.type = "lesopilnya"
    def draw(self, x_smeshenie, y_smeshenie):
        self.x_restangle += x_smeshenie
        self.y_restangle += y_smeshenie
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        if(-50<=self.x_restangle<=860 and -50<=self.y_restangle<=860): self.screen.blit(self.image, (self.x_restangle, self.y_restangle))

class House:
    def __init__(self, width, screen, parent):
        self.width = width
        self.image = pygame.image.load("images/house.png")
        self.screen = screen
        self.parent = parent
        self.x_restangle = self.parent.x * self.width
        self.y_restangle = self.parent.y * self.width
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, width, width))
        self.type = "house"
    def draw(self, x_smeshenie, y_smeshenie):
        self.x_restangle += x_smeshenie
        self.y_restangle += y_smeshenie
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        if(-50<=self.x_restangle<=860 and -50<=self.y_restangle<=860): self.screen.blit(self.image, (self.x_restangle, self.y_restangle))

class Melnitsa:
    def __init__(self, width, screen, parent):
        self.width = width
        self.images = [pygame.image.load("images/melnitsa2.png"), pygame.image.load("images/melnitsa3.png")]
        self.target_image = 0
        self.tick = 0
        self.screen = screen
        self.parent = parent
        self.x_restangle = self.parent.x * self.width
        self.y_restangle = self.parent.y * self.width
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, width, width))
        self.type = "house"
    def draw(self, x_smeshenie, y_smeshenie):
        self.x_restangle += x_smeshenie
        self.y_restangle += y_smeshenie
        self.rect = pygame.Rect((self.x_restangle, self.y_restangle, self.width, self.width))
        if(-50<=self.x_restangle<=860 and -50<=self.y_restangle<=860):
            self.tick += 0.05
            if self.tick >= 2:
                self.tick = 0
            self.screen.blit(self.images[int(self.tick)], (self.x_restangle, self.y_restangle))
