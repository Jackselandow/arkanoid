import pygame as pg
from arkanoid import constants, Level
from arkanoid.classes import Label, Image, Button
from .settings_menu import run_main_settings
from .levels_menu import run_levels_menu
pg.init()


def run_main_menu(alpha, func_name='run_main_menu'):
    desired_func = None
    constants.MENU_MUSIC.play(-1)
    menu_bg = Image('arkanoid/resources/graphics/backgrounds/main_menu.jpeg', (constants.WIN_RECT.right, constants.WIN_RECT.bottom), topleft=(0, 0))
    arkanoid_logo = Image('arkanoid/resources/graphics/ui/arkanoid_logo.png', (1400 * constants.X_COEFFICIENT, 300 * constants.Y_COEFFICIENT), topleft=(20 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT))
    author_label = Label('Jackselandow Edition', 50 * constants.FONT_COEFFICIENT, 'tales', 'white', topleft=(0, 5 * constants.Y_COEFFICIENT))
    play_button = Button(Label('PLAY', 300 * constants.FONT_COEFFICIENT, 'pixeboy', 'white', 'red', topleft=(440 * constants.X_COEFFICIENT, 370 * constants.Y_COEFFICIENT)), 'white_arrows', click_sound='start', feedback='constants.MENU_MUSIC.stop()\nif len(constants.PASSED_LEVELS_LIST) != 0 and int(constants.PASSED_LEVELS_LIST[-1]) == constants.MAX_LEVEL:\n number = constants.PASSED_LEVELS_LIST[-1]\nelse:\n number = str(len(constants.PASSED_LEVELS_LIST) + 1)\ndesired_func = Level(number).play()\noutput = desired_func')
    settings_button = Button(Label('SETTINGS', 60 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', 'green', topleft=(560 * constants.X_COEFFICIENT, 570 * constants.Y_COEFFICIENT)), 'white_arrows', feedback='constants.MENU_MUSIC.stop()\ndesired_func = run_main_settings()\noutput = desired_func')
    levels_button = Button(Label('LEVELS', 60 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', 'blue', topleft=(600 * constants.X_COEFFICIENT, 660 * constants.Y_COEFFICIENT)), 'white_arrows', feedback='constants.MENU_MUSIC.stop()\ndesired_func = run_levels_menu()\noutput = desired_func')
    exit_button = Button(Label('EXIT', 60 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', 'gray49', topleft=(640 * constants.X_COEFFICIENT, 750 * constants.Y_COEFFICIENT)), 'gray_arrows', feedback='pg.mixer.fadeout(850)\ndesired_func = "quit"\noutput = desired_func')
    version_label = Label('Version 4.0', 50 * constants.FONT_COEFFICIENT, 'tales', 'black', bottomright=(constants.WIN_RECT.width - 8 * constants.X_COEFFICIENT, constants.WIN_RECT.height))
    while True:
        constants.CLOCK.tick(constants.FPS)
        events = pg.event.get()
        globs = globals()
        locs = locals()
        for event in events:
            if event.type == pg.QUIT:
                pg.mixer.fadeout(850)
                desired_func = 'quit'
        menu_bg.show()
        arkanoid_logo.show()
        author_label.show()
        version_label.show()
        if output := play_button.update(events, globs, locs): desired_func = output
        if output := settings_button.update(events, globs, locs): desired_func = output
        if output := levels_button.update(events, globs, locs): desired_func = output
        if output := exit_button.update(events, globs, locs): desired_func = output
        if alpha != -5:
            alpha -= 10
            constants.BLACK_SCREEN.set_alpha(alpha)
            constants.WIN.blit(constants.BLACK_SCREEN, (0, 0))
        if desired_func:
            if func_name != desired_func:
                return desired_func
            else:
                desired_func = None
                constants.MENU_MUSIC.play(-1)
        pg.display.update()


def exit_confirmation():
    transparent_bg = constants.BLACK_SCREEN
    transparent_bg.set_alpha(120)
    constants.WIN.blit(transparent_bg, (0, 0))
    # confirmation_bg = Image('arkanoid/resources/graphics/backgrounds/pause_bg.png', (810 * constants.X_COEFFICIENT, 562.5 * constants.Y_COEFFICIENT), center=(constants.WIN_RECT.right / 2, constants.WIN_RECT.bottom / 2))
    confirmation_label = Label('Are you sure?', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'white', center=(constants.WIN_RECT.right / 2, 330 * constants.Y_COEFFICIENT))
    confirm_button = Button(Label('YES', 80 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', topleft=(600 * constants.X_COEFFICIENT, 450 * constants.Y_COEFFICIENT)), None, key=pg.K_SPACE, feedbacks=[constants.MENU_MUSIC.stop, run_outro])
    reject_button = Button(Label('NO', 80 * constants.FONT_COEFFICIENT, 'pixeboy', 'green', topleft=(800 * constants.X_COEFFICIENT, 450 * constants.Y_COEFFICIENT)), None, key=pg.K_ESCAPE)
    while True:
        constants.CLOCK.tick(constants.FPS)
        constants.WIN.blit(transparent_bg, (0, 0))
        # confirmation_bg.show()
        confirmation_label.show()
        confirm_button.all_in_one()
        if reject_button.all_in_one() is True:
            constants.CLICK_SOUND1.play()
            break
        pg.event.pump()
        pg.display.update()



