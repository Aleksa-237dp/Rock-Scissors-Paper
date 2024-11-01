import pygame as pg

# класс звука

class SoundGame:

    def __init__(self):
        self.background = None
        self.victory = None
        self.start = None

    def play_background(self, background=None):
        if background:
            self.background = pg.mixer.music.load(background)
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(-1)

    def play_victory(self, victory=None):
        if victory:
            self.victory = pg.mixer.Sound(victory)

            self.victory.play()

    def play_start(self, start=None):
        if start:
            self.start = pg.mixer.Sound(start)
            pg.mixer.Sound.set_volume(self.start, 0.4)
            self.start.play()

    def play_choice(self, choice=None):
        if choice:
            self.choice = pg.mixer.Sound(choice)
            self.choice.play()


sound_game = SoundGame()
