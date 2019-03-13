import pygame
import chamber
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):  # Player class

    move_x = 0
    move_y = 0

    def __init__(self, x, y):  # Constructor function

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((40, 40)) # Setting the width and height of the player

        self.image.fill(red)  # Assigning the player with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y

        self.gold = 0

        self.bullets = 0

    def movement(self, x, y):
        self.move_x += x
        self.move_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.move_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.move_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.move_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.move_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
