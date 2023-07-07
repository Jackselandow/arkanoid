import pygame
import basics
from main import run_menu
from classes import Label, Image, Button
pygame.init()


def pause():
    pygame.mixer.pause()
    basics.PAUSE_IN_SOUND.play()
    transparent_bg = basics.BLACK_SCREEN
    transparent_bg.set_alpha(120)
    basics.WIN.blit(transparent_bg, (0, 0))

    pause_bg = Image('backgrounds/pause_bg.png', (810 * basics.X_COEFFICIENT, 562.5 * basics.Y_COEFFICIENT), center=(basics.WIN_RECT.right / 2, basics.WIN_RECT.bottom / 2))
    pause_label = Label('GAME PAUSED', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 330 * basics.Y_COEFFICIENT))
    restart_button = Button(None, Image('objects/restart_button.png', (162 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), topleft=(440 * basics.X_COEFFICIENT, 420 * basics.Y_COEFFICIENT)), feedbacks=[pygame.mixer.stop, basics.PRELAST_RUN])
    main_menu_button = Button(None, Image('objects/main_menu_button.png', (162 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), topleft=(639 * basics.X_COEFFICIENT, 420 * basics.Y_COEFFICIENT)), key=pygame.K_ESCAPE)
    full_volume_button = Button(None, Image('objects/full_volume_button.png', (162 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), topleft=(838 * basics.X_COEFFICIENT, 420 * basics.Y_COEFFICIENT)))
    no_volume_button = Button(None, Image('objects/no_volume_button.png', (162 * basics.X_COEFFICIENT, 180 * basics.Y_COEFFICIENT), topleft=(838 * basics.X_COEFFICIENT, 420 * basics.Y_COEFFICIENT)))
    resume_button = Button(Label('RESUME', 130 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.GREEN, center=(basics.WIN_RECT.right / 2, 670 * basics.Y_COEFFICIENT)), None, key=pygame.K_SPACE)
    while True:
        basics.CLOCK.tick(basics.FPS)
        pause_bg.show()
        pause_label.show()
        restart_button.all_in_one()
        if main_menu_button.all_in_one() is True:
            pygame.mixer.stop()
            for buff in basics.LEVEL.active_buffs_group:
                if buff.timer:
                    buff.timer.cancel()
            run_menu()
        if basics.VOLUME == 0:
            if no_volume_button.all_in_one() is True:
                basics.VOLUME = basics.PREVOLUME
                for music in basics.MUSICS:
                    music.update()
                for sound in basics.SOUNDS:
                    sound.update()
        else:
            if full_volume_button.all_in_one() is True:
                basics.PREVOLUME = basics.VOLUME
                basics.VOLUME = 0
                for music in basics.MUSICS:
                    music.update()
                for sound in basics.SOUNDS:
                    sound.update()
        if resume_button.all_in_one() is True:
            if basics.LEVEL.started is True:
                basics.LEVEL.countdown_state = True
                basics.LEVEL.countdown_index = 0
            else:
                basics.PAUSE_OUT_SOUND.play()
                pygame.mixer.unpause()
            basics.LAST_RUN()
        pygame.event.pump()
        pygame.display.update()


def countdown():
    three = pygame.transform.scale(pygame.image.load('objects/countdown/three.png'), (160 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    two = pygame.transform.scale(pygame.image.load('objects/countdown/two.png'), (160 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    one = pygame.transform.scale(pygame.image.load('objects/countdown/one.png'), (76 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    go = pygame.transform.scale(pygame.image.load('objects/countdown/go.png'), (451 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
    countdown_list = [three, two, one, go]

    basics.LEVEL.countdown_state = 'process'
    x = 640 * basics.X_COEFFICIENT
    if basics.LEVEL.countdown_index == 2:
        x = 682 * basics.X_COEFFICIENT
    if basics.LEVEL.countdown_index == 3:
        x = 494.5 * basics.X_COEFFICIENT
        basics.PAUSE_OUT_SOUND.play()
    else:
        basics.COUNTDOWN_SOUND.play()
    basics.WIN.blit(countdown_list[basics.LEVEL.countdown_index], (x, 350 * basics.Y_COEFFICIENT))
    pygame.display.update()
    pygame.time.wait(600)
    pygame.display.update()
    if basics.LEVEL.countdown_index == 3:
        basics.LEVEL.countdown_state = False
        pygame.mixer.unpause()
    basics.LAST_RUN()
