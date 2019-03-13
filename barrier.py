import pygame

white = (255, 255, 255)


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((width, height))  # Setting the width and height of the wall

        self.image.fill(white)  # Assigning the wall with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y

