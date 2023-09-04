import pygame as pg
from arkanoid import constants, progress
from arkanoid.classes import Label, Image, Button, Shape
pg.init()


def run_main_settings(func_name='run_main_settings'):
    desired_func = None
    constants.SETTINGS_MUSIC.play(-1)
    settings_bg = Image('arkanoid/resources/graphics/backgrounds/settings_menu.jpg', (constants.WIN_RECT.right, constants.WIN_RECT.bottom), topleft=(0, 0))
    back_settings_button = Button(Label('<', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', 'gray49', topleft=(10 * constants.X_COEFFICIENT, 10 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_ESCAPE, feedback='constants.SETTINGS_MUSIC.stop()\ndesired_func = "run_main_menu"\noutput = desired_func')
    main_settings_label = Label('MAIN SETTINGS', 150 * constants.FONT_COEFFICIENT, 'endless', 'yellow', center=(constants.WIN_RECT.width / 2, 100 * constants.Y_COEFFICIENT))
    general_settings_button = Button(Label('GENERAL', 120 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', topleft=(440 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)), 'white_arrows', feedback='desired_func = run_general_settings()\noutput = desired_func')
    volume_settings_button = Button(Label('VOLUME', 120 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', topleft=(480 * constants.X_COEFFICIENT, 400 * constants.Y_COEFFICIENT)), 'white_arrows', feedback='desired_func = run_volume_settings()\noutput = desired_func')
    ball_shape_settings_button = Button(Label('BALL SHAPE', 120 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', topleft=(310 * constants.X_COEFFICIENT, 600 * constants.Y_COEFFICIENT)), 'white_arrows', feedback='desired_func = run_ball_shape_settings()\noutput = desired_func')
    while True:
        constants.CLOCK.tick(constants.FPS)
        events = pg.event.get()
        globs = globals()
        locs = locals()
        for event in events:
            if event.type == pg.QUIT:
                pg.mixer.fadeout(850)
                desired_func = 'quit'
        settings_bg.show()
        main_settings_label.show()
        if output := back_settings_button.update(events, globs, locs): desired_func = output
        if output := general_settings_button.update(events, globs, locs): desired_func = output
        if output := volume_settings_button.update(events, globs, locs): desired_func = output
        if output := ball_shape_settings_button.update(events, globs, locs): desired_func = output
        if desired_func:
            if func_name != desired_func:
                return desired_func
            else:
                desired_func = None
        pg.display.update()


def run_general_settings(func_name='run_general_settings'):
    desired_func = None
    settings_bg = Image('arkanoid/resources/graphics/backgrounds/settings_menu.jpg', (constants.WIN_RECT.right, constants.WIN_RECT.bottom), topleft=(0, 0))
    back_general_settings_button = Button(Label('<', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', 'gray49', topleft=(10 * constants.X_COEFFICIENT, 10 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_ESCAPE, feedback='desired_func = "run_main_settings"\noutput = desired_func')
    general_settings_label = Label('GENERAL SETTINGS', 100 * constants.FONT_COEFFICIENT, 'endless', 'yellow', center=(constants.WIN_RECT.right / 2, 75 * constants.Y_COEFFICIENT))
    control_type_label = Label('CONTROL TYPE', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.width / 2, 175 * constants.Y_COEFFICIENT))
    keyboard_icon_button = Button(Image('arkanoid/resources/graphics/settings/keyboard.png', (300 * constants.X_COEFFICIENT, 150 * constants.Y_COEFFICIENT), topleft=(370 * constants.X_COEFFICIENT, 225 * constants.Y_COEFFICIENT)), 'glow', feedback='constants.CONTROL_TYPE = "keyboard"\nprogress.update_value("preferences", "control_type", constants.CONTROL_TYPE)')
    mouse_icon_button = Button(Image('arkanoid/resources/graphics/settings/mouse.png', (100 * constants.X_COEFFICIENT, 150 * constants.Y_COEFFICIENT), topleft=(870 * constants.X_COEFFICIENT, 225 * constants.Y_COEFFICIENT)), 'glow', feedback='constants.CONTROL_TYPE = "mouse"\nprogress.update_value("preferences", "control_type", constants.CONTROL_TYPE)')
    select_circle = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/settings/selection_circle.png'), (50 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT)).convert_alpha()
    select_dot = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/settings/selection_dot.png'), (50 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT)).convert_alpha()
    shape_animation_label = Label('BALL SHAPE ANIMATION', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.width / 2, 525 * constants.Y_COEFFICIENT))
    switch_on_button = Button(Image('arkanoid/resources/graphics/settings/switch_on.png', (250 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(595 * constants.X_COEFFICIENT, 575 * constants.Y_COEFFICIENT)), 'glow', feedback='constants.SHAPE_ANIMATION = False\nprogress.update_value("preferences", "ball_shape_animation", constants.SHAPE_ANIMATION)')
    switch_off_button = Button(Image('arkanoid/resources/graphics/settings/switch_off.png', (250 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(595 * constants.X_COEFFICIENT, 575 * constants.Y_COEFFICIENT)), 'glow', feedback='constants.SHAPE_ANIMATION = True\nprogress.update_value("preferences", "ball_shape_animation", constants.SHAPE_ANIMATION)')
    while True:
        constants.CLOCK.tick(constants.FPS)
        events = pg.event.get()
        globs = globals()
        locs = locals()
        for event in events:
            if event.type == pg.QUIT:
                pg.mixer.fadeout(850)
                desired_func = 'quit'
        settings_bg.show()
        general_settings_label.show()
        control_type_label.show()
        constants.WIN.blit(select_circle, (495 * constants.X_COEFFICIENT, 405 * constants.Y_COEFFICIENT))
        constants.WIN.blit(select_circle, (895 * constants.X_COEFFICIENT, 405 * constants.Y_COEFFICIENT))
        if constants.CONTROL_TYPE == 'keyboard':
            constants.WIN.blit(select_dot, (495 * constants.X_COEFFICIENT, 405 * constants.Y_COEFFICIENT))
        elif constants.CONTROL_TYPE == 'mouse':
            constants.WIN.blit(select_dot, (895 * constants.X_COEFFICIENT, 405 * constants.Y_COEFFICIENT))
        shape_animation_label.show()
        if output := back_general_settings_button.update(events, globs, locs): desired_func = output
        keyboard_icon_button.update(events, globs, locs)
        mouse_icon_button.update(events, globs, locs)
        if constants.SHAPE_ANIMATION:
            switch_on_button.update(events, globs, locs)
        elif not constants.SHAPE_ANIMATION:
            switch_off_button.update(events, globs, locs)
        if desired_func:
            if func_name != desired_func:
                return desired_func
            else:
                desired_func = None
        pg.display.update()


def run_volume_settings(func_name='run_volume_settings'):
    desired_func = None
    settings_bg = Image('arkanoid/resources/graphics/backgrounds/settings_menu.jpg', (constants.WIN_RECT.right, constants.WIN_RECT.bottom), topleft=(0, 0))
    back_volume_settings_button = Button(Label('<', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', 'gray49', topleft=(10 * constants.X_COEFFICIENT, 10 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_ESCAPE, feedback='for music in constants.MUSICS:\n music.update()\nfor sound in constants.SOUNDS:\n sound.update()\ndesired_func = "run_main_settings"\noutput = desired_func')
    volume_settings_label = Label('VOLUME SETTINGS', 100 * constants.FONT_COEFFICIENT, 'endless', 'yellow', center=(constants.WIN_RECT.right / 2, 75 * constants.Y_COEFFICIENT))
    general_volume_label = Label('GENERAL VOLUME', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.right / 2, 175 * constants.Y_COEFFICIENT))
    music_volume_label = Label('MUSIC VOLUME', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.right / 2, 400 * constants.Y_COEFFICIENT))
    sound_volume_label = Label('SOUND VOLUME', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.right / 2, 625 * constants.Y_COEFFICIENT))
    volume_bar = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/settings/volume_bar.png'), (680 * constants.X_COEFFICIENT, 110 * constants.Y_COEFFICIENT)).convert_alpha()
    minus_general_volume_button = Button(Image('arkanoid/resources/graphics/settings/minus_volume.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(260 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)), 'glow', feedback='if constants.VOLUME > 0:\n constants.PREVOLUME = constants.VOLUME = round(constants.VOLUME - 0.1, 1)\n progress.update_value("volume", "general", constants.VOLUME)')
    plus_general_volume_button = Button(Image('arkanoid/resources/graphics/settings/plus_volume.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(1080 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)), 'glow', feedback='if constants.VOLUME < 1:\n constants.PREVOLUME = constants.VOLUME = round(constants.VOLUME + 0.1, 1)\n progress.update_value("volume", "general", constants.VOLUME)')
    minus_music_volume_button = Button(Image('arkanoid/resources/graphics/settings/minus_volume.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(260 * constants.X_COEFFICIENT, 425 * constants.Y_COEFFICIENT)), 'glow', feedback='if constants.MUSIC_VOLUME > 0:\n constants.MUSIC_VOLUME = round(constants.MUSIC_VOLUME - 0.1, 1)\n progress.update_value("volume", "music", constants.MUSIC_VOLUME)')
    plus_music_volume_button = Button(Image('arkanoid/resources/graphics/settings/plus_volume.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(1080 * constants.X_COEFFICIENT, 425 * constants.Y_COEFFICIENT)), 'glow', feedback='if constants.MUSIC_VOLUME < 1:\n constants.MUSIC_VOLUME = round(constants.MUSIC_VOLUME + 0.1, 1)\n progress.update_value("volume", "music", constants.MUSIC_VOLUME)')
    minus_sound_volume_button = Button(Image('arkanoid/resources/graphics/settings/minus_volume.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(260 * constants.X_COEFFICIENT, 650 * constants.Y_COEFFICIENT)), 'glow', feedback='if constants.SOUND_VOLUME > 0:\n constants.SOUND_VOLUME = round(constants.SOUND_VOLUME - 0.1, 1)\n progress.update_value("volume", "sound", constants.SOUND_VOLUME)')
    plus_sound_volume_button = Button(Image('arkanoid/resources/graphics/settings/plus_volume.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(1080 * constants.X_COEFFICIENT, 650 * constants.Y_COEFFICIENT)), 'glow', feedback='if constants.SOUND_VOLUME < 1:\n constants.SOUND_VOLUME = round(constants.SOUND_VOLUME + 0.1, 1)\n progress.update_value("volume", "sound", constants.SOUND_VOLUME)')
    while True:
        constants.CLOCK.tick(constants.FPS)
        events = pg.event.get()
        globs = globals()
        locs = locals()
        for event in events:
            if event.type == pg.QUIT:
                pg.mixer.fadeout(850)
                desired_func = 'quit'
        general_volume_square_x = 410
        music_volume_square_x = 410
        sound_volume_square_x = 410
        settings_bg.show()
        volume_settings_label.show()
        general_volume_label.show()
        music_volume_label.show()
        sound_volume_label.show()
        constants.WIN.blit(volume_bar, (380 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT))
        constants.WIN.blit(volume_bar, (380 * constants.X_COEFFICIENT, 425 * constants.Y_COEFFICIENT))
        constants.WIN.blit(volume_bar, (380 * constants.X_COEFFICIENT, 650 * constants.Y_COEFFICIENT))
        for i in range(int(constants.VOLUME * 10)):
            pg.draw.rect(constants.WIN, 'red', pg.Rect(general_volume_square_x * constants.X_COEFFICIENT, 230 * constants.Y_COEFFICIENT, 50 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT))
            general_volume_square_x += 63
        for i in range(int(constants.MUSIC_VOLUME * 10)):
            pg.draw.rect(constants.WIN, 'red', pg.Rect(music_volume_square_x * constants.X_COEFFICIENT, 455 * constants.Y_COEFFICIENT, 50 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT))
            music_volume_square_x += 63
        for i in range(int(constants.SOUND_VOLUME * 10)):
            pg.draw.rect(constants.WIN, 'red', pg.Rect(sound_volume_square_x * constants.X_COEFFICIENT, 680 * constants.Y_COEFFICIENT, 50 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT))
            sound_volume_square_x += 63
        if output := back_volume_settings_button.update(events, globs, locs): desired_func = output
        minus_general_volume_button.update(events, globs, locs)
        plus_general_volume_button.update(events, globs, locs)
        minus_music_volume_button.update(events, globs, locs)
        plus_music_volume_button.update(events, globs, locs)
        minus_sound_volume_button.update(events, globs, locs)
        plus_sound_volume_button.update(events, globs, locs)
        if desired_func:
            if func_name != desired_func:
                return desired_func
            else:
                desired_func = None
        pg.display.update()
        constants.SETTINGS_MUSIC.update()
        constants.CLICK_SOUND1.update()


def run_ball_shape_settings(func_name='run_ball_shape_settings'):
    desired_func = None
    position = constants.BALL_SHAPES.index(constants.CURRENT_SHAPE)
    shape = Shape((620 * constants.X_COEFFICIENT, 150 * constants.Y_COEFFICIENT), (200 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT), constants.AVAILABLE_SHAPES.split(',')[position])
    shape_name_label = Label(shape.name, 75 * constants.FONT_COEFFICIENT, 'endless', 'green', center=(constants.WIN_RECT.right / 2, 400 * constants.Y_COEFFICIENT))
    description_label = Label('Description:', 50 * constants.FONT_COEFFICIENT, 'tales', 'orange', topleft=(50 * constants.X_COEFFICIENT, 450 * constants.Y_COEFFICIENT))
    shape_description_label = Label(shape.description, 50 * constants.FONT_COEFFICIENT, 'tales', 'orange', topleft=(50 * constants.X_COEFFICIENT, 520 * constants.Y_COEFFICIENT))

    settings_bg = Image('arkanoid/resources/graphics/backgrounds/settings_menu.jpg', (constants.WIN_RECT.right, constants.WIN_RECT.bottom), topleft=(0, 0))
    back_ball_shape_settings_button = Button(Label('<', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', 'gray49', topleft=(10 * constants.X_COEFFICIENT, 10 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_ESCAPE, feedback='desired_func = "run_main_settings"\noutput = desired_func')
    ball_shape_settings_label = Label('BALL SHAPE', 100 * constants.FONT_COEFFICIENT, 'endless', 'yellow', center=(constants.WIN_RECT.right / 2, 75 * constants.Y_COEFFICIENT))
    previous_shape_button = Button(Label('<', 200 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', topleft=(496 * constants.X_COEFFICIENT, 193 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_LEFT, feedback='position -= 1\nshape = Shape((620 * constants.X_COEFFICIENT, 150 * constants.Y_COEFFICIENT), (200 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT), constants.AVAILABLE_SHAPES.split(",")[position])\nshape_name_label = Label(shape.name, 75 * constants.FONT_COEFFICIENT, "endless", "green", center=(constants.WIN_RECT.right / 2, 400 * constants.Y_COEFFICIENT))\nshape_description_label = Label(shape.description, 50 * constants.FONT_COEFFICIENT, "tales", "orange", topleft=(50 * constants.X_COEFFICIENT, 520 * constants.Y_COEFFICIENT))\noutput = position, shape, shape_name_label, shape_description_label')
    next_shape_button = Button(Label('>', 200 * constants.FONT_COEFFICIENT, 'pixeboy', 'red', topleft=(850 * constants.X_COEFFICIENT, 193 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_RIGHT, feedback='position += 1\nshape = Shape((620 * constants.X_COEFFICIENT, 150 * constants.Y_COEFFICIENT), (200 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT), constants.AVAILABLE_SHAPES.split(",")[position])\nshape_name_label = Label(shape.name, 75 * constants.FONT_COEFFICIENT, "endless", "green", center=(constants.WIN_RECT.right / 2, 400 * constants.Y_COEFFICIENT))\nshape_description_label = Label(shape.description, 50 * constants.FONT_COEFFICIENT, "tales", "orange", topleft=(50 * constants.X_COEFFICIENT, 520 * constants.Y_COEFFICIENT))\noutput = position, shape, shape_name_label, shape_description_label')
    confirm_shape_button = Button(Label('CONFIRM', 100 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', 'red', topleft=(485.5 * constants.X_COEFFICIENT, 650 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_SPACE, click_sound=2, feedback='progress.update_value("ball_shapes", "current", shape.surf_name)\nconstants.CURRENT_SHAPE = progress.get_value("ball_shapes", "current")\ndesired_func = "run_main_settings"\noutput = desired_func')
    while True:
        constants.CLOCK.tick(constants.FPS)
        events = pg.event.get()
        globs = globals()
        locs = locals()
        for event in events:
            if event.type == pg.QUIT:
                pg.mixer.fadeout(850)
                desired_func = 'quit'
        settings_bg.show()
        ball_shape_settings_label.show()
        description_label.show()
        shape_name_label.show()
        shape_description_label.show()
        shape.update()
        constants.WIN.blit(shape.image, shape.rect)
        if output := back_ball_shape_settings_button.update(events, globs, locs): desired_func = output
        if position > 0:
            if output := previous_shape_button.update(events, globs, locs): position, shape, shape_name_label, shape_description_label = output
        if position < len(constants.AVAILABLE_SHAPES.split(',')) - 1:
            if output := next_shape_button.update(events, globs, locs): position, shape, shape_name_label, shape_description_label = output
        if output := confirm_shape_button.update(events, globs, locs): desired_func = output
        if desired_func:
            if func_name != desired_func:
                return desired_func
            else:
                desired_func = None
        pg.display.update()
