import pygame
import basics
from main import run_menu, run_settings, run_levels_menu
from classes import Label, Image, Button
pygame.init()


def preview():
    pygame.time.wait(500)
    basics.PREVIEW_SOUND.play()
    pygame.time.wait(1000)
    preview_bg = Image('backgrounds/preview_bg0(1).png', (basics.WIN_RECT.width, basics.WIN_RECT.height), topleft=(0, 0))
    alpha = 255
    while alpha != -5:
        alpha -= 10
        basics.CLOCK.tick(basics.FPS)
        basics.BLACK_SCREEN.set_alpha(alpha)
        preview_bg.show()
        basics.WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()
    pygame.time.wait(1000)
    while alpha != 255:
        alpha += 10
        basics.CLOCK.tick(basics.FPS)
        basics.BLACK_SCREEN.set_alpha(alpha)
        preview_bg.show()
        basics.WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()
    basics.PREVIEW_SOUND.stop()
    run_menu(alpha)


def main_menu(alpha):
    basics.MENU_MUSIC.play(loops=-1)
    menu_bg = Image('backgrounds/menu_bg.jpeg', (basics.WIN_RECT.right, basics.WIN_RECT.bottom), topleft=(0, 0))
    arkanoid_logo = Image('objects/arkanoid_logo.png', (1400 * basics.X_COEFFICIENT, 300 * basics.Y_COEFFICIENT), topleft=(20 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    author_label = Label('Jackselandow Edition', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.WHITE, topleft=(0, 5 * basics.Y_COEFFICIENT))
    play_button = Button(Label('PLAY', 300 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.WHITE, basics.RED, topleft=(440 * basics.X_COEFFICIENT, 370 * basics.Y_COEFFICIENT)), None, 'arrows', 'white')
    settings_button = Button(Label('SETTINGS', 60 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.GREEN, topleft=(560 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT)), None, 'arrows', 'white', feedbacks=[basics.CLICK_SOUND1.play, basics.MENU_MUSIC.stop, run_settings])
    levels_button = Button(Label('LEVELS', 60 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.BLUE, topleft=(600 * basics.X_COEFFICIENT, 660 * basics.Y_COEFFICIENT)), None, 'arrows', 'white', feedbacks=[basics.CLICK_SOUND1.play, basics.MENU_MUSIC.stop, run_levels_menu])
    exit_button = Button(Label('EXIT', 60 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.GRAY, topleft=(640 * basics.X_COEFFICIENT, 750 * basics.Y_COEFFICIENT)), None, 'arrows', 'black', feedbacks=[basics.CLICK_SOUND1.play, exit_confirmation])
    version_label = Label('Version 4.0', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.BLACK, bottomright=(basics.WIN_RECT.width - 8 * basics.X_COEFFICIENT, basics.WIN_RECT.height))
    while True:
        basics.CLOCK.tick(basics.FPS)
        menu_bg.show()
        arkanoid_logo.show()
        author_label.show()
        version_label.show()
        if play_button.all_in_one() is True:
            basics.MENU_MUSIC.stop()
            if len(basics.PASSED_LEVELS_LIST) == len(basics.LEVELS_ICONS):
                basics.LEVELS_ICONS[-1].give_feedback()
            else:
                index = len(basics.PASSED_LEVELS_LIST)
                basics.LEVELS_ICONS[index].give_feedback()
        settings_button.all_in_one()
        levels_button.all_in_one()
        exit_button.all_in_one()
        if alpha != -5:
            alpha -= 10
            basics.BLACK_SCREEN.set_alpha(alpha)
            basics.WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.event.pump()
        pygame.display.update()


def exit_confirmation():
    transparent_bg = basics.BLACK_SCREEN
    transparent_bg.set_alpha(120)
    basics.WIN.blit(transparent_bg, (0, 0))
    confirmation_bg = Image('backgrounds/pause_bg.png', (810 * basics.X_COEFFICIENT, 562.5 * basics.Y_COEFFICIENT), center=(basics.WIN_RECT.right / 2, basics.WIN_RECT.bottom / 2))
    confirmation_label = Label('Are you sure?', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 330 * basics.Y_COEFFICIENT))
    confirm_button = Button(Label('YES', 80 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, topleft=(600 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT)), None, key=pygame.K_SPACE, feedbacks=[basics.MENU_MUSIC.stop, postview])
    reject_button = Button(Label('NO', 80 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.GREEN, topleft=(800 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT)), None, key=pygame.K_ESCAPE)
    while True:
        basics.CLOCK.tick(basics.FPS)
        basics.WIN.blit(transparent_bg, (0, 0))
        # confirmation_bg.show()
        confirmation_label.show()
        confirm_button.all_in_one()
        if reject_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            break
        pygame.event.pump()
        pygame.display.update()


def postview():
    ws_alpha = 0
    shutdown_list = [pygame.transform.scale(pygame.image.load(f'objects/shutdown/{i}.png'), (basics.WIN_RECT.width, basics.WIN_RECT.height)) for i in range(1, 19)]
    basics.POWER_DOWN_SOUND.play()
    while ws_alpha < 255:
        ws_alpha += 5
        basics.CLOCK.tick(basics.FPS)
        basics.WHITE_SCREEN.set_alpha(ws_alpha)
        basics.WIN.blit(basics.WHITE_SCREEN, (0, 0))
        pygame.display.update()
    basics.POSTVIEW_SOUND.play()
    for frame in shutdown_list:
        basics.CLOCK.tick(20)
        basics.WIN.blit(frame, (0, 0))
        pygame.display.update()
    exit()
