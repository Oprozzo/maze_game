import pygame
import barrier


class Room:  # Class for all rooms

    wall_list = []
    enemy_list = None
    treasure_list = None
    bullet_list = None
    # List for all objects in a room

    def __init__(self):
        # creates our lists
        self.wall_list = pygame.sprite.Group()
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
                    treasure_rect = pygame.Rect(x, y, 20, 20)
                x += 20
            y += 20
            x = 0

# class make_room(Room):
#
#     def __init__(self):
#         super().__init__()
#
#         walls = [[0, 0, 20, 250],  # top left v
#                  [0, 350, 20, 250],  # bottom left v
#
#                  [780, 0, 20, 250],  # top right v
#                  [780, 350, 20, 250],  # bottom right v
#
#                  [0, 0, 350, 20],  # top left h
#                  [450, 0, 350, 20],  # top right h
#
#                  [0, 580, 350, 20],
#                  [450, 580, 350, 20]
#
#                  ]
#
#         for brick in walls:
#             brick = barrier.Wall(brick[0], brick[1], brick[2], brick[3])
#             self.wall_list.add(brick)

