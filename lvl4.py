import pygame
import basics
from main import run_countdown, run_win, run_lose
from classes import Label, Image, Platform, Ball, Brick
pygame.init()


def run_lvl():
    basics.LVL4_MUSIC.update()
    level4_label = Label('l e v e l 4', 100 * basics.FONT_COEFFICIENT, 'fonts/retroblaze_font.ttf', 'green', center=(basics.WIN_RECT.right / 2, basics.LEVEL.upper_menu.bottom / 2))
    while True:
        bricks_left_label = Label('BRICKS LEFT: ' + str(len(basics.LEVEL.bricks_group) - 13), 60 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', 'white', bottomright=(basics.WIN_RECT.right - 8 * basics.X_COEFFICIENT, basics.LEVEL.upper_menu.bottom - 8 * basics.Y_COEFFICIENT))
        basics.CLOCK.tick(basics.FPS)
        if len(basics.LEVEL.bricks_group) - 13 == 0:
            basics.LVL4_MUSIC.stop()
            run_win('4')
        elif len(basics.LEVEL.balls_group) == 0:
            basics.LVL4_MUSIC.stop()
            run_lose()

        basics.LEVEL.bg.show()
        basics.WIN.fill('black', basics.LEVEL.upper_menu)
        level4_label.show()
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
        basics.LEVEL.handle_buffs()
        pygame.event.pump()
        pygame.display.update()
        if basics.LEVEL.countdown_state is True:
            run_countdown()
        if basics.LEVEL.countdown_state == 'process':
            basics.LEVEL.countdown_index += 1
            run_countdown()


def create_bricks():
    brick_x, brick_y = 8 * basics.X_COEFFICIENT, 124 * basics.Y_COEFFICIENT
    brick_size = (81.5 * basics.X_COEFFICIENT, 65 * basics.Y_COEFFICIENT)
    delta_brick_x, delta_brick_y = 89.5 * basics.X_COEFFICIENT, 73 * basics.Y_COEFFICIENT
    for i in range(80):
        brick_color = 'none'
        if i % 16 == 0 and i != 0:
            brick_x, brick_y = 8 * basics.X_COEFFICIENT, brick_y + delta_brick_y
        if i in [4, 11, 17, 21, 26, 30, 34, 38, 41, 45, 51, 60]:
            brick_color = 'yellow'
        if i in [5, 6, 7, 8, 9, 10, 16, 22, 23, 24, 25, 31, 32, 33, 39, 40, 46, 47, 48, 49, 50, 61, 62, 63]:
            brick_color = 'orange'
        if i in [55, 56]:
            brick_color = 'red'
        if i in [0, 15]:
            brick_color = 'blue'
        if i in [64, 65, 66, 67, 68, 75, 76, 77, 78, 79]:
            brick_color = 'gray'
        if brick_color != 'none':
            basics.LEVEL.bricks_group.add(Brick((brick_x, brick_y), brick_size, brick_color, armor=2))
        brick_x += delta_brick_x


def lvl4_main():
    basics.LAST_RUN = lvl4_main
    basics.LEVEL.__init__(bg=Image('backgrounds/lvl4_bg.png', (basics.WIN_RECT.right, basics.WIN_RECT.bottom - basics.LEVEL.upper_menu.height), topleft=(0, basics.LEVEL.upper_menu.bottom)), music=basics.LVL4_MUSIC, platform=Platform((620 * basics.X_COEFFICIENT, 720 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 30 * basics.Y_COEFFICIENT), 'objects/platform.png', 8))
    basics.LEVEL.balls_group.add(Ball((695 * basics.X_COEFFICIENT, 670 * basics.Y_COEFFICIENT), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT), basics.CURRENT_SHAPE, 8))
    create_bricks()

    basics.PRELAST_RUN = basics.LAST_RUN
    basics.LAST_RUN = run_lvl
    run_lvl()
