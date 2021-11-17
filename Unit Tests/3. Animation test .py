import os
import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 720, 480
BACKROUND_COLOR = pygame.Color('black')

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock

def load_images(path):
    '''
    Loads all imgaes in the directory. The directory must only contain images

    Args:
         path: The relative or absolute path to the directory to load the images
         from.
    Returns:
        list of images.
     '''
    images[]
    for file_name in os.listdir(spaceinvadersU):
        image = pygame.imageload(spaceinvadersU + os.sep + animationTst1.png)
        images.append(image)
        return images
class AnimatedSprite (pygame.sprtie.Sprite):
    def__init__(self, position, images)
    super(AnimatedSprite, self).__init__()

    size (10,7)

    self.rect = pygame.Rect(position, size)
    self.
