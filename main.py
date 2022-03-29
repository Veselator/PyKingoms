import pygame.image

from Settings import *
from Tile import *
from Buildings import *
from Units import *
from musicManager import *
from time import sleep
import threading

pygame.init()
pygame.font.init()

setup = Settings()

top_bar_image = pygame.image.load("images/topBar.png")
money_icon = pygame.image.load("images/money.png")
man_icon = pygame.image.load("images/man.png")
wood_icon = pygame.image.load("images/wood.png")
stone_icon = pygame.image.load("images/stone.png")
food_icon = pygame.image.load("images/food_icon.png")
pixel_font = pygame.font.Font("fonts/ds-pixel-cyr.ttf", 50)
pixel_font_small = pygame.font.Font("fonts/pixel-cyr-normal.ttf", 18)
infos1 = ["Свежий ветер дует.", "Рабочие идут по полю.", "Рабочие идут", "Колонна рабочих", "Колонна рабочих", "Группа рабочих", "Группа скаутов", "Скауты"]
infos2 = ["Солнце ярко светит.", "Они счастливы.", "на работу.", "шагает на работу", "шагает на работу", "вышла из замка.", "вышла из замка.", "исследуют местность."]

def draw_topbar(window, money, man, wood, stone, hod, food, info, target_unit):
    window.blit(top_bar_image, (0, -80))

    window.blit(money_icon, (10, 10))
    window.blit(man_icon, (10, 90))

    window.blit(wood_icon, (210, 10))
    window.blit(stone_icon, (210, 90))
    window.blit(food_icon, (400, 90))

    money_text = pixel_font.render(str(money), True, (0, 0, 0))
    man_text = pixel_font.render(str(man), True, (0, 0, 0))
    wood_text = pixel_font.render(str(wood), True, (0, 0, 0))
    stone_text = pixel_font.render(str(stone), True, (0, 0, 0))
    hod_text = pixel_font.render("Ход " + str(hod), True, (0, 0, 0))
    food_text = pixel_font.render(str(food), True, (0, 0, 0))
    next_hod_text1 = pixel_font_small.render("Нажмите пробел", True, (0, 0, 0))
    next_hod_text2 = pixel_font_small.render("для следующего хода.", True, (0, 0, 0))
    info_text1 = pixel_font_small.render(infos1[info], True, (0, 0, 0))
    info_text2 = pixel_font_small.render(infos2[info], True, (0, 0, 0))
    if target_unit != None: od_text = pixel_font_small.render(f"Од: {target_unit.move_points}", True, (0, 0, 0))


    window.blit(money_text, (70, 10))
    window.blit(man_text, (70, 90))
    window.blit(wood_text, (270, 10))
    window.blit(stone_text, (270, 90))
    window.blit(hod_text, (400, 10))
    window.blit(food_text, (460, 90))
    window.blit(next_hod_text1, (570, 10))
    window.blit(next_hod_text2, (570, 30))
    window.blit(info_text1, (570, 90))
    window.blit(info_text2, (570, 110))
    if target_unit != None: window.blit(od_text, (5, 170))
can_next_move = True

money = setup.START_MONEY
man = setup.START_PEOPLE
stone = setup.START_STONE
wood = setup.START_WOOD
food = setup.START_FOOD
hod = 1
info = 0
draw_next_move_text = False

def next_move(units, buildings, window):
    global money
    global man
    global stone
    global wood
    global hod
    global food
    global info
    if units != None:
        for unit in units:
            unit.move_points = unit.start_move_points
            if unit.type == "worker": food -= 5
            elif unit.type == "skaut": food -= 2.5
    if buildings != None:
        for building in buildings:
            if building.type == "castle": money += 20
            elif building.type == "lesopilnya":
                money -= 5
                wood += 5
            elif building.type == "house":
                wood -= 2.5
            elif building.type == "melnitsa":
                food += 10
    move_thread = threading.Thread(target=reload_next_move)
    move_thread.start()

def move_position(tile, target_unit):
    #Неудачная попытка сделать плавное перемещение
    #start_x_pos = target_unit.x_restangle
    #start_y_pos = target_unit.y_restangle
    #target_unit.parent.unit = "none"
    #target_unit.move_right()
    #time.sleep(1)
    #target_unit.move_right()
    #time.sleep(1)
    #target_unit.x_restangle = start_x_pos
    #target_unit.y_restangle = start_y_pos
    target_unit.x = tile.x
    target_unit.y = tile.y
    target_unit.parent.unit = "none"
    tile.unit = target_unit.type
    target_unit.parent = tile

    target_unit.x_restangle = tile.rect.x
    target_unit.y_restangle = tile.rect.y

    target_unit.move_points -= 1

