import pygame
import basics
pygame.init()


def run_main_settings():
    for music in basics.MUSICS:
        music.update()
    for sound in basics.SOUNDS:
        sound.update()
    
    basics.LAST_RUN = run_main_settings
    basics.MENU_MUSIC.stop()
    if basics.SETTINGS_MUSIC.get_busy() is False:
        basics.SETTINGS_MUSIC.play(loops=-1)

    settings_bg = pygame.transform.scale(pygame.image.load('backgrounds/settings_bg.jpg'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom))
    back_settings_button = basics.TextButton('<', (10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT), 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GREY, [basics.CLICK_SOUND1.play, 'PRELAST_RUN'])
    main_settings_text = basics.BIG_ENDLESS_FONT.render('MAIN SETTINGS', False, basics.YELLOW)
    main_settings_rect = main_settings_text.get_rect(center=(basics.WIN_RECT.right / 2, 100 * basics.Y_COEFFICIENT))
    general_settings_button = basics.TextButton('GENERAL', (440 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), 120 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, 'none', [basics.CLICK_SOUND1.play, run_general_settings])
    volume_settings_button = basics.TextButton('VOLUME', (480 * basics.X_COEFFICIENT, 400 * basics.Y_COEFFICIENT), 120 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, 'none', [basics.CLICK_SOUND1.play, run_volume_settings])
    ball_shape_settings_button = basics.TextButton('BALL SHAPE', (310 * basics.X_COEFFICIENT, 600 * basics.Y_COEFFICIENT), 120 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, 'none', [basics.CLICK_SOUND1.play, run_ball_shape_settings])
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            back_settings_button.detect_click(event)
            general_settings_button.detect_click(event)
            volume_settings_button.detect_click(event)
            ball_shape_settings_button.detect_click(event)

        basics.WIN.blit(settings_bg, (0, 0))
        basics.WIN.blit(main_settings_text, main_settings_rect)
        back_settings_button.detect_mouse_collision()
        general_settings_button.detect_mouse_collision()
        volume_settings_button.detect_mouse_collision()
        ball_shape_settings_button.detect_mouse_collision()
        back_settings_button.show()
        general_settings_button.show()
        volume_settings_button.show()
        ball_shape_settings_button.show()
        pygame.display.update()


