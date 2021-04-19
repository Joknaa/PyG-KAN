import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/comet4.png')
        self.image = pygame.transform.scale(self.image, (50, 150))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(20,25)
        self.rect.x = random.randint(20, 700)
        self.rect.y = -50
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity
        # destruction
        if self.rect.y > 500:
            self.remove()

        # comet and player
        if self.comet_event.game.check_colision(self, self.comet_event.game.all_players):
            #sounds

            self.remove()
            self.comet_event.game.player.damage(20)
