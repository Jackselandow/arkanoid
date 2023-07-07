import pygame
import basics
from main import run_menu
from classes import Label, Button
from progress import update_game_progress
pygame.init()


def win(passed_level):
    for buff in basics.LEVEL.active_buffs_group:
        if buff.timer:
            buff.timer.cancel()
    basics.LEVEL.active_buffs_group.empty()
    passed_state = update_game_progress(passed_level)
    basics.WIN_SOUND.play()

    cup = pygame.transform.scale(pygame.image.load('objects/cup.png'), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    level_label = Label('LEVEL', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 150 * basics.Y_COEFFICIENT))
    completed_label = Label('COMPLETED', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 270 * basics.Y_COEFFICIENT))
    next_level_button = Button(Label('NEXT LEVEL', 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.GREEN, topleft=(470 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT)), None, 'arrows', 'green', key=pygame.K_SPACE)
    menu_button = Button(Label('MAIN MENU', 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.GRAY, topleft=(495 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT)), None, 'arrows', 'gray', key=pygame.K_ESCAPE, feedbacks=[basics.CLICK_SOUND1.play, basics.WIN_SOUND.stop, run_menu])
    shape_unlocked_label = Label('NEW BALL SHAPE UNLOCKED!', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.RED, bottomleft=(basics.WIN_RECT.width, basics.WIN_RECT.bottom))
    while True:
        basics.CLOCK.tick(basics.FPS)
        basics.WIN.fill(basics.BLACK)
        basics.WIN.blit(cup, (220 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
        basics.WIN.blit(cup, (1010 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
        level_label.show()
        completed_label.show()
        if int(passed_level) != len(basics.LEVELS_ICONS) and next_level_button.all_in_one():
            basics.WIN_SOUND.stop()
            basics.LEVELS_ICONS[int(passed_level)].give_feedback()
        menu_button.all_in_one()
        if passed_state is True:
            shape_unlocked_label.show()
            shape_unlocked_label.rect.x -= 5
        pygame.event.pump()
        pygame.display.update()


def lose():
    for buff in basics.LEVEL.active_buffs_group:
        if buff.timer:
            buff.timer.cancel()
    basics.LEVEL.active_buffs_group.empty()
    basics.LOSE_SOUND.play()

    lose_screen = pygame.transform.scale(pygame.image.load('objects/lose.png'), (640 * basics.X_COEFFICIENT, 320 * basics.Y_COEFFICIENT))
    retry_button = Button(Label('RETRY', 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.RED, topleft=(595 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT)), None, 'arrows', 'red', key=pygame.K_SPACE, feedbacks=[basics.CLICK_SOUND1.play, basics.LOSE_SOUND.stop, basics.PRELAST_RUN])
    menu_button = Button(Label('MAIN MENU', 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.GRAY, topleft=(495 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT)), None, 'arrows', 'gray', key=pygame.K_ESCAPE, feedbacks=[basics.CLICK_SOUND1.play, basics.LOSE_SOUND.stop, run_menu])
    while True:
        basics.CLOCK.tick(basics.FPS)
        basics.WIN.fill(basics.BLACK)
        basics.WIN.blit(lose_screen, (400 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
        retry_button.all_in_one()
        menu_button.all_in_one()
        pygame.event.pump()
        pygame.display.update()
