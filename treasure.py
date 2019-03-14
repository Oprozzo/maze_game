import pygame

yellow = (255, 255, 0)


class Loot(pygame.sprite.Sprite):

    def __init__(self, x, y):  # Constructor function

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((20, 20))  # Setting the width and height of the player

        self.image.fill(yellow)  # Assigning the player with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y