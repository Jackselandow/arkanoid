import pygame as pg
from arkanoid import constants, run_main_menu
from arkanoid.classes import Image
pg.init()


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
    last_frame = run_main_menu(alpha) # the last frame is returned instead of desired function since otherwise the unnecessary ui of the screens, called between run_intro() and the last screen where exit was pressed, would be shown
    return last_frame


def run_outro(last_frame):
    ws_alpha = 0
    shutdown_list = [pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/shutdown/{i}.png'), (constants.WIN_RECT.width, constants.WIN_RECT.height)).convert() for i in range(1, 19)]
    constants.POWER_DOWN_SOUND.play()
    while ws_alpha < 255:
        constants.CLOCK.tick(constants.FPS)
        constants.WIN.blit(last_frame, (0, 0))
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
    last_frame = run_intro()
    run_outro(last_frame)
    exit()


if __name__ == "__main__":
    main()
