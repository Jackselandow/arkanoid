import pygame
import basics
from classes import Label, Image, Button, Shape
import progress
pygame.init()


def main_settings():
    if basics.SETTINGS_MUSIC.get_busy() is False:
        basics.SETTINGS_MUSIC.play(loops=-1)

    settings_bg = Image('backgrounds/settings_bg.jpg', (basics.WIN_RECT.right, basics.WIN_RECT.bottom), topleft=(0, 0))
    back_settings_button = Button(Label('<', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GRAY, topleft=(10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT)), None, key=pygame.K_ESCAPE, feedbacks=[basics.CLICK_SOUND1.play, basics.SETTINGS_MUSIC.stop, basics.PRELAST_RUN])
    main_settings_label = Label('MAIN SETTINGS', 150 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.YELLOW, center=(basics.WIN_RECT.width / 2, 100 * basics.Y_COEFFICIENT))
    general_settings_button = Button(Label('GENERAL', 120 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, topleft=(440 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT)), None, 'arrows', 'white', feedbacks=[basics.CLICK_SOUND1.play, general_settings])
    volume_settings_button = Button(Label('VOLUME', 120 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, topleft=(480 * basics.X_COEFFICIENT, 400 * basics.Y_COEFFICIENT)), None, 'arrows', 'white', feedbacks=[basics.CLICK_SOUND1.play, volume_settings])
    ball_shape_settings_button = Button(Label('BALL SHAPE', 120 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, topleft=(310 * basics.X_COEFFICIENT, 600 * basics.Y_COEFFICIENT)), None, 'arrows', 'white', feedbacks=[basics.CLICK_SOUND1.play, ball_shape_settings])
    while True:
        basics.CLOCK.tick(basics.FPS)
        settings_bg.show()
        main_settings_label.show()
        back_settings_button.all_in_one()
        general_settings_button.all_in_one()
        volume_settings_button.all_in_one()
        ball_shape_settings_button.all_in_one()
        pygame.event.pump()
        pygame.display.update()


