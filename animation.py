import pygame

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images  = animations.get(sprite_name)
        self.animation = False
    # def methode poyur demarer anilatiuon
    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1 # iamge suivant
            # vifier si on attein la fin
            if self.current_image >= len(self.images):
                self.current_image=0
                if loop is False:
                    self.animation= False
            # modifier limage prec par la suivante
            self.image = self.images[self.current_image]



# un fonction pour charger les image d'un sprite
def load_animation_images(sprite_name):
    # charge de l'image
    images = []
    # recupere le dossier des images
    path = f"assets/{sprite_name}/{sprite_name}"
    #boucler dans ce dosier
    for num in range(1,24):
        image_path = f"{path}{num}.png"
        images.append(pygame.image.load(image_path))
    # revoyer le contenu de la liste d'image
    return images

# dictionaire d'image pour chaque sprite
# mummy -> [....] no images

animations = {}