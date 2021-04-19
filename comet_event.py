import pygame
from comet import Comet


class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 3200
        self.game = game

        # stockage des comets
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loading(self):
        return self.percent >= 100


    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # relance
        if self.is_full_loading():
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):
        self.add_percent()
        self.attempt_fall()