def reload_next_move():
    global can_next_move
    global draw_next_move_text
    draw_next_move_text = True
    sleep(0.5)
    draw_next_move_text = False
    sleep(1)
    can_next_move = True

def generate_river(tiles, setup):
    print("Generate rivers...")
    reka_y = randint(5, setup.GENERATION_WIDTH - 2)
    for x in range(0, setup.GENERATION_WIDTH):
        try:
            tiles[reka_y][x].change_landshaft("reka")
        except:
            break
        try:
            if randint(0, 100) <= 10 and reka_y != setup.GENERATION_WIDTH and reka_y != 6:
                reka_y += 1
                tiles[reka_y][x].change_landshaft("reka")
            elif randint(0, 100) <= 10 and reka_y != 0 and reka_y != 8:
                reka_y -= 1
                tiles[reka_y][x].change_landshaft("reka")
            elif randint(0, 100) <= 10 and reka_y != 0:
                for q in range(0, randint(2, 5)):
                    try:
                        if reka_y != 6:
                            reka_y += 1
                            tiles[reka_y][x].change_landshaft("reka")
                    except:
                        break
            elif randint(0, 100) <= 10 and reka_y != setup.GENERATION_WIDTH:
                for q in range(0, randint(2, 5)):
                    try:
                        if reka_y != 8:
                            reka_y -= 1
                            tiles[reka_y][x].change_landshaft("reka")
                    except:
                        break
        except:
            break

        if randint(0, 100) <= 10 and x != 0 and x != setup.GENERATION_WIDTH and x != 7:
            new_x = x
            for y in range(0, reka_y):
                try:
                    tiles[y][new_x].change_landshaft("reka")
                except:
                    break
                if randint(0, 100) <= 10 and new_x != 3 and new_x != setup.GENERATION_WIDTH:
                    new_x += 1
                    tiles[y][x].change_landshaft("reka")
                elif randint(0, 100) <= 10 and new_x != 5 and new_x != 0:
                    new_x -= 1
                    tiles[y][x].change_landshaft("reka")
                elif randint(0, 100) <= 10 and reka_y != 0:
                    for q in range(0, randint(2, 5)):
                        try:
                            if new_x != 3:
                                new_x += 1
                                tiles[reka_y][new_x].change_landshaft("reka")
                        except:
                            break
                elif randint(0, 100) <= 10 and reka_y != setup.GENERATION_WIDTH:
                    for q in range(0, randint(2, 5)):
                        try:
                            if new_x != 5:
                                new_x -= 1
                                tiles[reka_y][new_x].change_landshaft("reka")
                        except:
                            break
            if reka_y == 4:
                reka_y += 1
                tiles[reka_y][x].change_landshaft("reka")
    for y in range(1, setup.GENERATION_WIDTH - 1):
        for x in range(1, setup.GENERATION_WIDTH - 1):
            if tiles[y][x].type != "reka" and \
                    (tiles[y - 1][x].type == "reka" or tiles[y + 1][x].type == "reka" or
                     tiles[y][x - 1].type == "reka" or tiles[y][x + 1].type == "reka" or
                     tiles[y - 1][x - 1].type == "reka" or tiles[y - 1][x + 1].type == "reka" or
                     tiles[y + 1][x - 1].type == "reka" or tiles[y + 1][x + 1].type == "reka"):
                tiles[y][x].change_landshaft("sand")
    if tiles[4][7].type == "reka": tiles[4][7].change_landshaft("grass")
    if tiles[5][7].type == "reka": tiles[5][7].change_landshaft("grass")

def check_na_podsvetku(tile, target_unit):
    if tile.building == "none" and tile.unit == "none" and (tile.type != "reka" or (target_unit.type == "worker" or target_unit.type == "skaut")): tile.is_podsvechena = True
    else: tile.is_podsvechena = False

