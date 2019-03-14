import pygame
import barrier
import treasure
import enemy

wall_sprite = pygame.sprite.Group()


class Room:  # Class for all rooms

    wall_list = []
    enemy_list = None
    treasure_list = None
    bullet_list = None
    # List for all objects in a room

    def __init__(self):
        # creates our lists
        self.wall_list = wall_sprite
        self.enemy_list = pygame.sprite.Group()
        self.treasure_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

    def make_room(self, level):

        super().__init__()

        level = level
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    self.wall_list.add(barrier.Wall(x, y, 20, 20))
                if col == "T":
                    self.treasure_list.add(treasure.Loot(x, y))
                if col == "R":
                    self.enemy_list.add(enemy.Rival(x, y))
                x += 20
            y += 20
            x = 0



