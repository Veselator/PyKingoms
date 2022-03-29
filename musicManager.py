import pygame

pygame.init()

class MusicManager:
    def __init__(self):
        self.hodba_sound = pygame.mixer.Sound('musics/hodba.mp3')
        pygame.mixer.music.set_volume(0.5)
        self.fonovaya_music = pygame.mixer.Sound('musics/fonovaya.mp3')
        self.fonovaya_music.play()
        self.zapret = pygame.mixer.Sound('musics/zapret.mp3')
        self.razgovor = pygame.mixer.Sound('musics/razgovorTEST.mp3')
        self.create_unit = pygame.mixer.Sound('musics/sozdanie_unita.mp3')
        self.stroyka = pygame.mixer.Sound('musics/stroyka.mp3')
        self.monetu = pygame.mixer.Sound('musics/monetu.mp3')
        self.swim = pygame.mixer.Sound('musics/swim.mp3')
