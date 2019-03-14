import pygame
import character
import chamber
import projectile

black = (0, 0, 0)

level = [
"WWWWWWWWWWWWWWW          WWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                              R       W",
"W                                      W",
"W                                      W",
"W                                      W",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                      T                 ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"WWWWWWWWWWWWWWW          WWWWWWWWWWWWWWW"
]

def main():
    # This is the main function of the game

    pygame.init()  # This is to initialise pygame

    screen_width = 1000  # Assigns the width of the game
    screen_height = 600  # Assigns the height of the game

    gamedisplay = pygame.display.set_mode([screen_width, screen_height])
    # Creates the window of the sizes specified above

    player = character.Player(50, 50)
    character.player_sprite.add(player)
    player_speed = 4
    clock = pygame.time.Clock()

    key_up = pygame.K_UP
    key_down = pygame.K_DOWN
    key_left = pygame.K_LEFT
    key_right = pygame.K_RIGHT


    rooms = []
    room = chamber.Room()
    chamber.Room.make_room(room, level)
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
                if event.key == pygame.K_SPACE:
                    character.Player.shoot(player)


            if event.type == pygame.KEYUP:
                if event.key == key_left:
                    player.movement(player_speed, 0)
                if event.key == key_right:
                    player.movement(-player_speed, 0)
                if event.key == key_up:
                    player.movement(0, player_speed)
                if event.key == key_down:
                    player.movement(0, -player_speed)

        projectile.bullets.update()

        player.move(room.wall_list)
        gamedisplay.fill(black)
        character.player_sprite.draw(gamedisplay)
        room.wall_list.draw(gamedisplay)
        room.treasure_list.draw(gamedisplay)
        room.enemy_list.draw(gamedisplay)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()