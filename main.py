import pygame
import basics
pygame.init()


def run_preview():
    preview_bg = pygame.transform.scale(pygame.image.load('backgrounds/preview_bg1.png'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom))
    basics.LAST_RUN = run_preview
    alpha = 255
    while alpha != -5:
        alpha -= 10
        basics.CLOCK.tick(basics.FPS)
        basics.BLACK_SCREEN.set_alpha(alpha)
        basics.WIN.blit(preview_bg, (0, 0))
        basics.WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()
    pygame.time.wait(1000)
    while alpha != 255:
        alpha += 10
        basics.CLOCK.tick(basics.FPS)
        basics.BLACK_SCREEN.set_alpha(alpha)
        basics.WIN.blit(preview_bg, (0, 0))
        basics.WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()
    run_menu()


def run_menu():
    if basics.LAST_RUN == run_preview:
        alpha = 255
    else:
        alpha = -5
    basics.LAST_RUN = run_menu
    basics.PRELAST_RUN = basics.LAST_RUN
    for music in basics.MUSICS:
        music.stop()
    basics.MENU_MUSIC.play(loops=-1)

    menu_bg = pygame.transform.scale(pygame.image.load('backgrounds/menu_bg.jpeg'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom))
    arkanoid_logo = pygame.transform.scale(pygame.image.load('objects/arkanoid_logo.png'), (1400 * basics.X_COEFFICIENT, 300 * basics.Y_COEFFICIENT))
    author_text = basics.TALES_FONT.render('Jackselandow Edition', False, basics.WHITE)
    author_rect = author_text.get_rect(topleft=(0, 5 * basics.Y_COEFFICIENT))
    play_button = basics.TextButton('PLAY', (440 * basics.X_COEFFICIENT, 370 * basics.Y_COEFFICIENT), 300 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.WHITE, basics.RED, ['none'])
    settings_button = basics.TextButton('SETTINGS', (560 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT), 60 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.GREEN, [basics.CLICK_SOUND1.play, basics.run_main_settings])
    levels_button = basics.TextButton('LEVELS', (600 * basics.X_COEFFICIENT, 660 * basics.Y_COEFFICIENT), 60 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.BLUE, [basics.CLICK_SOUND1.play, basics.run_levels_menu])
    exit_button = basics.TextButton('EXIT', (640 * basics.X_COEFFICIENT, 750 * basics.Y_COEFFICIENT), 60 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.GREY, [basics.CLICK_SOUND1.play, exit])
    version_text = basics.TALES_FONT.render('Version 3.0', False, basics.BLACK)
    version_rect = version_text.get_rect(bottomright=(basics.WIN_RECT.right - 8 * basics.X_COEFFICIENT, basics.WIN_RECT.bottom))
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            if play_button.detect_click(event) is True:
                if len(basics.PASSED_LEVELS_LIST) == len(basics.LEVELS_ICONS):
                    basics.LEVELS_ICONS[-1].clicked()
                else:
                    index = len(basics.PASSED_LEVELS_LIST)
                    basics.LEVELS_ICONS[index].clicked()
            levels_button.detect_click(event)
            settings_button.detect_click(event)
            exit_button.detect_click(event)

        basics.WIN.blit(menu_bg, (0, 0))
        basics.WIN.blit(arkanoid_logo, (20 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
        basics.WIN.blit(author_text, author_rect)
        basics.WIN.blit(version_text, version_rect)
        play_button.detect_mouse_collision()
        levels_button.detect_mouse_collision()
        settings_button.detect_mouse_collision()
        exit_button.detect_mouse_collision()
        play_button.show()
        levels_button.show()
        settings_button.show()
        exit_button.show()
        if alpha != -5:
            alpha -= 10
            basics.BLACK_SCREEN.set_alpha(alpha)
            basics.WIN.blit(basics.BLACK_SCREEN, (0, 0))
        pygame.display.update()


def run_pause():
    pygame.mixer.pause()
    basics.PAUSE_IN_SOUND.play()
    transparent_bg = basics.BLACK_SCREEN
    transparent_bg.set_alpha(120)
    basics.WIN.blit(transparent_bg, (0, 0))

    pause_bg = pygame.transform.scale(pygame.image.load('backgrounds/pause_bg.png'), (basics.WIN_RECT.right / 2, basics.WIN_RECT.bottom / 2))
    pause_text = basics.BIG_PIXEBOY_FONT.render('GAME PAUSED', False, basics.WHITE)
    pause_rect = pause_text.get_rect(center=(basics.WIN_RECT.right / 2, 300 * basics.Y_COEFFICIENT))
    restart_button = basics.ImageButton('objects/restart_button.png', (430 * basics.X_COEFFICIENT, 370 * basics.Y_COEFFICIENT), (180 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), ['PRELAST_RUN'])
    main_menu_button = basics.ImageButton('objects/main_menu_button.png', (630 * basics.X_COEFFICIENT, 370 * basics.Y_COEFFICIENT), (180 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), ['none'])
    full_volume_button = basics.ImageButton('objects/full_volume_button.png', (830 * basics.X_COEFFICIENT, 370 * basics.Y_COEFFICIENT), (180 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), ['none'])
    no_volume_button = basics.ImageButton('objects/no_volume_button.png', (830 * basics.X_COEFFICIENT, 370 * basics.Y_COEFFICIENT), (180 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), ['none'])
    resume_button = basics.TextButton('RESUME', (540 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT), 130 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.DARK_GREEN, basics.GREEN, ['none'])
    while True:
        key_pressed = pygame.key.get_pressed()
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            restart_button.detect_click(event)
            if main_menu_button.detect_click(event) is True:
                for buff in basics.LEVEL.active_buffs:
                    if buff.timer:
                        buff.timer.cancel()
                run_menu()
            if basics.VOLUME == 0:
                if no_volume_button.detect_click(event) is True:
                    basics.VOLUME = basics.PREVOLUME
            else:
                if full_volume_button.detect_click(event) is True:
                    basics.PREVOLUME = basics.VOLUME
                    basics.VOLUME = 0
            if resume_button.detect_click(event) is True or key_pressed[pygame.K_SPACE]:
                if basics.LEVEL.level_started is True:
                    basics.LEVEL.countdown_state = True
                    basics.LEVEL.countdown_index = 0
                else:
                    basics.PAUSE_OUT_SOUND.play()
                    pygame.mixer.unpause()
                basics.LAST_RUN()

        basics.WIN.blit(pause_bg, (360 * basics.X_COEFFICIENT, 225 * basics.Y_COEFFICIENT))
        basics.WIN.fill(basics.RED, pause_rect)
        basics.WIN.blit(pause_text, (pause_rect.x, pause_rect.y))
        resume_button.detect_mouse_collision()
        restart_button.detect_mouse_collision()
        main_menu_button.detect_mouse_collision()
        full_volume_button.detect_mouse_collision()
        restart_button.show()
        main_menu_button.show()
        if basics.VOLUME == 0:
            no_volume_button.show()
        else:
            full_volume_button.show()
        resume_button.show()
        pygame.display.update()


def run_countdown():
    three = pygame.transform.scale(pygame.image.load('objects/countdown/three.png'), (160 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    two = pygame.transform.scale(pygame.image.load('objects/countdown/two.png'), (160 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    one = pygame.transform.scale(pygame.image.load('objects/countdown/one.png'), (76 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    go = pygame.transform.scale(pygame.image.load('objects/countdown/go.png'), (451 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    countdown = [three, two, one, go]

    basics.LEVEL.countdown_state = 'process'
    x = 640 * basics.X_COEFFICIENT
    if basics.LEVEL.countdown_index == 2:
        x = 682 * basics.X_COEFFICIENT
    if basics.LEVEL.countdown_index == 3:
        x = 494.5 * basics.X_COEFFICIENT
        basics.PAUSE_OUT_SOUND.play()
    else:
        basics.COUNTDOWN_SOUND.play()
    basics.WIN.blit(countdown[basics.LEVEL.countdown_index], (x, 350 * basics.Y_COEFFICIENT))
    pygame.display.update()
    pygame.time.wait(600)
    pygame.display.update()
    if basics.LEVEL.countdown_index == 3:
        basics.LEVEL.countdown_state = False
        pygame.mixer.unpause()
    basics.LAST_RUN()


def run_win(passed_level):
    for buff in basics.LEVEL.active_buffs:
        if buff.timer:
            buff.timer.cancel()
    passed_state = basics.update_game_progress(passed_level)
    for music in basics.MUSICS:
        music.stop()
    basics.WIN_SOUND.play()

    cup = pygame.transform.scale(pygame.image.load('objects/cup.png'), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    level_text = basics.BIG_PIXELOID_FONT.render('LEVEL', False, basics.WHITE)
    level_rect = level_text.get_rect(center=(basics.WIN_RECT.right / 2, 150 * basics.Y_COEFFICIENT))
    completed_text = basics.BIG_PIXELOID_FONT.render('COMPLETED', False, basics.WHITE)
    completed_rect = completed_text.get_rect(center=(basics.WIN_RECT.right / 2, 270 * basics.Y_COEFFICIENT))
    next_level_button = basics.TextButton('NEXT LEVEL', (470 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT), 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.GREEN, basics.BLACK, ['none'])
    menu_button = basics.TextButton('MAIN MENU', (495 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT), 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.GREY, basics.BLACK, [basics.CLICK_SOUND1.play, basics.WIN_SOUND.stop, basics.LOSE_SOUND.stop, run_menu])
    shape_unlocked_text = basics.PIXELOID_FONT.render('NEW BALL SHAPE UNLOCKED!', False, basics.RED)
    shape_unlocked_rect = shape_unlocked_text.get_rect(bottomleft=(basics.WIN_RECT.width, basics.WIN_RECT.bottom))
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            if len(basics.PASSED_LEVELS_LIST) != len(basics.LEVELS_ICONS):
                if next_level_button.detect_click(event) is True:
                    basics.LEVELS_ICONS[int(passed_level)].clicked()
            menu_button.detect_click(event)

        basics.WIN.fill(basics.BLACK)
        basics.WIN.blit(cup, (220 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
        basics.WIN.blit(cup, (1010 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
        basics.WIN.blit(level_text, level_rect)
        basics.WIN.blit(completed_text, completed_rect)
        if len(basics.PASSED_LEVELS_LIST) != len(basics.LEVELS_ICONS):
            next_level_button.detect_mouse_collision()
            next_level_button.show()
        menu_button.detect_mouse_collision()
        menu_button.show()
        if passed_state is True:
            basics.WIN.blit(shape_unlocked_text, shape_unlocked_rect)
            shape_unlocked_rect.x -= 5
        pygame.display.update()


def run_lose():
    for buff in basics.LEVEL.active_buffs:
        if buff.timer:
            buff.timer.cancel()
    for music in basics.MUSICS:
        music.stop()
    basics.LOSE_SOUND.play()

    lose_screen = pygame.transform.scale(pygame.image.load('objects/lose.png'), (640 * basics.X_COEFFICIENT, 320 * basics.Y_COEFFICIENT))
    menu_button = basics.TextButton('MAIN MENU', (495 * basics.X_COEFFICIENT, 570 * basics.Y_COEFFICIENT), 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.GREY, basics.BLACK, [basics.CLICK_SOUND1.play, basics.WIN_SOUND.stop, basics.LOSE_SOUND.stop, run_menu])
    retry_button = basics.TextButton('RETRY', (595 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT), 75 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.RED, basics.BLACK, [basics.CLICK_SOUND1.play, 'PRELAST_RUN'])
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            retry_button.detect_click(event)
            menu_button.detect_click(event)

        basics.WIN.fill(basics.BLACK)
        basics.WIN.blit(lose_screen, (400 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
        retry_button.detect_mouse_collision()
        menu_button.detect_mouse_collision()
        retry_button.show()
        menu_button.show()
        pygame.display.update()


def run_lvl1():
    basics.LAST_RUN = run_lvl1
    from lvl1 import lvl1_main
    lvl1_main()


def run_lvl2():
    basics.LAST_RUN = run_lvl2
    from lvl2 import lvl2_main
    lvl2_main()


def run_lvl3():
    basics.LAST_RUN = run_lvl3
    from lvl3 import lvl3_main
    lvl3_main()


def main():
    run_preview()


if __name__ == "__main__":
    main()
