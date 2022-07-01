import pygame
import basics
from main import WIN
pygame.init()


def run_main_settings():
    for music in basics.MUSICS:
        music.update()
    from lvl1 import music
    music.update()
    for sound in basics.SOUNDS:
        sound.update()
    
    basics.LAST_RUN = run_main_settings
    run = True
    basics.menu_music.stop()
    if basics.settings_music.get_busy() is False:
        basics.settings_music.play(loops=-1)

    while run:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            basics.back_settings_button.detect_click(event)
            basics.volume_settings_button.detect_click(event)
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(basics.settings_bg, (0, 0))
        WIN.blit(basics.main_settings_text, basics.main_settings_rect)
        basics.back_settings_button.detect_mouse_collision()
        basics.volume_settings_button.detect_mouse_collision()
        basics.back_settings_button.show()
        basics.volume_settings_button.show()
        pygame.display.update()

    pygame.quit()


def run_volume_settings():
    run = True

    while run:
        basics.CLOCK.tick(basics.FPS)
        general_volume_square_x = 410
        music_volume_square_x = 410
        sound_volume_square_x = 410
        for event in pygame.event.get():
            basics.back_volume_settings_button.detect_click(event)
            if basics.minus_general_volume_button.detect_click(event) is True and basics.VOLUME > 0:
                basics.VOLUME -= 0.1
            if basics.plus_general_volume_button.detect_click(event) is True and basics.VOLUME < 1:
                basics.VOLUME += 0.1
            if basics.minus_music_volume_button.detect_click(event) is True and basics.MUSIC_VOLUME > 0:
                basics.MUSIC_VOLUME -= 0.1
            if basics.plus_music_volume_button.detect_click(event) is True and basics.MUSIC_VOLUME < 1:
                basics.MUSIC_VOLUME += 0.1
            if basics.minus_sound_volume_button.detect_click(event) is True and basics.SOUND_VOLUME > 0:
                basics.SOUND_VOLUME -= 0.1
            if basics.plus_sound_volume_button.detect_click(event) is True and basics.SOUND_VOLUME < 1:
                basics.SOUND_VOLUME += 0.1
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(basics.settings_bg, (0, 0))
        WIN.blit(basics.volume_settings_text, basics.volume_settings_rect)
        WIN.blit(basics.general_volume_text, basics.general_volume_rect)
        WIN.blit(basics.music_volume_text, basics.music_volume_rect)
        WIN.blit(basics.sound_volume_text, basics.sound_volume_rect)
        WIN.blit(basics.volume_bar, (380 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
        WIN.blit(basics.volume_bar, (380 * basics.X_COEFFICIENT, 425 * basics.Y_COEFFICIENT))
        WIN.blit(basics.volume_bar, (380 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT))
        for i in range(int(basics.VOLUME * 10)):
            WIN.blit(basics.red_square, (general_volume_square_x * basics.X_COEFFICIENT, 230 * basics.Y_COEFFICIENT))
            general_volume_square_x += 63
        for i in range(int(basics.MUSIC_VOLUME * 10)):
            WIN.blit(basics.red_square, (music_volume_square_x * basics.X_COEFFICIENT, 455 * basics.Y_COEFFICIENT))
            music_volume_square_x += 63
        for i in range(int(basics.SOUND_VOLUME * 10)):
            WIN.blit(basics.red_square, (sound_volume_square_x * basics.X_COEFFICIENT, 680 * basics.Y_COEFFICIENT))
            sound_volume_square_x += 63
        basics.back_volume_settings_button.detect_mouse_collision()
        basics.minus_general_volume_button.detect_mouse_collision()
        basics.plus_general_volume_button.detect_mouse_collision()
        basics.minus_music_volume_button.detect_mouse_collision()
        basics.plus_music_volume_button.detect_mouse_collision()
        basics.minus_sound_volume_button.detect_mouse_collision()
        basics.plus_sound_volume_button.detect_mouse_collision()
        basics.back_volume_settings_button.show()
        basics.minus_general_volume_button.show()
        basics.plus_general_volume_button.show()
        basics.minus_music_volume_button.show()
        basics.plus_music_volume_button.show()
        basics.minus_sound_volume_button.show()
        basics.plus_sound_volume_button.show()
        pygame.display.update()
        basics.settings_music.update()
        basics.CLICK_SOUND.update()

    pygame.quit()
