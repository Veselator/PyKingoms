import pygame
import main
from Settings import *

pygame.init()
pygame.font.init()
pixel_font = pygame.font.Font("fonts/pixel-cyr-normal.ttf", 18)
pixel_font_big = pygame.font.Font("fonts/ds-pixel-cyr.ttf", 100)
class Fake_tile:
    def __init__(self, x, y, speed, window, images):
        self.is_animated = False
        self.x = x
        self.y = y
        self.speed = speed
        self.window = window
        self.images = images
        self.target_image = main.randint(0, len(self.images)-1)
        self.tick = 0
        if main.randint(0, 100) == 1: self.target_building = pygame.image.load("images/castle.png")
        elif main.randint(0, 60) == 14:
            self.target_animation = [pygame.image.load("images/workers1.png"), pygame.image.load("images/workers2.png")]
            self.target_building = pygame.image.load(f"images/workers{main.randint(1, 2)}.png")
            self.tick = 0
            self.tick_speed = 0.02
            self.is_animated = True
        elif main.randint(0, 60) == 16:
            self.target_animation = [pygame.image.load("images/melnitsa2.png"), pygame.image.load("images/melnitsa3.png")]
            self.target_building = pygame.image.load(f"images/melnitsa{main.randint(1, 1)}.png")
            self.tick = 0
            self.tick_speed = 0.05
            self.is_animated = True
        elif main.randint(0, 1000) <= 13: self.target_building = pygame.image.load("images/house.png")
        elif main.randint(0, 1000) <= 12: self.target_building = pygame.image.load("images/lesopilnya.png")
        else:
            self.target_building = None
    def draw(self):
        self.y += self.speed
        if self.y >= 800: self.y = -50
        self.window.blit(self.images[self.target_image], (self.x, self.y))
        if self.target_building != None:
            if self.is_animated:
                self.tick += self.tick_speed
                if self.tick >= len(self.target_animation):
                    self.tick = 0
                self.target_building = self.target_animation[int(self.tick) - 1]
            self.window.blit(self.target_building, (self.x, self.y))

def main_menu():
    play_button = [pygame.image.load("images/play_button.png"), pygame.image.load("images/play_button2.png" ), pygame.Rect((300, 300, 154, 62))]
    settings_button = [pygame.image.load("images/settings_button.png"), pygame.image.load("images/settings_button2.png" ), pygame.Rect((300, 400, 154, 62))]
    exit_button = [pygame.image.load("images/exit_button.png"), pygame.image.load("images/exit_button2.png" ), pygame.Rect((300, 500, 154, 62))]
    buttons = [play_button, settings_button, exit_button]
    running = True
    play = False
    speed = 1
    setup = Settings()
    window = pygame.display.set_mode(setup.WINDOW_SIZE)
    window.fill(setup.BG_COLOR)
    pygame.display.set_caption(setup.WINDOW_TITLE)
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(False)
    cursor_image = pygame.image.load("images/cursor.png")

    tiles = []
    for y in range(0, 17):
        target_line = []
        for x in range(0, 17):
            if main.randint(0, 1000) <= setup.FOREST_FACTOR: tile = Fake_tile((x - 1) * 50, (y-1) * 50, speed, window, [pygame.image.load("images/forest1.png"), pygame.image.load("images/forest2.png"), pygame.image.load("images/forest3.png"), pygame.image.load("images/forest4.png"),
                                                                pygame.image.load("images/forest5.png"), pygame.image.load("images/forest6.png"), pygame.image.load("images/forest2.png"), pygame.image.load("images/forest5.png")])
            elif main.randint(0, 1000) <= setup.MOUNTAIN_FACTOR: tile = Fake_tile((x - 1) * 50, (y-1) * 50, speed, window, [pygame.image.load("images/mountain1.png"), pygame.image.load("images/mountain2.png"), pygame.image.load("images/mountain3.png"), pygame.image.load("images/mountain1.png")])
            elif main.randint(0, 1000) <= setup.VILLAGE_FACTOR: tile = Fake_tile((x - 1) * 50, (y-1) * 50, speed, window, [pygame.image.load("images/village.png"), pygame.image.load("images/village2.png"), pygame.image.load("images/village3.png"), pygame.image.load("images/village4.png")])
            else: tile = Fake_tile((x - 1) * 50, (y-1) * 50, speed, window, [pygame.image.load("images/grass1.png"), pygame.image.load("images/grass1.png"), pygame.image.load("images/grass1.png"), pygame.image.load("images/grass2.png"),
                           pygame.image.load("images/grass3.png"), pygame.image.load("images/grass4.png"), pygame.image.load("images/grass5.png"), pygame.image.load("images/grass6.png"),
                           pygame.image.load("images/grass7.png"), pygame.image.load("images/grass8.png"), pygame.image.load("images/grass9.png"), pygame.image.load("images/grass9.png"),
                           pygame.image.load("images/grass1.png"), pygame.image.load("images/grass1.png"), pygame.image.load("images/grass2.png"), pygame.image.load("images/grass5.png")])
            target_line.append(tile)
        tiles.append(target_line)
    is_loading = False

    logo_x = 136
    logo_y = 101
    text = ["P", "y", "Kingdoms"]
    text_color = [(0, 4, 255), (255, 251, 0), (145, 145, 145)]
    by_text = pixel_font.render("By VESELATOR", True, (0, 0, 0))
    while running and not(play):
        clock.tick(setup.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button[2].collidepoint(pygame.mouse.get_pos()):
                    play = True
                elif exit_button[2].collidepoint(pygame.mouse.get_pos()):
                    running = False
        window.fill(setup.BG_COLOR)
        for line in tiles:
            for tile in line:
                tile.draw()
        for button in buttons:
            if button[2].collidepoint(pygame.mouse.get_pos()): window.blit(button[1], (button[2].x, button[2].y))
            else: window.blit(button[0], (button[2].x, button[2].y))

        for i in range(0, len(text)):
            logo_text = pixel_font_big.render(text[i], True, text_color[i])
            logo_fon = pixel_font_big.render(text[i], True, (0, 0, 0))
            window.blit(logo_fon, (logo_x + i * 50 + 4, logo_y + 4))
            window.blit(logo_text, (logo_x + i * 50, logo_y))

        window.blit(by_text, (5, 780))
        window.blit(cursor_image, pygame.mouse.get_pos())
        pygame.display.flip()
    if not(running): pygame.quit()
    else:
        load_text = pixel_font.render("ЗАГРУЗКА...", True, (0, 0, 0))
        window.blit(load_text, (350, 400))
        pygame.display.flip()
        main.main()


if __name__ == "__main__":
    main_menu()