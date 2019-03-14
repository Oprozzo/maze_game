import pygame

blue = (0, 0, 255)

bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((15, 10))  # Setting the width and height of the bullet

        self.image.fill(blue)  # Assigning the bullet with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x

        self.rect.y = y

        # self.direction = direction

        self.speed = 6

    def update(self):

        self.rect.x += self.speed

        if self.rect.left > 800:
            self.kill()

    # def collision(self, sprite1, sprite2):
    #     col = pygame.sprite.collide_rect(sprite1, sprite2)
    #
    #     if col == True:
    #         self.kill()