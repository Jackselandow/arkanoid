import pygame
import basics
from main import run_lvl1, run_lvl2, run_lvl3, run_lvl4
from classes import Label, Image, Button
pygame.init()


def levels_menu():
    basics.LEVELS_MENU_MUSIC.play(loops=-1)
    interference_index = 0

    levels_menu_bg = Image('backgrounds/levels_menu_bg.png', (basics.WIN_RECT.width, basics.WIN_RECT.height), topleft=(0, 0))
    back_levels_button = Button(Label('<', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GRAY, topleft=(10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT)), None, key=pygame.K_ESCAPE, feedbacks=[basics.CLICK_SOUND1.play, basics.LEVELS_MENU_MUSIC.stop, basics.PRELAST_RUN])
    levels_label = Label('LEVELS', 150 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.YELLOW, center=(basics.WIN_RECT.right / 2, 100 * basics.Y_COEFFICIENT))
    lvl1_icon_button = Button(None, Image('objects/levels_icons/lvl1_icon.png', (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), topleft=(160 * basics.X_COEFFICIENT, 270 * basics.Y_COEFFICIENT)), feedbacks=[basics.START_SOUND.play, basics.LEVELS_MENU_MUSIC.stop, run_lvl1])
    lvl1_icon_label = Label('Classic', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.WHITE, center=(320 * basics.X_COEFFICIENT, 472.5 * basics.Y_COEFFICIENT))
    lvl2_icon_button = Button(None, Image('objects/levels_icons/lvl2_icon.png', (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), topleft=(560 * basics.X_COEFFICIENT, 270 * basics.Y_COEFFICIENT)), feedbacks=[basics.START_SOUND.play, basics.LEVELS_MENU_MUSIC.stop, run_lvl2])
    lvl2_icon_label = Label('Ancient Egypt', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.WHITE, center=(720 * basics.X_COEFFICIENT, 472.5 * basics.Y_COEFFICIENT))
    lvl3_icon_button = Button(None, Image('objects/levels_icons/lvl3_icon.png', (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), topleft=(960 * basics.X_COEFFICIENT, 270 * basics.Y_COEFFICIENT)), feedbacks=[basics.START_SOUND.play, basics.LEVELS_MENU_MUSIC.stop, run_lvl3])
    lvl3_icon_label = Label('Middle Ages', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.WHITE, center=(1120 * basics.X_COEFFICIENT, 472.5 * basics.Y_COEFFICIENT))
    lvl4_icon_button = Button(None, Image('objects/levels_icons/lvl4_icon.png', (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), topleft=(360 * basics.X_COEFFICIENT, 545 * basics.Y_COEFFICIENT)), feedbacks=[basics.START_SOUND.play, basics.LEVELS_MENU_MUSIC.stop, run_lvl4])
    lvl4_icon_label = Label('Feudal Japan', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.WHITE, center=(520 * basics.X_COEFFICIENT, 747.5 * basics.Y_COEFFICIENT))
    # lvl5_icon_button = ImageButton(None, Image('objects/levels_icons/lvl5_icon.png', (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), topleft=(760 * basics.X_COEFFICIENT, 545 * basics.Y_COEFFICIENT)), feedbacks=[basics.START_SOUND.play, basics.LEVELS_MENU_MUSIC.stop, basics.run_lvl5])
    # lvl5_icon_label = Label('?', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.WHITE, center=(920 * basics.X_COEFFICIENT, 747.5 * basics.Y_COEFFICIENT))
    interference = [pygame.transform.scale(pygame.image.load('objects/interference/1.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/2.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/3.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/4.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/5.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT))]
    locker = pygame.transform.scale(pygame.image.load('objects/locker.png'), (50 * basics.X_COEFFICIENT, 75 * basics.Y_COEFFICIENT))
    levels_icons = [lvl1_icon_button, lvl2_icon_button, lvl3_icon_button, lvl4_icon_button]
    while True:
        basics.CLOCK.tick(basics.FPS)
        levels_menu_bg.show()
        levels_label.show()
        lvl1_icon_label.show()
        lvl2_icon_label.show()
        lvl3_icon_label.show()
        lvl4_icon_label.show()
        back_levels_button.all_in_one()
        done = False
        for level_icon in levels_icons:
            if len(basics.PASSED_LEVELS_LIST) >= levels_icons.index(level_icon):
                level_icon.all_in_one()
            else:
                basics.WIN.blit(interference[int(interference_index)], (level_icon.content.rect.x, level_icon.content.rect.y))
                if interference_index >= 4:
                    interference_index = 0
                elif done is False:
                    interference_index += 0.23
                    done = True
                basics.WIN.blit(locker, (level_icon.content.rect.x + 135 * basics.X_COEFFICIENT, level_icon.content.rect.y + 37.5 * basics.Y_COEFFICIENT))
        pygame.event.pump()
        pygame.display.update()
