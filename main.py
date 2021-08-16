import os
from Obstacles import *
import pygame
from Menu import *
import Character
import glob

# player
player_size = (150, 150)
player_coordinates = [0, 575]
player = Character.Character(player_coordinates[0], player_coordinates[1], player_size[0], player_size[1])

# window
window_size = width, height = 1280, 768
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("The Epic Sword Guy")
bg = pygame.transform.scale(pygame.image.load(
    os.path.join("assets/background", "Background.png")), window_size)

# menu
menu = Menu(24)
# obstacles
lava = Obstacles(window_size[0], 700, 300, 285, 15)
lava.load_image(os.path.join("assets/Obstacles/lava", "lava0.png"))

spikes = Obstacles(window_size[0], 700, 300, 285, 0)
spikes.load_image(os.path.join("assets/Obstacles", "spikes.png"))

list_of_obstacles = [lava, spikes]
item = 0
FPS = 27


def redraw_window():
    window.blit(bg, (0, 0))
    if menu.game_started:
        player.alive = True
        key = pygame.key.get_pressed()
        player.movement(key)
        player.draw_remaining_health(window)
        spawn_obstacle()
        player.player_animation(window, FPS)
        player.damage_player(list_of_obstacles, 0)
        player.damage_player(list_of_obstacles, 1)
        menu.draw_score(window, window_size[0] - 200, 50, player.score)
        if player.alive is False:
            menu.restart_game(player, list_of_obstacles)
    else:
        menu.draw_main_menu(window, window_size[0], window_size[1])

    pygame.display.update()


def spawn_obstacle():
    window.blit(list_of_obstacles[0].image, (list_of_obstacles[0].x, list_of_obstacles[0].y))
    window.blit(list_of_obstacles[1].image, (list_of_obstacles[1].x, list_of_obstacles[1].y))
    if player.alive:
        list_of_obstacles[0].move()
        list_of_obstacles[1].move()
    if list_of_obstacles[0].x + list_of_obstacles[0].width < 0:
        list_of_obstacles[0].x = window_size[0]
    if list_of_obstacles[1].x + list_of_obstacles[1].width < 0:
        list_of_obstacles[1].x = window_size[0]
    if list_of_obstacles[0].x < 500:
        list_of_obstacles[1].velocity = 15


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redraw_window()


main()
