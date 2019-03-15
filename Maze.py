import pygame

white = (255, 255, 255)
red = (255, 0, 0)
purple = (97, 0, 127)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)


class Player(pygame.sprite.Sprite):  # Player class

    move_x = 0
    move_y = 0

    def __init__(self, x, y):  # Constructor function

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((40, 40))  # Setting the width and height of the player

        self.image.fill(red)  # Assigning the player with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y

        self.gold = 0

    def movement(self, x, y):
        self.move_x += x
        self.move_y += y

    def move(self, walls):
        # Move player

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

    def shoot(self):

        bullet = Bullet(self.rect.centerx, self.rect.centery)

        all_sprites.add(bullet)

        bullets_sprite.add(bullet)


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((width, height))  # Setting the width and height of the wall

        self.image.fill(white)  # Assigning the wall with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y


class Room(pygame.sprite.Sprite):  # Class for all rooms

    def make_room(self, level):

        super().__init__()

        level = level
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    wall_sprite.add(Wall(x, y, 20, 20))
                    all_sprites.add(wall_sprite)
                if col == "T":
                    treasure_sprite.add(Loot(x, y))
                    all_sprites.add(treasure_sprite)
                if col == "R":
                    enemy_sprite.add(Rival(x, y))
                    all_sprites.add(enemy_sprite)
                x += 20
            y += 20
            x = 0


class Rival(pygame.sprite.Sprite):  # Troll class

    def __init__(self, x, y):  # Constructor function

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((40, 40)) # Setting the width and height of the player

        self.image.fill(purple)  # Assigning the player with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y


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
    #     if col:
    #         self.kill()


class Loot(pygame.sprite.Sprite):

    def __init__(self, x, y):  # Constructor function

        super().__init__()  # Calling the parent constructor

        self.image = pygame.Surface((20, 20))  # Setting the width and height of the player

        self.image.fill(yellow)  # Assigning the player with a colour

        self.rect = self.image.get_rect()  # Gets the rectangular area of the surface

        self.rect.x = x
        self.rect.y = y


class Check:
    def __init__(self, file, output):
        file = open(file)
        output = output
        lines = file.readlines()
        count = len(lines)
        if count == 30:
            for char in lines:
                if len(char) <= 41:
                    output.append(char)


player_sprite = pygame.sprite.Group()
bullets_sprite = pygame.sprite.Group()
wall_sprite = pygame.sprite.Group()
treasure_sprite = pygame.sprite.Group()
enemy_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


def main():
    # This is the main function of the game

    pygame.init()  # This is to initialise pygame

    screen_width = 800  # Assigns the width of the game
    screen_height = 600  # Assigns the height of the game

    gamedisplay = pygame.display.set_mode([screen_width, screen_height])
    # Creates the window of the sizes specified above

    level = []

    Check("Rooms.txt", level)

    player = Player(50, 50)
    player_sprite.add(player)
    player_speed = 4
    clock = pygame.time.Clock()

    key_up = pygame.K_UP
    key_down = pygame.K_DOWN
    key_left = pygame.K_LEFT
    key_right = pygame.K_RIGHT
    key_shoot = pygame.K_SPACE
    key_coin = pygame.K_c

    all_sprites.add(player)

    rooms = []
    room = Room()
    Room.make_room(room, level)
    rooms.append(room)

    end = False

    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == key_left:
                    player.movement(-player_speed, 0)
                if event.key == key_right:
                    player.movement(player_speed, 0)
                if event.key == key_up:
                    player.movement(0, -player_speed)
                if event.key == key_down:
                    player.movement(0, player_speed)
                if event.key == key_shoot:
                    Player.shoot(player)
                if event.key == key_coin:
                    if player.gold > 0:
                        player.gold -= 1
                        treasure_sprite.add(Loot(player.rect.x+60, player.rect.y+10))
                        all_sprites.add(treasure_sprite)

            if event.type == pygame.KEYUP:
                if event.key == key_left:
                    player.movement(player_speed, 0)
                if event.key == key_right:
                    player.movement(-player_speed, 0)
                if event.key == key_up:
                    player.movement(0, player_speed)
                if event.key == key_down:
                    player.movement(0, -player_speed)

        player.move(wall_sprite)

        blocks_hit_treasure_list = pygame.sprite.spritecollide(player, treasure_sprite, True)
        if blocks_hit_treasure_list:
            player.gold += 1
            print(player.gold)

        blocks_hit_list = pygame.sprite.groupcollide(wall_sprite, bullets_sprite, False, True)
        blocks_hit_list = pygame.sprite.groupcollide(bullets_sprite, enemy_sprite, False, True)

        all_sprites.update()
        gamedisplay.fill(black)
        all_sprites.draw(gamedisplay)
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()