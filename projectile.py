import pygame

blue = (0, 0, 255)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((3, 5))  # Setting the width and height of the bullet

        self.image.fill(blue)  # Assigning the bullet with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x

        self.rect.y = y

        self.direction = direction

        self.speed = 8 * direction
