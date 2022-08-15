import pygame
import basics
pygame.init()


def run_levels_menu():
    basics.LAST_RUN = run_levels_menu
    for music in basics.MUSICS:
        music.stop()
    basics.LEVELS_MENU_MUSIC.play(loops=-1)
    interference_index = 0

    levels_menu_bg = pygame.transform.scale(pygame.image.load('backgrounds/levels_menu_bg.png'), (basics.WIN_RECT.width, basics.WIN_RECT.height))
    back_levels_button = basics.TextButton('<', (10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT), 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GREY, [basics.CLICK_SOUND1.play, 'PRELAST_RUN'])
    levels_text = basics.BIG_ENDLESS_FONT.render('LEVELS', False, basics.YELLOW)
    levels_rect = levels_text.get_rect(center=(basics.WIN_RECT.right / 2, 100 * basics.Y_COEFFICIENT))
    lvl1_icon_button = basics.ImageButton('objects/levels_icons/lvl1_icon.png', (160 * basics.X_COEFFICIENT, 270 * basics.Y_COEFFICIENT), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), [basics.START_SOUND.play, basics.run_lvl1])
    lvl1_icon_text = basics.TALES_FONT.render('Classic', False, basics.WHITE)
    lvl1_icon_rect = lvl1_icon_text.get_rect(center=(320 * basics.X_COEFFICIENT, 472.5 * basics.Y_COEFFICIENT))
    lvl2_icon_button = basics.ImageButton('objects/levels_icons/lvl2_icon.png', (560 * basics.X_COEFFICIENT, 270 * basics.Y_COEFFICIENT), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), [basics.START_SOUND.play, basics.run_lvl2])
    lvl2_icon_text = basics.TALES_FONT.render('Ancient Egypt', False, basics.WHITE)
    lvl2_icon_rect = lvl2_icon_text.get_rect(center=(720 * basics.X_COEFFICIENT, 472.5 * basics.Y_COEFFICIENT))
    lvl3_icon_button = basics.ImageButton('objects/levels_icons/lvl3_icon.png', (960 * basics.X_COEFFICIENT, 270 * basics.Y_COEFFICIENT), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), [basics.START_SOUND.play, basics.run_lvl3])
    lvl3_icon_text = basics.TALES_FONT.render('Middle Ages', False, basics.WHITE)
    lvl3_icon_rect = lvl3_icon_text.get_rect(center=(1120 * basics.X_COEFFICIENT, 472.5 * basics.Y_COEFFICIENT))
    # lvl4_icon_button = basics.ImageButton('objects/levels_icons/lvl4_icon.png', (360 * basics.X_COEFFICIENT, 545 * basics.Y_COEFFICIENT), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), [basics.START_SOUND1.play, basics.run_lvl4])
    # lvl4_icon_text = basics.TALES_FONT.render('?', False, basics.WHITE)
    # lvl4_icon_rect = lvl4_icon_text.get_rect(center=(520 * basics.X_COEFFICIENT, 747.5 * basics.Y_COEFFICIENT))
    # lvl5_icon_button = basics.ImageButton('objects/levels_icons/lvl5_icon.png', (760 * basics.X_COEFFICIENT, 545 * basics.Y_COEFFICIENT), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT), [basics.START_SOUND1.play, basics.run_lvl5])
    # lvl5_icon_text = basics.TALES_FONT.render('?', False, basics.WHITE)
    # lvl5_icon_rect = lvl5_icon_text.get_rect(center=(920 * basics.X_COEFFICIENT, 747.5 * basics.Y_COEFFICIENT))
    interference = [pygame.transform.scale(pygame.image.load('objects/interference/1.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/2.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/3.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/4.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT)), pygame.transform.scale(pygame.image.load('objects/interference/5.jpeg'), (320 * basics.X_COEFFICIENT, 160 * basics.Y_COEFFICIENT))]
    locker = pygame.transform.scale(pygame.image.load('objects/locker.png'), (50 * basics.X_COEFFICIENT, 75 * basics.Y_COEFFICIENT))
    levels_icons = [lvl1_icon_button, lvl2_icon_button, lvl3_icon_button]
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            back_levels_button.detect_click(event)
            for level_icon in levels_icons:
                if len(basics.PASSED_LEVELS_LIST) >= levels_icons.index(level_icon):
                    level_icon.detect_click(event)

        basics.WIN.blit(levels_menu_bg, (0, 0))
        basics.WIN.blit(levels_text, levels_rect)
        basics.WIN.blit(lvl1_icon_text, lvl1_icon_rect)
        basics.WIN.blit(lvl2_icon_text, lvl2_icon_rect)
        basics.WIN.blit(lvl3_icon_text, lvl3_icon_rect)
        back_levels_button.detect_mouse_collision()
        back_levels_button.show()
        done = False
        for level_icon in levels_icons:
            if len(basics.PASSED_LEVELS_LIST) >= levels_icons.index(level_icon):
                level_icon.detect_mouse_collision()
                level_icon.show()
            else:
                basics.WIN.blit(interference[int(interference_index)], (level_icon.rect.x, level_icon.rect.y))
                if interference_index >= 4:
                    interference_index = 0
                elif done is False:
                    interference_index += 0.23
                    done = True
                basics.WIN.blit(locker, (level_icon.rect.x + 135 * basics.X_COEFFICIENT, level_icon.rect.y + 37.5 * basics.Y_COEFFICIENT))
        pygame.display.update()
