import pygame
import basics
from main import run_countdown, run_win, run_lose
from classes import Label, Image, Platform, Ball, Brick
pygame.init()


def run_lvl():
    basics.LVL1_MUSIC.update()
    level1_label = Label('l e v e l 1', 100 * basics.FONT_COEFFICIENT, 'fonts/retroblaze_font.ttf', 'green', center=(basics.WIN_RECT.right / 2, basics.LEVEL.upper_menu.bottom / 2))
    while True:
        bricks_left_label = Label('BRICKS LEFT: ' + str(len(basics.LEVEL.bricks_group)), 60 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', 'white', bottomright=(basics.WIN_RECT.right - 8 * basics.X_COEFFICIENT, basics.LEVEL.upper_menu.bottom - 8 * basics.Y_COEFFICIENT))
        basics.CLOCK.tick(basics.FPS)
        if len(basics.LEVEL.bricks_group) == 0:
            basics.LVL1_MUSIC.stop()
            run_win('1')
        elif len(basics.LEVEL.balls_group) == 0:
            basics.LVL1_MUSIC.stop()
            run_lose()

        basics.LEVEL.bg.show()
        basics.WIN.fill('black', basics.LEVEL.upper_menu)
        level1_label.show()
        bricks_left_label.show()
        basics.LEVEL.platform_group.draw(basics.WIN)
        basics.LEVEL.balls_group.draw(basics.WIN)
        basics.LEVEL.bricks_group.draw(basics.WIN)
        if basics.LEVEL.countdown_state is False:
            if basics.LEVEL.pause_button.detect_press() is True:
                basics.LEVEL.pause_button.give_feedback()
            basics.LEVEL.platform_group.update()
            basics.LEVEL.detect_start()
        basics.LEVEL.pause_button.show()
        pygame.event.pump()
        pygame.display.update()
        if basics.LEVEL.countdown_state is True:
            run_countdown()
        if basics.LEVEL.countdown_state == 'process':
            basics.LEVEL.countdown_index += 1
            run_countdown()


def create_bricks():
    # brick1 = basics.Brick((8 * basics.X_COEFFICIENT, 124 * basics.Y_COEFFICIENT), brick_size, 'blue')
    brick_x, brick_y = 8 * basics.X_COEFFICIENT, 124 * basics.Y_COEFFICIENT
    brick_size = (135.2 * basics.X_COEFFICIENT, 40 * basics.Y_COEFFICIENT)
    delta_brick_x, delta_brick_y = 143.2 * basics.X_COEFFICIENT, 48 * basics.Y_COEFFICIENT
    for i in range(56):
        brick_color = 'none'
        if i % 10 == 0 and i != 0:
            brick_x, brick_y = 8 * basics.X_COEFFICIENT, brick_y + delta_brick_y
        if i in [0, 9, 10, 19]:
            brick_color = 'green'
        if i in [1, 2, 7, 8, 11, 12, 17, 18, 21, 22, 27, 28, 31, 32, 37, 38]:
            brick_color = 'purple'
        if i in [3, 4, 5, 6, 13, 16]:
            brick_color = 'yellow'
        if i in [23, 26, 33, 34, 35, 36, 44, 45, 54, 55]:
            brick_color = 'red'
        if brick_color != 'none':
            basics.LEVEL.bricks_group.add(Brick((brick_x, brick_y), brick_size, brick_color))
        brick_x += delta_brick_x


def lvl1_main():
    basics.LAST_RUN = lvl1_main
    basics.LEVEL.__init__(bg=Image('backgrounds/lvl1_bg.png', (basics.WIN_RECT.right, basics.WIN_RECT.bottom - basics.LEVEL.upper_menu.height), topleft=(0, basics.LEVEL.upper_menu.bottom)), music=basics.LVL1_MUSIC, platform=Platform((620 * basics.X_COEFFICIENT, 720 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 30 * basics.Y_COEFFICIENT), 'objects/platform.png', 8))
    basics.LEVEL.balls_group.add(Ball((695 * basics.X_COEFFICIENT, 670 * basics.Y_COEFFICIENT), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT), basics.CURRENT_SHAPE, 8))
    create_bricks()

    basics.PRELAST_RUN = basics.LAST_RUN
    basics.LAST_RUN = run_lvl
    run_lvl()
