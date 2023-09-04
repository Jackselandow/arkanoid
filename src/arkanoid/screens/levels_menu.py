import pygame as pg
from arkanoid import constants, Level
from arkanoid.classes import Label, Image, Button
pg.init()


def run_levels_menu(func_name='run_levels_menu'):
    desired_func = None
    constants.LEVELS_MENU_MUSIC.play(loops=-1)
    interference_index = 0

    levels_menu_bg = Image('arkanoid/resources/graphics/backgrounds/levels_menu.png', (constants.WIN_RECT.width, constants.WIN_RECT.height), topleft=(0, 0))
    back_levels_button = Button(Label('<', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', 'gray49', topleft=(10 * constants.X_COEFFICIENT, 10 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_ESCAPE, feedback='constants.LEVELS_MENU_MUSIC.stop()\ndesired_func = "run_main_menu"\noutput = desired_func')
    levels_label = Label('LEVELS', 150 * constants.FONT_COEFFICIENT, 'endless', 'yellow', center=(constants.WIN_RECT.right / 2, 100 * constants.Y_COEFFICIENT))
    lvl1_icon_button = Button(Image('arkanoid/resources/graphics/levels_menu/level_icons/lvl1_icon.png', (320 * constants.X_COEFFICIENT, 160 * constants.Y_COEFFICIENT), topleft=(160 * constants.X_COEFFICIENT, 270 * constants.Y_COEFFICIENT)), 'glow', click_sound='start', feedback='constants.LEVELS_MENU_MUSIC.stop\ndesired_func = Level("1").play()\noutput = desired_func')
    lvl1_icon_label = Label('Classic', 50 * constants.FONT_COEFFICIENT, 'tales', 'white', center=(320 * constants.X_COEFFICIENT, 472.5 * constants.Y_COEFFICIENT))
    lvl2_icon_button = Button(Image('arkanoid/resources/graphics/levels_menu/level_icons/lvl2_icon.png', (320 * constants.X_COEFFICIENT, 160 * constants.Y_COEFFICIENT), topleft=(560 * constants.X_COEFFICIENT, 270 * constants.Y_COEFFICIENT)), 'glow', click_sound='start', feedback='constants.LEVELS_MENU_MUSIC.stop\ndesired_func = Level("2").play()\noutput = desired_func')
    lvl2_icon_label = Label('Ancient Egypt', 50 * constants.FONT_COEFFICIENT, 'tales', 'white', center=(720 * constants.X_COEFFICIENT, 472.5 * constants.Y_COEFFICIENT))
    lvl3_icon_button = Button(Image('arkanoid/resources/graphics/levels_menu/level_icons/lvl3_icon.png', (320 * constants.X_COEFFICIENT, 160 * constants.Y_COEFFICIENT), topleft=(960 * constants.X_COEFFICIENT, 270 * constants.Y_COEFFICIENT)), 'glow', click_sound='start', feedback='constants.LEVELS_MENU_MUSIC.stop\ndesired_func = Level("3").play()\noutput = desired_func')
    lvl3_icon_label = Label('Middle Ages', 50 * constants.FONT_COEFFICIENT, 'tales', 'white', center=(1120 * constants.X_COEFFICIENT, 472.5 * constants.Y_COEFFICIENT))
    lvl4_icon_button = Button(Image('arkanoid/resources/graphics/levels_menu/level_icons/lvl4_icon.png', (320 * constants.X_COEFFICIENT, 160 * constants.Y_COEFFICIENT), topleft=(360 * constants.X_COEFFICIENT, 545 * constants.Y_COEFFICIENT)), 'glow', click_sound='start', feedback='constants.LEVELS_MENU_MUSIC.stop\ndesired_func = Level("4").play()\noutput = desired_func')
    lvl4_icon_label = Label('Feudal Japan', 50 * constants.FONT_COEFFICIENT, 'tales', 'white', center=(520 * constants.X_COEFFICIENT, 747.5 * constants.Y_COEFFICIENT))
    # lvl5_icon_button = ImageButton(None, Image('arkanoid/resources/graphics/levels_menu/level_icons/lvl5_icon.png', (320 * constants.X_COEFFICIENT, 160 * constants.Y_COEFFICIENT), topleft=(760 * constants.X_COEFFICIENT, 545 * constants.Y_COEFFICIENT)), feedbacks=[constants.START_SOUND.play, constants.LEVELS_MENU_MUSIC.stop, constants.run_lvl5])
    # lvl5_icon_label = Label('?', 50 * constants.FONT_COEFFICIENT, 'tales', constants.WHITE, center=(920 * constants.X_COEFFICIENT, 747.5 * constants.Y_COEFFICIENT))
    interference = [pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/levels_menu/interference/{i}.jpeg'), (320 * constants.X_COEFFICIENT, 160 * constants.Y_COEFFICIENT)).convert() for i in range(5)]
    lock = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/levels_menu/lock.png'), (50 * constants.X_COEFFICIENT, 75 * constants.Y_COEFFICIENT)).convert_alpha()
    level_icons = [lvl1_icon_button, lvl2_icon_button, lvl3_icon_button, lvl4_icon_button]
    while True:
        constants.CLOCK.tick(constants.FPS)
        events = pg.event.get()
        globs = globals()
        locs = locals()
        for event in events:
            if event.type == pg.QUIT:
                pg.mixer.fadeout(850)
                desired_func = 'quit'
        levels_menu_bg.show()
        levels_label.show()
        lvl1_icon_label.show()
        lvl2_icon_label.show()
        lvl3_icon_label.show()
        lvl4_icon_label.show()
        if output := back_levels_button.update(events, globs, locs): desired_func = output
        done = False
        for level_icon in level_icons:
            if len(constants.PASSED_LEVELS_LIST) >= level_icons.index(level_icon):
                if output := level_icon.update(events, globs, locs): desired_func = output
            else:
                constants.WIN.blit(interference[int(interference_index)], (level_icon.content.rect.x, level_icon.content.rect.y))
                if interference_index >= 4:
                    interference_index = 0
                elif done is False:
                    interference_index += 0.23
                    done = True
                constants.WIN.blit(lock, (level_icon.content.rect.x + 135 * constants.X_COEFFICIENT, level_icon.content.rect.y + 37.5 * constants.Y_COEFFICIENT))
        if desired_func:
            if func_name != desired_func:
                return desired_func
            else:
                desired_func = None
        pg.display.update()