def run_general_settings():
    settings_bg = pygame.transform.scale(pygame.image.load('backgrounds/settings_bg.jpg'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom))
    back_general_settings_button = basics.TextButton('<', (10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT), 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GREY, [basics.CLICK_SOUND1.play, 'LAST_RUN'])
    general_settings_text = basics.ENDLESS_FONT.render('GENERAL SETTINGS', False, basics.YELLOW)
    general_settings_rect = general_settings_text.get_rect(center=(basics.WIN_RECT.right / 2, 75 * basics.Y_COEFFICIENT))
    control_type_text = basics.PIXELOID_FONT.render('CONTROL TYPE', False, basics.WHITE)
    control_type_rect = control_type_text.get_rect(center=(basics.WIN_RECT.width / 2, 175 * basics.Y_COEFFICIENT))
    keyboard_icon_button = basics.ImageButton('objects/keyboard_icon.png', (370 * basics.X_COEFFICIENT, 300 * basics.Y_COEFFICIENT), (300 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    mouse_icon_button = basics.ImageButton('objects/mouse_icon.png', (870 * basics.X_COEFFICIENT, 300 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    select_circle = pygame.transform.scale(pygame.image.load('objects/select_circle.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    select_dot = pygame.transform.scale(pygame.image.load('objects/select_dot.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            back_general_settings_button.detect_click(event)
            if keyboard_icon_button.detect_click(event) is True:
                basics.CONTROL_TYPE = 'keyboard'
                basics.update_value('Preferences', 'control_type', None, f'"{basics.CONTROL_TYPE}"')
            if mouse_icon_button.detect_click(event) is True:
                basics.CONTROL_TYPE = 'mouse'
                basics.update_value('Preferences', 'control_type', None, f'"{basics.CONTROL_TYPE}"')

        basics.WIN.blit(settings_bg, (0, 0))
        basics.WIN.blit(general_settings_text, general_settings_rect)
        basics.WIN.blit(control_type_text, control_type_rect)
        basics.WIN.blit(select_circle, (495 * basics.X_COEFFICIENT, 480 * basics.Y_COEFFICIENT))
        basics.WIN.blit(select_circle, (895 * basics.X_COEFFICIENT, 480 * basics.Y_COEFFICIENT))
        if basics.CONTROL_TYPE == 'keyboard':
            basics.WIN.blit(select_dot, (495 * basics.X_COEFFICIENT, 480 * basics.Y_COEFFICIENT))
        elif basics.CONTROL_TYPE == 'mouse':
            basics.WIN.blit(select_dot, (895 * basics.X_COEFFICIENT, 480 * basics.Y_COEFFICIENT))
        back_general_settings_button.detect_mouse_collision()
        keyboard_icon_button.detect_mouse_collision()
        mouse_icon_button.detect_mouse_collision()
        back_general_settings_button.show()
        keyboard_icon_button.show()
        mouse_icon_button.show()
        pygame.display.update()


def run_volume_settings():
    settings_bg = pygame.transform.scale(pygame.image.load('backgrounds/settings_bg.jpg'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom))
    back_volume_settings_button = basics.TextButton('<', (10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT), 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GREY, [basics.CLICK_SOUND1.play, 'LAST_RUN'])
    volume_settings_text = basics.ENDLESS_FONT.render('VOLUME SETTINGS', False, basics.YELLOW)
    volume_settings_rect = volume_settings_text.get_rect(center=(basics.WIN_RECT.right / 2, 75 * basics.Y_COEFFICIENT))
    general_volume_text = basics.PIXELOID_FONT.render('GENERAL VOLUME', False, basics.WHITE)
    general_volume_rect = general_volume_text.get_rect(center=(basics.WIN_RECT.right / 2, 175 * basics.Y_COEFFICIENT))
    music_volume_text = basics.PIXELOID_FONT.render('MUSIC VOLUME', False, basics.WHITE)
    music_volume_rect = music_volume_text.get_rect(center=(basics.WIN_RECT.right / 2, 400 * basics.Y_COEFFICIENT))
    sound_volume_text = basics.PIXELOID_FONT.render('SOUND VOLUME', False, basics.WHITE)
    sound_volume_rect = sound_volume_text.get_rect(center=(basics.WIN_RECT.right / 2, 625 * basics.Y_COEFFICIENT))
    volume_bar = pygame.transform.scale(pygame.image.load('objects/volume_bar.png'), (680 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
    red_square = pygame.transform.scale(pygame.image.load('objects/red_square.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    minus_general_volume_button = basics.ImageButton('objects/minus_volume.png', (260 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    plus_general_volume_button = basics.ImageButton('objects/plus_volume.png', (1080 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    minus_music_volume_button = basics.ImageButton('objects/minus_volume.png', (260 * basics.X_COEFFICIENT, 425 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    plus_music_volume_button = basics.ImageButton('objects/plus_volume.png', (1080 * basics.X_COEFFICIENT, 425 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    minus_sound_volume_button = basics.ImageButton('objects/minus_volume.png', (260 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])
    plus_sound_volume_button = basics.ImageButton('objects/plus_volume.png', (1080 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.CLICK_SOUND1.play, 'none'])

    while True:
        basics.CLOCK.tick(basics.FPS)
        general_volume_square_x = 410
        music_volume_square_x = 410
        sound_volume_square_x = 410
        for event in pygame.event.get():
            back_volume_settings_button.detect_click(event)
            if minus_general_volume_button.detect_click(event) is True and basics.VOLUME > 0:
                basics.PREVOLUME = basics.VOLUME = basics.VOLUME - 0.1
                basics.update_value('Volume', 'general', None, basics.VOLUME)
            if plus_general_volume_button.detect_click(event) is True and basics.VOLUME < 1:
                basics.PREVOLUME = basics.VOLUME = basics.VOLUME + 0.1
                basics.update_value('Volume', 'general', None, basics.VOLUME)
            if minus_music_volume_button.detect_click(event) is True and basics.MUSIC_VOLUME > 0:
                basics.MUSIC_VOLUME -= 0.1
                basics.update_value('Volume', 'music', None, basics.MUSIC_VOLUME)
            if plus_music_volume_button.detect_click(event) is True and basics.MUSIC_VOLUME < 1:
                basics.MUSIC_VOLUME += 0.1
                basics.update_value('Volume', 'music', None, basics.MUSIC_VOLUME)
            if minus_sound_volume_button.detect_click(event) is True and basics.SOUND_VOLUME > 0:
                basics.SOUND_VOLUME -= 0.1
                basics.update_value('Volume', 'sound', None, basics.SOUND_VOLUME)
            if plus_sound_volume_button.detect_click(event) is True and basics.SOUND_VOLUME < 1:
                basics.SOUND_VOLUME += 0.1
                basics.update_value('Volume', 'sound', None, basics.SOUND_VOLUME)

        basics.WIN.blit(settings_bg, (0, 0))
        basics.WIN.blit(volume_settings_text, volume_settings_rect)
        basics.WIN.blit(general_volume_text, general_volume_rect)
        basics.WIN.blit(music_volume_text, music_volume_rect)
        basics.WIN.blit(sound_volume_text, sound_volume_rect)
        basics.WIN.blit(volume_bar, (380 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT))
        basics.WIN.blit(volume_bar, (380 * basics.X_COEFFICIENT, 425 * basics.Y_COEFFICIENT))
        basics.WIN.blit(volume_bar, (380 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT))
        for i in range(int(basics.VOLUME * 10)):
            basics.WIN.blit(red_square, (general_volume_square_x * basics.X_COEFFICIENT, 230 * basics.Y_COEFFICIENT))
            general_volume_square_x += 63
        for i in range(int(basics.MUSIC_VOLUME * 10)):
            basics.WIN.blit(red_square, (music_volume_square_x * basics.X_COEFFICIENT, 455 * basics.Y_COEFFICIENT))
            music_volume_square_x += 63
        for i in range(int(basics.SOUND_VOLUME * 10)):
            basics.WIN.blit(red_square, (sound_volume_square_x * basics.X_COEFFICIENT, 680 * basics.Y_COEFFICIENT))
            sound_volume_square_x += 63
        back_volume_settings_button.detect_mouse_collision()
        minus_general_volume_button.detect_mouse_collision()
        plus_general_volume_button.detect_mouse_collision()
        minus_music_volume_button.detect_mouse_collision()
        plus_music_volume_button.detect_mouse_collision()
        minus_sound_volume_button.detect_mouse_collision()
        plus_sound_volume_button.detect_mouse_collision()
        back_volume_settings_button.show()
        minus_general_volume_button.show()
        plus_general_volume_button.show()
        minus_music_volume_button.show()
        plus_music_volume_button.show()
        minus_sound_volume_button.show()
        plus_sound_volume_button.show()
        pygame.display.update()
        basics.SETTINGS_MUSIC.update()
        basics.CLICK_SOUND1.update()


def run_ball_shape_settings():
    position = basics.BALL_SHAPES.index(basics.CURRENT_SHAPE)
    shape = basics.Shape((620 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), basics.AVAILABLE_SHAPES.split(',')[position])
    shape_name_text = basics.SMALL_ENDLESS_FONT.render(shape.name, False, basics.GREEN)
    shape_name_rect = shape_name_text.get_rect(center=(basics.WIN_RECT.width / 2, 400 * basics.Y_COEFFICIENT))
    description_text = basics.TALES_FONT.render('Description:', False, basics.ORANGE)
    description_rect = description_text.get_rect(topleft=(50 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT))
    shape_description_text = basics.TALES_FONT.render(shape.description, False, basics.ORANGE)
    shape_description_rect = shape_description_text.get_rect(topleft=(50 * basics.X_COEFFICIENT, 520 * basics.Y_COEFFICIENT))

    settings_bg = pygame.transform.scale(pygame.image.load('backgrounds/settings_bg.jpg'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom))
    back_ball_shape_settings_button = basics.TextButton('<', (10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT), 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GREY, [basics.CLICK_SOUND1.play, 'LAST_RUN'])
    ball_shape_settings_text = basics.ENDLESS_FONT.render('BALL SHAPE', False, basics.YELLOW)
    ball_shape_settings_rect = ball_shape_settings_text.get_rect(center=(basics.WIN_RECT.right / 2, 75 * basics.Y_COEFFICIENT))
    previous_shape_button = basics.TextButton('<', (496 * basics.X_COEFFICIENT, 193 * basics.Y_COEFFICIENT), 200 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, 'none', [basics.CLICK_SOUND1.play, 'none'])
    next_shape_button = basics.TextButton('>', (850 * basics.X_COEFFICIENT, 193 * basics.Y_COEFFICIENT), 200 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, 'none', [basics.CLICK_SOUND1.play, 'none'])
    confirm_shape_button = basics.TextButton('CONFIRM', (485.5 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT), 100 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.RED, [basics.CLICK_SOUND2.play, 'none'])
    while True:
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            back_ball_shape_settings_button.detect_click(event)
            if position > 0 and previous_shape_button.detect_click(event) is True:
                position -= 1
                shape = basics.Shape((620 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), basics.AVAILABLE_SHAPES.split(',')[position])
                shape_name_text = basics.SMALL_ENDLESS_FONT.render(shape.name, False, basics.GREEN)
                shape_name_rect = shape_name_text.get_rect(center=(basics.WIN_RECT.width / 2, 400 * basics.Y_COEFFICIENT))
                shape_description_text = basics.TALES_FONT.render(shape.description, False, basics.ORANGE)
                shape_description_rect = shape_description_text.get_rect(topleft=(50 * basics.X_COEFFICIENT, 520 * basics.Y_COEFFICIENT))
            if position < len(basics.AVAILABLE_SHAPES.split(',')) - 1 and next_shape_button.detect_click(event) is True:
                position += 1
                shape = basics.Shape((620 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), basics.AVAILABLE_SHAPES.split(',')[position])
                shape_name_text = basics.SMALL_ENDLESS_FONT.render(shape.name, False, basics.GREEN)
                shape_name_rect = shape_name_text.get_rect(center=(basics.WIN_RECT.width / 2, 400 * basics.Y_COEFFICIENT))
                shape_description_text = basics.TALES_FONT.render(shape.description, False, basics.ORANGE)
                shape_description_rect = shape_description_text.get_rect(topleft=(50 * basics.X_COEFFICIENT, 520 * basics.Y_COEFFICIENT))
            if confirm_shape_button.detect_click(event) is True:
                basics.update_value('Ball Shapes', 'current', None, f'"{shape.surf_name}"')
                basics.CURRENT_SHAPE = basics.get_value('Ball Shapes', 'current', None)

        basics.WIN.blit(settings_bg, (0, 0))
        basics.WIN.blit(ball_shape_settings_text, ball_shape_settings_rect)
        basics.WIN.blit(description_text, description_rect)
        basics.WIN.blit(shape_name_text, shape_name_rect)
        basics.WIN.blit(shape_description_text, shape_description_rect)
        back_ball_shape_settings_button.detect_mouse_collision()
        confirm_shape_button.detect_mouse_collision()
        shape.show()
        back_ball_shape_settings_button.show()
        confirm_shape_button.show()
        if position > 0:
            previous_shape_button.detect_mouse_collision()
            previous_shape_button.show()
        if position < len(basics.AVAILABLE_SHAPES.split(',')) - 1:
            next_shape_button.detect_mouse_collision()
            next_shape_button.show()

        pygame.display.update()
