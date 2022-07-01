import pygame
import basics
pygame.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    # my WIN.size = (1440, 900)
# WIN = pygame.display.set_mode((900, 750))
pygame.display.set_caption("ARKANOID")


def run_preview():
    basics.LAST_RUN = run_preview
    alpha = 255
    while alpha != -5:
        alpha -= 10
        basics.CLOCK.tick(basics.FPS)
        basics.BLACK_SCREEN.set_alpha(alpha)
        WIN.blit(basics.preview_bg, (0, 0))
        WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()
    pygame.time.wait(1000)
    while alpha != 255:
        alpha += 10
        basics.CLOCK.tick(basics.FPS)
        basics.BLACK_SCREEN.set_alpha(alpha)
        WIN.blit(basics.preview_bg, (0, 0))
        WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()
    run_menu()


def run_menu():
    if basics.LAST_RUN == run_preview:
        alpha = 255
    else:
        alpha = -5
    basics.LAST_RUN = run_menu
    basics.PRELAST_RUN = basics.LAST_RUN
    run = True
    for music in basics.MUSICS:
        music.stop()
    basics.menu_music.play(loops=-1)
    while run:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            if basics.play_button.detect_click(event) is True:
                for level_icon in basics.levels_icons:
                    if basics.LEVELS_PASSED == basics.levels_icons.index(level_icon):
                        level_icon.clicked()
            basics.levels_button.detect_click(event)
            basics.settings_button.detect_click(event)
            basics.exit_button.detect_click(event)
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(basics.menu_bg, (0, 0))
        WIN.blit(basics.arkanoid_logo, (20 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
        WIN.blit(basics.author_text, basics.author_rect)
        WIN.blit(basics.version_text, basics.version_rect)
        basics.play_button.detect_mouse_collision()
        basics.levels_button.detect_mouse_collision()
        basics.settings_button.detect_mouse_collision()
        basics.exit_button.detect_mouse_collision()
        basics.play_button.show()
        basics.levels_button.show()
        basics.settings_button.show()
        basics.exit_button.show()
        if alpha != -5:
            alpha -= 10
            basics.BLACK_SCREEN.set_alpha(alpha)
            WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()

    pygame.quit()


def run_pause():
    run = True
    pygame.mixer.pause()
    transparent_bg = basics.BLACK_SCREEN
    transparent_bg.set_alpha(120)
    WIN.blit(transparent_bg, (0, 0))

    while run:
        key_pressed = pygame.key.get_pressed()
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            basics.restart_button.detect_click(event)
            basics.main_menu_button.detect_click(event)
            if basics.VOLUME == 0:
                if basics.no_volume_button.detect_click(event) is True:
                    basics.VOLUME = basics.PREVOLUME
            else:
                if basics.full_volume_button.detect_click(event) is True:
                    basics.PREVOLUME = basics.VOLUME
                    basics.VOLUME = 0
            basics.resume_button.detect_click(event)
            if event.type == pygame.QUIT:
                run = False
            if key_pressed[pygame.K_SPACE]:
                basics.resume_button.clicked()

        WIN.blit(basics.pause_bg, (360 * basics.X_COEFFICIENT, 225 * basics.Y_COEFFICIENT))
        WIN.fill(basics.RED, basics.pause_rect)
        WIN.blit(basics.pause_text, (basics.pause_rect.x, basics.pause_rect.y))
        basics.resume_button.detect_mouse_collision()
        basics.restart_button.detect_mouse_collision()
        basics.main_menu_button.detect_mouse_collision()
        basics.full_volume_button.detect_mouse_collision()
        basics.restart_button.show()
        basics.main_menu_button.show()
        if basics.VOLUME == 0:
            basics.no_volume_button.show()
        else:
            basics.full_volume_button.show()
        basics.resume_button.show()
        pygame.display.update()

    pygame.quit()


def run_win(passed_level):
    from progress import get_values, change_values
    if passed_level not in basics.NAMES_PASSED_LEVELS:
        change_values(basics.LEVELS_PASSED + 1, passed_level)
        basics.LEVELS_PASSED, basics.NAMES_PASSED_LEVELS = get_values()
    run = True
    for music in basics.MUSICS:
        music.stop()
    basics.WIN_SOUND.play(0)

    while run:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            basics.next_level_button.detect_click(event)
            basics.menu_button.detect_click(event)
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(basics.BLACK)
        WIN.blit(basics.CUP, (220 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
        WIN.blit(basics.CUP, (1010 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
        WIN.blit(basics.LEVEL_TEXT, basics.LEVEL_RECT)
        WIN.blit(basics.COMPLETED_TEXT, basics.COMPLETED_RECT)
        basics.next_level_button.detect_mouse_collision()
        basics.menu_button.detect_mouse_collision()
        basics.next_level_button.show()
        basics.menu_button.show()
        pygame.display.update()

    pygame.quit()


def run_lose():
    run = True
    for music in basics.MUSICS:
        music.stop()
    basics.LOSE_SOUND.play(0)

    while run:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            basics.retry_button.detect_click(event)
            basics.menu_button.detect_click(event)
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(basics.BLACK)
        WIN.blit(basics.LOSE_SCREEN, (400 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
        basics.retry_button.detect_mouse_collision()
        basics.menu_button.detect_mouse_collision()
        basics.retry_button.show()
        basics.menu_button.show()
        pygame.display.update()

    pygame.quit()


def run_lvl1():
    basics.LAST_RUN = run_lvl1
    from lvl1 import lvl1_main
    lvl1_main()


def run_lvl2():
    basics.LAST_RUN = run_lvl2
    from lvl2 import lvl2_main
    lvl2_main()


def main():
    run_preview()
    pygame.quit()


if __name__ == "__main__":
    main()
