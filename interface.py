import pygame
import pygame_menu
import sys

class Interface:
    pygame.init()
    surface = pygame.display.set_mode((800, 800))

    def set_difficulty(value, difficulty):
        #slozhnost pomenyat
        pass

    def start_the_game():
        pass



    while True:
        menu = pygame_menu.Menu("Denis Pacman v.1.0", 500, 600,
                                theme=pygame_menu.themes.THEME_BLUE)

        menu.add.text_input('Name :', default='denis')
        menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
        menu.add.button('Play', start_the_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)

        menu.mainloop(surface)