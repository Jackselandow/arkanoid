import pygame
import basics
from main import WIN
pygame.init()


def run_levels_menu():
    basics.LAST_RUN = run_levels_menu
    run = True
    for music in basics.MUSICS:
        music.stop()
    basics.levels_music.play(loops=-1)

    while run:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            basics.back_levels_button.detect_click(event)
            for level_icon in basics.levels_icons:
                if basics.LEVELS_PASSED >= basics.levels_icons.index(level_icon):
                    level_icon.detect_click(event)
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(basics.levels_menu_bg, (0, 0))
        WIN.blit(basics.levels_text, basics.levels_rect)
        WIN.blit(basics.lvl1_icon_text, basics.lvl1_icon_rect)
        WIN.blit(basics.lvl2_icon_text, basics.lvl2_icon_rect)
        WIN.blit(basics.lvl3_icon_text, basics.lvl3_icon_rect)
        basics.back_levels_button.detect_mouse_collision()
        basics.back_levels_button.show()
        for level_icon in basics.levels_icons:
            if basics.LEVELS_PASSED >= basics.levels_icons.index(level_icon):
                level_icon.detect_mouse_collision()
                level_icon.show()
            else:
                WIN.blit(basics.interference, (level_icon.rect.x, level_icon.rect.y))
                WIN.blit(basics.locker, (level_icon.rect.x + 135 * basics.X_COEFFICIENT, level_icon.rect.y + 37.5 * basics.Y_COEFFICIENT))
        pygame.display.update()

    pygame.quit()
