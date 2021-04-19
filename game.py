from player import Player
from comet_event import CometFallEvent
import pygame
import random

# class jeux
class Game:
    def __init__(self):
        # condition du jeux
        self.is_playing = False
        self.is_pause  = False
        self.pause = False
        # generer notre joueur
        self.all_players =  pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer event comet
        self.comet_event = CometFallEvent(self)
       
        self.pressed = {}

    def question(self):
        Question_list = [
                        ["The closest planet", "to the Earth is", " 'Venus' ","planets/8.png"],
                        ["The closest planet", "to the   Sun is", " 'Mercury'","planets/7.png"],
                        ["The period of a rotation"," of the Earth on","  itself is '1day'","planets/1.png"],
                        ["The period of a rotation "," of the Earth on" ," the Sun is '1month'","planets/1.png"],
                        ["The farthest planet"," to the Sun is", "'Neptune'","planets/3.png"],
                        ["There is '9' planets"," in the solar system"," ","planets/1.png"],
                        ["The hottest planet"," in our solar system is"," 'Venus'","planets/8.png"],
                        ["The sun is a 'Star'"," "," ","planets/5.png"],
                        ["The name of the first ","satellite sent into "," space is 'Sputnik'","planets/1.png"],
                        ["The period of a  rotation","of the Moon  on ","itself is '27day'","planets/6.png"],
                        ["The speed of the Earth","in a rotation on ","itself is '120km/h'","planets/1.png"],
                        ["The biggest planet in ","the solar system is ","'Jupite'r","planets/4.png"],
                        ["The speed of the Earth"," in a rotation on ","the Sun is '108000km/h'","planets/1.png"],
                        ["The planet witch was ","included in the solar system ","in 2006 is 'Pluto'","planets/2.png"],        
                        ]
        # random item from list
        qst = random.choice(Question_list)
        
        return qst

        


    def start(self): 
        test = True
        self.pause = False
        self.is_playing=True
        self.is_pause  = False 
        self.player.life == 3  
        pygame.mixer.music.load('sounds/son1.mpeg')
        pygame.mixer.music.play(-1)
     

    def game_over(self):
            self.player.life -= 1
            self.player.health = self.player.max_health
            if   self.player.life == 0:
                self.is_playing = False
                self.player.score = 0
                self.player.life = 3
                pygame.mixer.music.load('sounds/go.mp3')
                pygame.mixer.music.play(0)
            
            
        

    def update(self, screen):
        myfont = pygame.font.SysFont("monospace",36)
       #score
        self.player.score +=1


        #les information
        if self.player.score % 600 == 0:
            self.is_playing = False
            self.is_pause = True
        else:
            self.pause = False
         
        #Life
        text = myfont.render("life : {0}".format(self.player.life), 1, (255,255,255))
        screen.blit(text, (480,0))

        #pour comet fall
        self.comet_event.update_bar(screen)


        #comet fall
        for comet in self.comet_event.all_comets:
            comet.fall()

        # player
        screen.blit(self.player.image, self.player.rect)

        # draw comet
        self.comet_event.all_comets.draw(screen)

        # player mouvement 
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

 

