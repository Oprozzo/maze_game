import pygame

purple = (97, 0, 127)


class Rival(pygame.sprite.Sprite):  # Troll class

    def __init__(self, x, y):  # Constructor function

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((40, 40)) # Setting the width and height of the player

        self.image.fill(purple)  # Assigning the player with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y