def general_settings():
    settings_bg = Image('backgrounds/settings_bg.jpg', (basics.WIN_RECT.right, basics.WIN_RECT.bottom), topleft=(0, 0))
    back_general_settings_button = Button(Label('<', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GRAY, topleft=(10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT)), None, key=pygame.K_ESCAPE, feedbacks=[basics.CLICK_SOUND1.play, basics.LAST_RUN])
    general_settings_label = Label('GENERAL SETTINGS', 100 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.YELLOW, center=(basics.WIN_RECT.right / 2, 75 * basics.Y_COEFFICIENT))
    control_type_label = Label('CONTROL TYPE', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.width / 2, 175 * basics.Y_COEFFICIENT))
    keyboard_icon_button = Button(None, Image('objects/keyboard_icon.png', (300 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), topleft=(370 * basics.X_COEFFICIENT, 225 * basics.Y_COEFFICIENT)))
    mouse_icon_button = Button(None, Image('objects/mouse_icon.png', (100 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), topleft=(870 * basics.X_COEFFICIENT, 225 * basics.Y_COEFFICIENT)))
    select_circle = pygame.transform.scale(pygame.image.load('objects/select_circle.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    select_dot = pygame.transform.scale(pygame.image.load('objects/select_dot.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    shape_animation_label = Label('BALL SHAPE ANIMATION', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.width / 2, 525 * basics.Y_COEFFICIENT))
    switch_on_button = Button(None, Image('objects/switch_on.png', (250 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(595 * basics.X_COEFFICIENT, 575 * basics.Y_COEFFICIENT)))
    switch_off_button = Button(None, Image('objects/switch_off.png', (250 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(595 * basics.X_COEFFICIENT, 575 * basics.Y_COEFFICIENT)))
    while True:
        basics.CLOCK.tick(basics.FPS)
        settings_bg.show()
        general_settings_label.show()
        control_type_label.show()
        basics.WIN.blit(select_circle, (495 * basics.X_COEFFICIENT, 405 * basics.Y_COEFFICIENT))
        basics.WIN.blit(select_circle, (895 * basics.X_COEFFICIENT, 405 * basics.Y_COEFFICIENT))
        if basics.CONTROL_TYPE == 'keyboard':
            basics.WIN.blit(select_dot, (495 * basics.X_COEFFICIENT, 405 * basics.Y_COEFFICIENT))
        elif basics.CONTROL_TYPE == 'mouse':
            basics.WIN.blit(select_dot, (895 * basics.X_COEFFICIENT, 405 * basics.Y_COEFFICIENT))
        shape_animation_label.show()
        back_general_settings_button.all_in_one()
        if keyboard_icon_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            basics.CONTROL_TYPE = 'keyboard'
            progress.update_value('Preferences', 'control_type', None, f'"{basics.CONTROL_TYPE}"')
        if mouse_icon_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            basics.CONTROL_TYPE = 'mouse'
            progress.update_value('Preferences', 'control_type', None, f'"{basics.CONTROL_TYPE}"')
        if basics.SHAPE_ANIMATION and switch_on_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            basics.SHAPE_ANIMATION = False
            progress.update_value('Preferences', 'ball_shape_animation', None, f'{basics.SHAPE_ANIMATION}')
        elif not basics.SHAPE_ANIMATION and switch_off_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            basics.SHAPE_ANIMATION = True
            progress.update_value('Preferences', 'ball_shape_animation', None, f'{basics.SHAPE_ANIMATION}')
        pygame.event.pump()
        pygame.display.update()


def volume_settings():
    settings_bg = Image('backgrounds/settings_bg.jpg', (basics.WIN_RECT.right, basics.WIN_RECT.bottom), topleft=(0, 0))
    back_volume_settings_button = Button(Label('<', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GRAY, topleft=(10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT)), None, key=pygame.K_ESCAPE)
    volume_settings_label = Label('VOLUME SETTINGS', 100 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.YELLOW, center=(basics.WIN_RECT.right / 2, 75 * basics.Y_COEFFICIENT))
    general_volume_label = Label('GENERAL VOLUME', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 175 * basics.Y_COEFFICIENT))
    music_volume_label = Label('MUSIC VOLUME', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 400 * basics.Y_COEFFICIENT))
    sound_volume_label = Label('SOUND VOLUME', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, center=(basics.WIN_RECT.right / 2, 625 * basics.Y_COEFFICIENT))
    volume_bar = pygame.transform.scale(pygame.image.load('objects/volume_bar.png'), (680 * basics.X_COEFFICIENT, 110 * basics.Y_COEFFICIENT))
    red_square = pygame.transform.scale(pygame.image.load('objects/red_square.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT))
    minus_general_volume_button = Button(None, Image('objects/minus_volume.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(260 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT)))
    plus_general_volume_button = Button(None, Image('objects/plus_volume.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(1080 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT)))
    minus_music_volume_button = Button(None, Image('objects/minus_volume.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(260 * basics.X_COEFFICIENT, 425 * basics.Y_COEFFICIENT)))
    plus_music_volume_button = Button(None, Image('objects/plus_volume.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(1080 * basics.X_COEFFICIENT, 425 * basics.Y_COEFFICIENT)))
    minus_sound_volume_button = Button(None, Image('objects/minus_volume.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(260 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT)))
    plus_sound_volume_button = Button(None, Image('objects/plus_volume.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(1080 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT)))
    while True:
        basics.CLOCK.tick(basics.FPS)
        general_volume_square_x = 410
        music_volume_square_x = 410
        sound_volume_square_x = 410
        settings_bg.show()
        volume_settings_label.show()
        general_volume_label.show()
        music_volume_label.show()
        sound_volume_label.show()
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
        if back_volume_settings_button.all_in_one() is True:
            for music in basics.MUSICS:
                music.update()
            for sound in basics.SOUNDS:
                sound.update()
            basics.CLICK_SOUND1.play()
            basics.LAST_RUN()
        if minus_general_volume_button.all_in_one() is True and basics.VOLUME > 0:
            basics.PREVOLUME = basics.VOLUME = basics.VOLUME - 0.1
            progress.update_value('Volume', 'general', None, basics.VOLUME)
            basics.CLICK_SOUND1.play()
        if plus_general_volume_button.all_in_one() is True and basics.VOLUME < 1:
            basics.PREVOLUME = basics.VOLUME = basics.VOLUME + 0.1
            progress.update_value('Volume', 'general', None, basics.VOLUME)
            basics.CLICK_SOUND1.play()
        if minus_music_volume_button.all_in_one() is True and basics.MUSIC_VOLUME > 0:
            basics.MUSIC_VOLUME -= 0.1
            progress.update_value('Volume', 'music', None, basics.MUSIC_VOLUME)
            basics.CLICK_SOUND1.play()
        if plus_music_volume_button.all_in_one() is True and basics.MUSIC_VOLUME < 1:
            basics.MUSIC_VOLUME += 0.1
            progress.update_value('Volume', 'music', None, basics.MUSIC_VOLUME)
            basics.CLICK_SOUND1.play()
        if minus_sound_volume_button.all_in_one() is True and basics.SOUND_VOLUME > 0:
            basics.SOUND_VOLUME -= 0.1
            progress.update_value('Volume', 'sound', None, basics.SOUND_VOLUME)
            basics.CLICK_SOUND1.play()
        if plus_sound_volume_button.all_in_one() is True and basics.SOUND_VOLUME < 1:
            basics.SOUND_VOLUME += 0.1
            progress.update_value('Volume', 'sound', None, basics.SOUND_VOLUME)
            basics.CLICK_SOUND1.play()
        pygame.event.pump()
        pygame.display.update()
        basics.SETTINGS_MUSIC.update()
        basics.CLICK_SOUND1.update()


def ball_shape_settings():
    position = basics.BALL_SHAPES.index(basics.CURRENT_SHAPE)
    shape = Shape((620 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), basics.AVAILABLE_SHAPES.split(',')[position])
    shape_name_label = Label(shape.name, 75 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.GREEN, center=(basics.WIN_RECT.right / 2, 400 * basics.Y_COEFFICIENT))
    description_label = Label('Description:', 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.ORANGE, topleft=(50 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT))
    shape_description_label = Label(shape.description, 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.ORANGE, topleft=(50 * basics.X_COEFFICIENT, 520 * basics.Y_COEFFICIENT))

    settings_bg = Image('backgrounds/settings_bg.jpg', (basics.WIN_RECT.right, basics.WIN_RECT.bottom), topleft=(0, 0))
    back_ball_shape_settings_button = Button(Label('<', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, basics.GRAY, topleft=(10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT)), None, key=pygame.K_ESCAPE, feedbacks=[basics.CLICK_SOUND1.play, basics.LAST_RUN])
    ball_shape_settings_label = Label('BALL SHAPE', 100 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.YELLOW, center=(basics.WIN_RECT.right / 2, 75 * basics.Y_COEFFICIENT))
    previous_shape_button = Button(Label('<', 200 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, topleft=(496 * basics.X_COEFFICIENT, 193 * basics.Y_COEFFICIENT)), None, key=pygame.K_LEFT)
    next_shape_button = Button(Label('>', 200 * basics.FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', basics.RED, topleft=(850 * basics.X_COEFFICIENT, 193 * basics.Y_COEFFICIENT)), None, key=pygame.K_RIGHT)
    confirm_shape_button = Button(Label('CONFIRM', 100 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', basics.WHITE, basics.RED, topleft=(485.5 * basics.X_COEFFICIENT, 650 * basics.Y_COEFFICIENT)), None, key=pygame.K_SPACE)
    while True:
        basics.CLOCK.tick(basics.FPS)
        settings_bg.show()
        ball_shape_settings_label.show()
        description_label.show()
        shape_name_label.show()
        shape_description_label.show()
        confirm_shape_button.detect_mouse_collision()
        shape.update()
        basics.WIN.blit(shape.image, shape.rect)
        back_ball_shape_settings_button.all_in_one()
        if position > 0 and previous_shape_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            position -= 1
            shape = Shape((620 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), basics.AVAILABLE_SHAPES.split(',')[position])
            shape_name_label = Label(shape.name, 75 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.GREEN, center=(basics.WIN_RECT.right / 2, 400 * basics.Y_COEFFICIENT))
            shape_description_label = Label(shape.description, 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.ORANGE, topleft=(50 * basics.X_COEFFICIENT, 520 * basics.Y_COEFFICIENT))
        if position < len(basics.AVAILABLE_SHAPES.split(',')) - 1 and next_shape_button.all_in_one() is True:
            basics.CLICK_SOUND1.play()
            position += 1
            shape = Shape((620 * basics.X_COEFFICIENT, 150 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 200 * basics.Y_COEFFICIENT), basics.AVAILABLE_SHAPES.split(',')[position])
            shape_name_label = Label(shape.name, 75 * basics.FONT_COEFFICIENT, 'fonts/endless_font.ttf', basics.GREEN, center=(basics.WIN_RECT.right / 2, 400 * basics.Y_COEFFICIENT))
            shape_description_label = Label(shape.description, 50 * basics.FONT_COEFFICIENT, 'fonts/tales_font.ttf', basics.ORANGE, topleft=(50 * basics.X_COEFFICIENT, 520 * basics.Y_COEFFICIENT))
        if confirm_shape_button.all_in_one() is True:
            basics.CLICK_SOUND2.play()
            progress.update_value('Ball Shapes', 'current', None, f'"{shape.surf_name}"')
            basics.CURRENT_SHAPE = progress.get_value('Ball Shapes', 'current', None)
        pygame.event.pump()
        pygame.display.update()