def main():
    global money
    global man
    global stone
    global wood
    global hod
    global food
    global info
    global can_next_move
    global draw_next_move_text

    running = True
    pygame.init()
    pygame.font.init()
    setup = Settings()

    window = pygame.display.set_mode(setup.WINDOW_SIZE) #Это screen
    pygame.display.set_caption(setup.WINDOW_TITLE)
    window.fill(setup.BG_COLOR)
    clock = pygame.time.Clock()
    tiles = []
    #Генерация карты
    for y in range(0, setup.GENERATION_WIDTH):
        target_tiles = []
        for x in range(0, setup.GENERATION_WIDTH):
            if x == 7 and y == 4: tile = Tile(window, x, y, "grass", setup.TILE_WIDTH, "castle", "none")
            elif x == 7 and y == 5: tile = Tile(window, x, y, "grass", setup.TILE_WIDTH, "castle", "worker")
            elif y == 0 or x == 0 or y == setup.GENERATION_WIDTH - 1 or x == setup.GENERATION_WIDTH - 1: tile = Tile(window, x, y, "sand", setup.TILE_WIDTH, "none", "none")
            else:
                if randint(0, 1000) <= setup.SAND_FACTOR and (y==20 or y==1 or (x==1 or x==20)): tile = Tile(window, x, y, "sand", setup.TILE_WIDTH, "none", "none")
                elif randint(0, 1000) <= setup.FOREST_FACTOR: tile = Tile(window, x, y, "forest", setup.TILE_WIDTH, "none", "none")
                elif randint(0, 1000) <= setup.MOUNTAIN_FACTOR: tile = Tile(window, x, y, "mountain", setup.TILE_WIDTH, "none", "none")
                elif randint(0, 1000) <= setup.VILLAGE_FACTOR: tile = Tile(window, x, y, "village", setup.TILE_WIDTH, "none", "none")
                else: tile = Tile(window, x, y, "grass", setup.TILE_WIDTH, "none", "none")
            target_tiles.append(tile)
        tiles.append(target_tiles)

    #Генерация рек
    a = randint(0, 100)
    if a <= 80:
        generate_river(tiles, setup)
        if a <= 20:
            generate_river(tiles, setup)
            if a <= 5:
                generate_river(tiles, setup)
                if a == 1:
                    generate_river(tiles, setup)

                #Изучение области вокруг замка
    for y in range(2, 7):
        for x in range(5, 10):
            tiles[y][x].is_researched = True

    smeshenie_x = 0
    smeshenie_y = 0
    buildings = []
    units = []

    #Нужно для обнаружения колизий с курсором
    worker_button_rect = pygame.Rect((20, 620, 154, 62))
    skaut_button_rect = pygame.Rect((200, 620, 154, 62))
    lesopilnya_button_rect = pygame.Rect((20, 620, 154, 62))
    back_button_rect = pygame.Rect((775, 610, 20, 20))
    house_button_rect = pygame.Rect((200, 620, 154, 62))
    melnitsa_button_rect = pygame.Rect((380, 620, 154, 62))
    # Моя вундервафля по рендеру кнопок
    spawn_unit_buttons = [[pygame.image.load("images/work_button.png"), pygame.image.load("images/work_button2.png"), pygame.Rect((20, 620, 154, 62))],
                          [pygame.image.load("images/skaut_button.png"), pygame.image.load("images/skaut_button2.png"), pygame.Rect((200, 620, 154, 62))],
                          [pygame.image.load("images/back.png"), pygame.image.load("images/back2.png"), pygame.Rect((775, 610, 20, 20))]]
    buildings_buttons = [[pygame.image.load("images/lesopilnya_button.png"), pygame.image.load("images/lesopilnya_button2.png"), pygame.Rect((20, 620, 154, 62))],
                         [pygame.image.load("images/house_button.png"), pygame.image.load("images/house_button2.png"), pygame.Rect((200, 620, 154, 62))],
                         [pygame.image.load("images/melnitsa_button.png"), pygame.image.load("images/melnitsa_button2.png"), pygame.Rect((380, 620, 154, 62))],
                         [pygame.image.load("images/back.png"), pygame.image.load("images/back2.png"), pygame.Rect((775, 610, 20, 20))]]

    start_castle = Castle(setup.TILE_WIDTH, window, tiles[4][7])
    start_unit = Worker(window, tiles[5][7], setup.TILE_WIDTH, tiles[5][7].x, tiles[5][7].y)
    units.append(start_unit)
    buildings.append(start_castle)
    menu_open = False
    building_menu_open = False
    target_unit = None

    target_castle = None

    pygame.mouse.set_visible(False)
    cursor_image = pygame.image.load("images/cursor.png")

    music_manager = MusicManager()
    next_move_text = pixel_font_small.render("Следующий ход", True, (0, 0, 0))
    by_text = pixel_font_small.render("By VESELATOR", True, (0, 0, 0))
    pashakla_image = pygame.image.load("images/pashalka.png")
    #Главный цикл
    while running:
        clock.tick(setup.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                #Куча говнокода по пермещению юнитов и нажатию на кнопки
                clicked_buildings = [s for s in buildings if s.rect.collidepoint(pygame.mouse.get_pos())]
                clicked_units = [s for s in units if s.rect.collidepoint(pygame.mouse.get_pos())]
                clicked_tiles = []
                for s in tiles:
                    for d in s:
                        if d.rect.collidepoint(pygame.mouse.get_pos()): clicked_tiles.append(d)
                try:
                    if(clicked_buildings[0] != None):
                        if clicked_buildings[0].type == "castle":
                            menu_open = not(menu_open)
                            if menu_open:
                                target_castle = clicked_buildings[0]
                                music_manager.razgovor.play()
                            else: target_castle = None
                except:
                    pass
                try:
                    if(clicked_units[0] != None):
                        if clicked_units[0] == target_unit:
                            tiles[target_unit.y - 1][target_unit.x].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x].is_podsvechena = False
                            tiles[target_unit.y][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y][target_unit.x + 1].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x + 1].is_podsvechena = False
                            tiles[target_unit.y - 1][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y - 1][target_unit.x + 1].is_podsvechena = False
                            if target_unit.type == "worker": building_menu_open = False
                            target_unit = None
                        elif clicked_units[0].move_points > 0 and target_unit == None:
                            target_unit = clicked_units[0]
                            if target_unit.type == "worker": building_menu_open = True
                        else:
                            tiles[target_unit.y - 1][target_unit.x].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x].is_podsvechena = False
                            tiles[target_unit.y][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y][target_unit.x + 1].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x + 1].is_podsvechena = False
                            tiles[target_unit.y - 1][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y - 1][target_unit.x + 1].is_podsvechena = False
                            target_unit = clicked_units[0]
                            if target_unit.type == "worker": building_menu_open = True
                except:
                    pass
                try:
                    if(clicked_tiles[0] != None):
                        #print(clicked_tiles[0].x, clicked_tiles[0].y)
                        if clicked_tiles[0].is_podsvechena == True:
                            tiles[target_unit.y - 1][target_unit.x].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x].is_podsvechena = False
                            tiles[target_unit.y][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y][target_unit.x + 1].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y + 1][target_unit.x + 1].is_podsvechena = False
                            tiles[target_unit.y - 1][target_unit.x - 1].is_podsvechena = False
                            tiles[target_unit.y - 1][target_unit.x + 1].is_podsvechena = False

                            move_position(clicked_tiles[0], target_unit)

                            tiles[target_unit.y - 1][target_unit.x].is_researched = True
                            tiles[target_unit.y + 1][target_unit.x].is_researched = True
                            tiles[target_unit.y][target_unit.x - 1].is_researched = True
                            tiles[target_unit.y][target_unit.x + 1].is_researched = True
                            tiles[target_unit.y + 1][target_unit.x - 1].is_researched = True
                            tiles[target_unit.y + 1][target_unit.x + 1].is_researched = True
                            tiles[target_unit.y - 1][target_unit.x - 1].is_researched = True
                            tiles[target_unit.y - 1][target_unit.x + 1].is_researched = True
                            if target_unit.type == "worker":
                                info = randint(1, 4)
                                building_menu_open = False
                            elif target_unit.type == "skaut": info = 7
                            #Колонизируем дикую деревню
                            if clicked_tiles[0].type == "village":
                                clicked_tiles[0].change_landshaft("grass")
                                money += 5
                                food += 10
                                wood += 10
                                stone += 10
                                man += 5
                                music_manager.monetu.play()
                            #При заходе на гору радиус обзора увеличивается
                            if clicked_tiles[0].type == "mountain":
                                for y in range(target_unit.y - 2, target_unit.y + 3):
                                    for x in range(target_unit.x - 2, target_unit.x + 3):
                                        tiles[y][x].is_researched = True
                            target_unit = None
                            if clicked_tiles[0].type != "reka": music_manager.hodba_sound.play()
                            else: music_manager.swim.play()
                except:
                    pass
                #Проверка нажатий кнопок
                if worker_button_rect.collidepoint(pygame.mouse.get_pos()) and menu_open:
                    if money > 39 and man > 29:
                        money -= 40
                        man -= 30
                        new_worker = Worker(window, tiles[target_castle.parent.y+1][target_castle.parent.x], setup.TILE_WIDTH, tiles[target_castle.parent.y+1][target_castle.parent.x].x, tiles[target_castle.parent.y+1][target_castle.parent.x].y)
                        units.append(new_worker)
                        menu_open = not (menu_open)
                        music_manager.create_unit.play()
                        info = 5
                    else:
                        music_manager.zapret.play()
                if skaut_button_rect.collidepoint(pygame.mouse.get_pos()) and menu_open:
                    if money > 24 and man > 19:
                        money -= 25
                        man -= 20
                        new_skaut = Skaut(window, tiles[target_castle.parent.y+1][target_castle.parent.x], setup.TILE_WIDTH, tiles[target_castle.parent.y+1][target_castle.parent.x].x, tiles[target_castle.parent.y+1][target_castle.parent.x].y)
                        units.append(new_skaut)
                        menu_open = not (menu_open)
                        music_manager.create_unit.play()
                        info = 6
                    else:
                        music_manager.zapret.play()
                if lesopilnya_button_rect.collidepoint(pygame.mouse.get_pos()) and building_menu_open:
                    if money > 14 and target_unit.parent.type == "forest":
                        money -= 15
                        new_lesopilnya = Lesopilnya(setup.TILE_WIDTH, window, target_unit.parent)
                        new_lesopilnya.x_restangle = target_unit.parent.rect.x
                        new_lesopilnya.y_restangle = target_unit.parent.rect.y
                        units.remove(target_unit)
                        tiles[target_unit.y - 1][target_unit.x].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y - 1][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y - 1][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x].building = "lesopilnya"
                        building_menu_open = False
                        target_unit = None
                        buildings.append(new_lesopilnya)
                        music_manager.stroyka.play()
                    else: music_manager.zapret.play()
                if house_button_rect.collidepoint(pygame.mouse.get_pos()) and building_menu_open:
                    if money > 24 and wood > 9:
                        money -= 25
                        wood -= 10
                        man += 40
                        new_house = House(setup.TILE_WIDTH, window, target_unit.parent)
                        new_house.x_restangle = target_unit.parent.rect.x
                        new_house.y_restangle = target_unit.parent.rect.y
                        units.remove(target_unit)
                        tiles[target_unit.y - 1][target_unit.x].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y - 1][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y - 1][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x].building = "house"
                        building_menu_open = False
                        target_unit = None
                        buildings.append(new_house)
                        music_manager.stroyka.play()
                    else: music_manager.zapret.play()
                if  melnitsa_button_rect.collidepoint(pygame.mouse.get_pos()) and building_menu_open:
                    if wood > 19 and stone > 9:
                        wood -= 20
                        stone -= 10

                        new_melnitsa = Melnitsa(setup.TILE_WIDTH, window, target_unit.parent)
                        new_melnitsa.x_restangle = target_unit.parent.rect.x
                        new_melnitsa.y_restangle = target_unit.parent.rect.y

                        units.remove(target_unit)
                        tiles[target_unit.y - 1][target_unit.x].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y + 1][target_unit.x + 1].is_podsvechena = False
                        tiles[target_unit.y - 1][target_unit.x - 1].is_podsvechena = False
                        tiles[target_unit.y - 1][target_unit.x + 1].is_podsvechena = False

                        tiles[target_unit.y][target_unit.x].building = "melnitsa"
                        building_menu_open = False
                        target_unit = None
                        buildings.append(new_melnitsa)
                        music_manager.stroyka.play()
                    else: music_manager.zapret.play()
                if back_button_rect.collidepoint(pygame.mouse.get_pos()) and (building_menu_open or menu_open):
                    building_menu_open = False
                    menu_open = False

        #Проверка нажатий
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            smeshenie_x = -setup.SPEED_PROKRUTKI
            smeshenie_y = 0
        elif keys[pygame.K_a]:
            smeshenie_x = setup.SPEED_PROKRUTKI
            smeshenie_y = 0
        elif keys[pygame.K_w]:
            smeshenie_x = 0
            smeshenie_y = setup.SPEED_PROKRUTKI
        elif keys[pygame.K_s]:
            smeshenie_x = 0
            smeshenie_y = -setup.SPEED_PROKRUTKI
        else:
            smeshenie_x = 0
            smeshenie_y = 0
        if keys[pygame.K_SPACE] and can_next_move:
            can_next_move = False
            next_move(units, buildings, window)
            hod+=1

        window.fill(setup.BG_COLOR)

        #Рендер
        for i in tiles:
            for j in i:
                j.draw(smeshenie_x, smeshenie_y, pygame.mouse.get_pos())
        for i in buildings: i.draw(smeshenie_x, smeshenie_y)
        for i in units: i.draw(smeshenie_x, smeshenie_y)
        if menu_open:
            pygame.draw.rect(window, (145, 145, 145), (0, 600, 800, 200))
            for button in spawn_unit_buttons:
                if button[2].collidepoint(pygame.mouse.get_pos()): window.blit(button[1], (button[2].x, button[2].y))
                else: window.blit(button[0], (button[2].x, button[2].y))
        if building_menu_open:
            pygame.draw.rect(window, (145, 145, 145), (0, 600, 800, 200))
            for button in buildings_buttons:
                if button[2].collidepoint(pygame.mouse.get_pos()): window.blit(button[1], (button[2].x, button[2].y))
                else: window.blit(button[0], (button[2].x, button[2].y))

        if target_unit != None:
            check_na_podsvetku(tiles[target_unit.y - 1][target_unit.x], target_unit)
            check_na_podsvetku(tiles[target_unit.y - 1][target_unit.x + 1], target_unit)
            check_na_podsvetku(tiles[target_unit.y - 1][target_unit.x - 1], target_unit)

            check_na_podsvetku(tiles[target_unit.y][target_unit.x + 1], target_unit)
            check_na_podsvetku(tiles[target_unit.y][target_unit.x - 1], target_unit)
            check_na_podsvetku(tiles[target_unit.y][target_unit.x], target_unit)

            check_na_podsvetku(tiles[target_unit.y + 1][target_unit.x], target_unit)
            check_na_podsvetku(tiles[target_unit.y + 1][target_unit.x - 1], target_unit)
            check_na_podsvetku(tiles[target_unit.y + 1][target_unit.x + 1], target_unit)
            '''
            if tiles[target_unit.y - 1][target_unit.x].building == "none" and tiles[target_unit.y - 1][target_unit.x].unit == "none" and (tiles[target_unit.y - 1][target_unit.x].type != "reka" or (target_unit.type == "worker" and tiles[target_unit.y - 1][target_unit.x].type == "reka")): tiles[target_unit.y - 1][
                target_unit.x].is_podsvechena = True
            if tiles[target_unit.y + 1][target_unit.x].building == "none" and tiles[target_unit.y + 1][target_unit.x].unit == "none": tiles[target_unit.y + 1][
                target_unit.x].is_podsvechena = True
            if tiles[target_unit.y][target_unit.x - 1].building == "none" and tiles[target_unit.y][target_unit.x - 1].unit == "none": tiles[target_unit.y][
                target_unit.x - 1].is_podsvechena = True
            if tiles[target_unit.y][target_unit.x + 1].building == "none" and tiles[target_unit.y][target_unit.x + 1].unit == "none": tiles[target_unit.y][
                target_unit.x + 1].is_podsvechena = True
            if tiles[target_unit.y + 1][target_unit.x - 1].building == "none" and tiles[target_unit.y + 1][target_unit.x - 1].unit == "none": tiles[target_unit.y + 1][
                target_unit.x - 1].is_podsvechena = True
            if tiles[target_unit.y + 1][target_unit.x + 1].building == "none" and tiles[target_unit.y + 1][target_unit.x + 1].unit == "none": tiles[target_unit.y + 1][
                target_unit.x + 1].is_podsvechena = True
            if tiles[target_unit.y - 1][target_unit.x - 1].building == "none" and tiles[target_unit.y - 1][target_unit.x - 1].unit == "none": tiles[target_unit.y - 1][
                target_unit.x - 1].is_podsvechena = True
            if tiles[target_unit.y - 1][target_unit.x + 1].building == "none" and tiles[target_unit.y - 1][target_unit.x + 1].unit == "none": tiles[target_unit.y - 1][
                target_unit.x + 1].is_podsvechena = True
            '''

        if tiles[0][0].rect.y > 1000: window.blit(pashakla_image, (tiles[0][0].rect.x, tiles[0][0].rect.y - 1600))

        #рисуем Topbar
        draw_topbar(window, money, man, wood, stone, hod, food, info, target_unit)
        if draw_next_move_text: window.blit(next_move_text, (300, 400))
        window.blit(by_text, (5, 780))
        window.blit(cursor_image, pygame.mouse.get_pos())
        pygame.display.flip()
    #Running = True - выходим из цикла - выключаем программу
    pygame.quit()

if __name__ == "__main__":
    main()
