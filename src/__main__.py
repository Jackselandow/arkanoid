import pygame as pg
from arkanoid import constants, run_main_menu
from arkanoid.classes import Image
pg.init()

# def run_preview():
#     basics.LAST_RUN = run_preview
#     from main_menu import preview
#     preview()
#
#
# def run_menu(alpha=-5):
#     basics.LAST_RUN = run_menu
#     basics.PRELAST_RUN = basics.LAST_RUN
#     from main_menu import main_menu
#     main_menu(alpha)
#
#
# def run_settings():
#     basics.LAST_RUN = run_settings
#     from settings import main_settings
#     main_settings()
#
#
# def run_levels_menu():
#     basics.LAST_RUN = run_levels_menu
#     from levels_menu import levels_menu
#     levels_menu()
#
#
# def run_pause():
#     from pause import pause
#     pause()
#
#
# def run_countdown():
#     from pause import countdown
#     countdown()
#
#
# def run_win(passed_level):
#     from win_lose import win
#     win(passed_level)
#
#
# def run_lose():
#     from win_lose import lose
#     lose()
#
#
# def run_lvl1():
#     basics.LAST_RUN = run_lvl1
#     from lvl1 import lvl1_main
#     lvl1_main()
#
#
# def run_lvl2():
#     basics.LAST_RUN = run_lvl2
#     from lvl2 import lvl2_main
#     lvl2_main()
#
#
# def run_lvl3():
#     basics.LAST_RUN = run_lvl3
#     from lvl3 import lvl3_main
#     lvl3_main()
#
#
# def run_lvl4():
#     basics.LAST_RUN = run_lvl4
#     from lvl4 import lvl4_main
#     lvl4_main()


def run_intro():
    pg.time.wait(500)
    constants.INTRO_SOUND.play()
    pg.time.wait(1000)
    intro_bg = Image('arkanoid/resources/graphics/backgrounds/intro.png', (constants.WIN_RECT.width, constants.WIN_RECT.height), topleft=(0, 0))
    alpha = 255
    while alpha != -5:
        alpha -= 10
        constants.CLOCK.tick(constants.FPS)
        constants.BLACK_SCREEN.set_alpha(alpha)
        intro_bg.show()
        constants.WIN.blit(constants.BLACK_SCREEN, (0, 0))
        pg.display.update()
    pg.time.wait(1000)
    while alpha != 255:
        alpha += 10
        constants.CLOCK.tick(constants.FPS)
        constants.BLACK_SCREEN.set_alpha(alpha)
        intro_bg.show()
        constants.WIN.blit(constants.BLACK_SCREEN, (0, 0))
        pg.display.update()
    constants.INTRO_SOUND.stop()
    run_main_menu(alpha)


def run_outro():
    ws_alpha = 0
    shutdown_list = [pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/shutdown/{i}.png'), (constants.WIN_RECT.width, constants.WIN_RECT.height)).convert() for i in range(1, 19)]
    constants.POWER_DOWN_SOUND.play()
    while ws_alpha < 255:
        constants.CLOCK.tick(constants.FPS)
        ws_alpha += 10
        constants.WHITE_SCREEN.set_alpha(ws_alpha)
        constants.WIN.blit(constants.WHITE_SCREEN, (0, 0))
        pg.display.update()
    constants.OUTRO_SOUND.play()
    for frame in shutdown_list:
        constants.CLOCK.tick(20)
        constants.WIN.blit(frame, (0, 0))
        pg.display.update()


def main():
    run_intro()
    run_outro()
    exit()


if __name__ == "__main__":
    main()
