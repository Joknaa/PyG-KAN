import pygame
from animation import AnimateSprite

# class joueur
class Player(AnimateSprite):

    def __init__(self, game):
        super().__init__("astro")
        self.game = game
        self.life = 3
        self.health = 100
        self.max_health = 100
        self.score = 0
        self.veloity = 20
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


    def damage(self, value):
        #5 fois == -1 vie
        if self.health - value >0:
            self.health -= value
        else:
            self.game.game_over()


    def move_right(self):
             self.rect.x += self.veloity

    def move_left(self):
        self.rect.x -= self.veloity

 