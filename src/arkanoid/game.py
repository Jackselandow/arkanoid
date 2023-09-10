import pygame
import pygame as pg
from arkanoid import constants
from arkanoid.classes import Label, Image, Button, Border, Brick, Platform, Ball
from arkanoid.progress import update_game_progress
pg.init()


class Level:

    def __init__(self, number: str):
        self.number = number
        self.started = False
        self.press_space_label = Label('Press SPACE to start', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'red', center=(constants.WIN_RECT.right / 2, constants.WIN_RECT.height / 2))
        self.label_opacity_timer = 0
        self.upper_menu = pg.Rect(0, 0, constants.WIN_RECT.width, 116 * constants.Y_COEFFICIENT)
        self.pause_button = Button(Image('arkanoid/resources/graphics/game/pause_button.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(8 * constants.X_COEFFICIENT, 8 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_ESCAPE, feedback='last_frame = constants.WIN.copy()\ndesired_func = self.run_pause(last_frame)\noutput = desired_func')
        self.bg = Image(f'arkanoid/resources/graphics/backgrounds/lvl{self.number}.png', (constants.WIN_RECT.right, constants.WIN_RECT.bottom - self.upper_menu.height), topleft=(0, self.upper_menu.bottom))
        self.music = eval(f'constants.LVL{self.number}_MUSIC')
        self.left_border = Border((-1, 115 * constants.Y_COEFFICIENT), (1, constants.WIN_RECT.height))
        self.right_border = Border((constants.WIN_RECT.right, 115 * constants.Y_COEFFICIENT), (1, constants.WIN_RECT.height))
        self.top_border = Border((0, 115 * constants.Y_COEFFICIENT), (constants.WIN_RECT.width, 1))
        self.bottom_border = Border(constants.WIN_RECT.bottomleft, (constants.WIN_RECT.width, 1))
        self.borders_group = pg.sprite.Group(self.left_border, self.right_border, self.top_border, self.bottom_border)
        self.platform = Platform(self, (620 * constants.X_COEFFICIENT, 720 * constants.Y_COEFFICIENT), [200 * constants.X_COEFFICIENT, 30 * constants.Y_COEFFICIENT], 8)
        self.platform_group = pg.sprite.GroupSingle(self.platform)
        self.balls_group = pg.sprite.Group(Ball(self, (695 * constants.X_COEFFICIENT, 670 * constants.Y_COEFFICIENT), (50 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT), constants.CURRENT_SHAPE, 8))
        self.bricks_group = pg.sprite.Group()
        self.gray_bricks_number = 0
        self.passive_buffs_group = pg.sprite.Group()
        self.active_buffs_group = pg.sprite.Group()
        self.active_buffs_types = []
        self.create_bricks()
    
    def create_bricks(self):
        if self.number == '1':
            brick_x, brick_y = 8 * constants.X_COEFFICIENT, 124 * constants.Y_COEFFICIENT
            brick_size = (135.2 * constants.X_COEFFICIENT, 40 * constants.Y_COEFFICIENT)
            delta_brick_x, delta_brick_y = 143.2 * constants.X_COEFFICIENT, 48 * constants.Y_COEFFICIENT
            for i in range(56):
                brick_color = 'none'
                if i % 10 == 0 and i != 0:
                    brick_x, brick_y = 8 * constants.X_COEFFICIENT, brick_y + delta_brick_y
                if i in [0, 9, 10, 19]:
                    brick_color = 'green'
                if i in [1, 2, 7, 8, 11, 12, 17, 18, 21, 22, 27, 28, 31, 32, 37, 38]:
                    brick_color = 'purple'
                if i in [3, 4, 5, 6, 13, 16]:
                    brick_color = 'yellow'
                if i in [23, 26, 33, 34, 35, 36, 44, 45, 54, 55]:
                    brick_color = 'red'
                if brick_color != 'none':
                    self.bricks_group.add(Brick(self, (brick_x, brick_y), brick_size, brick_color))
                brick_x += delta_brick_x
        elif self.number == '2':
            brick_x, brick_y = 8 * constants.X_COEFFICIENT, 124 * constants.Y_COEFFICIENT
            brick_size = (81.5 * constants.X_COEFFICIENT, 65 * constants.Y_COEFFICIENT)
            delta_brick_x, delta_brick_y = 89.5 * constants.X_COEFFICIENT, 73 * constants.Y_COEFFICIENT
            for i in range(80):
                brick_color = 'none'
                if i % 16 == 0 and i != 0:
                    brick_x, brick_y = 8 * constants.X_COEFFICIENT, brick_y + delta_brick_y
                if i in [4, 11, 17, 21, 26, 30, 34, 38, 41, 45, 51, 60]:
                    brick_color = 'yellow'
                if i in [5, 6, 7, 8, 9, 10, 16, 22, 23, 24, 25, 31, 32, 33, 39, 40, 46, 47, 48, 49, 50, 61, 62, 63]:
                    brick_color = 'orange'
                if i in [55, 56]:
                    brick_color = 'red'
                if i in [0, 15]:
                    brick_color = 'blue'
                if i in [64, 65, 66, 67, 68, 75, 76, 77, 78, 79]:
                    brick_color = 'gray'
                    self.gray_bricks_number += 1
                if brick_color != 'none':
                    self.bricks_group.add(Brick(self, (brick_x, brick_y), brick_size, brick_color))
                brick_x += delta_brick_x
        elif self.number == '3':
            brick_x, brick_y = 8 * constants.X_COEFFICIENT, 124 * constants.Y_COEFFICIENT
            brick_size = (150 * constants.X_COEFFICIENT, 29.5 * constants.Y_COEFFICIENT)
            delta_brick_x, delta_brick_y = 159 * constants.X_COEFFICIENT, 37.5 * constants.Y_COEFFICIENT
            for i in range(81):
                brick_color = 'none'
                if i % 9 == 0 and i != 0:
                    brick_x, brick_y = 8 * constants.X_COEFFICIENT, brick_y + delta_brick_y
                if i in [22, 38, 42, 58]:
                    brick_color = 'green'
                if i in [18, 26, 54, 62]:
                    brick_color = 'purple'
                if i in [12, 14, 28, 34, 46, 52, 66, 68]:
                    brick_color = 'yellow'
                if i in [10, 16, 20, 24, 56, 60, 64, 70]:
                    brick_color = 'red'
                if i in [30, 32, 48, 50]:
                    brick_color = 'blue'
                if i in [0, 2, 4, 6, 8, 36, 40, 44, 72, 74, 76, 78, 80]:
                    brick_color = 'gray'
                    self.gray_bricks_number += 1
                if brick_color != 'none':
                    self.bricks_group.add(Brick(self, (brick_x, brick_y), brick_size, brick_color))
                brick_x += delta_brick_x
        elif self.number == '4':
            brick_x, brick_y = 8 * constants.X_COEFFICIENT, 124 * constants.Y_COEFFICIENT
            brick_size = (81.5 * constants.X_COEFFICIENT, 65 * constants.Y_COEFFICIENT)
            delta_brick_x, delta_brick_y = 89.5 * constants.X_COEFFICIENT, 73 * constants.Y_COEFFICIENT
            for i in range(80):
                brick_color = 'none'
                if i % 16 == 0 and i != 0:
                    brick_x, brick_y = 8 * constants.X_COEFFICIENT, brick_y + delta_brick_y
                if i in [4, 11, 17, 21, 26, 30, 34, 38, 41, 45, 51, 60]:
                    brick_color = 'yellow'
                if i in [5, 6, 7, 8, 9, 10, 16, 22, 23, 24, 25, 31, 32, 33, 39, 40, 46, 47, 48, 49, 50, 61, 62, 63]:
                    brick_color = 'orange'
                if i in [55, 56]:
                    brick_color = 'red'
                if i in [0, 15]:
                    brick_color = 'blue'
                if i in [64, 65, 66, 67, 68, 75, 76, 77, 78, 79]:
                    brick_color = 'gray'
                    self.gray_bricks_number += 1
                if brick_color != 'none':
                    self.bricks_group.add(Brick(self, (brick_x, brick_y), brick_size, brick_color, armor=3))
                brick_x += delta_brick_x

    def play(self, func_name='play'):
        desired_func = None
        lvl_name_label = Label(f'l e v e l {self.number}', 100 * constants.FONT_COEFFICIENT, 'retroblaze', 'green', center=(constants.WIN_RECT.right / 2, self.upper_menu.bottom / 2))
        while True:
            bricks_left_number = len(self.bricks_group) - self.gray_bricks_number
            bricks_left_label = Label('BRICKS LEFT: ' + str(bricks_left_number), 60 * constants.FONT_COEFFICIENT, 'pixeboy', 'white', bottomright=(constants.WIN_RECT.right - 8 * constants.X_COEFFICIENT, self.upper_menu.bottom - 8 * constants.Y_COEFFICIENT))
            constants.CLOCK.tick(constants.FPS)
            events = pg.event.get()
            globs = globals()
            locs = locals()
            for event in events:
                if event.type == pg.QUIT:
                    pg.mixer.fadeout(850)
                    desired_func = constants.WIN.copy()
                elif event.type == pg.KEYUP and event.key == pygame.K_SPACE and self.started is False:
                    self.started = True
                    self.music.play(-1)
            if bricks_left_number == 0:
                self.music.stop()
                desired_func = self.run_victory()
            elif len(self.balls_group) == 0:
                self.music.stop()
                desired_func = self.run_defeat()

            self.bg.show()
            constants.WIN.fill('black', self.upper_menu)
            lvl_name_label.show()
            bricks_left_label.show()
            self.bricks_group.draw(constants.WIN)
            if int(self.number) >= 3:
                self.update_buffs()
            self.platform_group.update()
            if self.started is True:
                self.balls_group.update()
            elif self.started is False:
                label_alpha = self.press_space_label.text.get_alpha()
                if self.label_opacity_timer == 0:
                    if label_alpha == 0:
                        self.press_space_label.text.set_alpha(255)
                    elif label_alpha == 255 or not label_alpha:
                        self.press_space_label.text.set_alpha(0)
                    self.label_opacity_timer = 30
                else:
                    self.label_opacity_timer -= 1
                self.press_space_label.show()
                for ball in self.balls_group:
                    ball.hitbox.centerx = self.platform.rect.centerx
                    ball.rect.centerx = self.platform.rect.centerx
            self.platform_group.draw(constants.WIN)
            self.balls_group.draw(constants.WIN)
            if output := self.pause_button.update(events, globs, locs): desired_func = output
            if desired_func:
                if func_name != desired_func:
                    return desired_func
                else:
                    desired_func = None
                    continue
            pg.display.update()

    def update_buffs(self):
        self.passive_buffs_group.update()
        if self.platform.width_scaler: # checks if the platform has fulfilled the 'narrow_platform' and 'wide_platform' buffs' effect
            if abs(self.platform.size[0] - self.platform.desired_size[0]) < 1 * constants.X_COEFFICIENT:
                self.platform.size[0] = self.platform.desired_size[0]
                self.platform.width_scaler = None
            else:
                self.platform.size[0] += self.platform.width_scaler
            self.platform.update_appearance()
        if 'x-ray' in self.active_buffs_types:
            self.passive_buffs_group.draw(constants.WIN)
        if 'ghost_ball' in self.active_buffs_types:
            for ball in self.balls_group:
                if ball.alpha == -100:
                    ball.visibility_state = 'appear'
                elif ball.alpha == 255:
                    ball.visibility_state = 'disappear'
                if ball.visibility_state == 'appear':
                    ball.alpha += 5
                    ball.image.set_alpha(ball.alpha)
                elif ball.visibility_state == 'disappear':
                    ball.alpha -= 5
                    ball.image.set_alpha(ball.alpha)

    def run_pause(self, last_frame, func_name='run_pause'):
        desired_func = None
        pg.mixer.pause()
        constants.PAUSE_IN_SOUND.play()
        transparent_bg = constants.BLACK_SCREEN
        transparent_bg.set_alpha(120)
        constants.WIN.blit(transparent_bg, (0, 0))

        pause_bg = Image('arkanoid/resources/graphics/backgrounds/pause.png', (810 * constants.X_COEFFICIENT, 562.5 * constants.Y_COEFFICIENT), center=(constants.WIN_RECT.right / 2, constants.WIN_RECT.bottom / 2))
        pause_label = Label('GAME PAUSED', 100 * constants.FONT_COEFFICIENT, 'pixeboy', 'white', center=(constants.WIN_RECT.right / 2, 330 * constants.Y_COEFFICIENT))
        restart_button = Button(Image('arkanoid/resources/graphics/game/pause/restart_button.png', (162 * constants.X_COEFFICIENT, 180 * constants.Y_COEFFICIENT), topleft=(440 * constants.X_COEFFICIENT, 420 * constants.Y_COEFFICIENT)), 'glow', feedback='pg.mixer.stop()\ndesired_func = Level(self.number).play()\noutput = desired_func')
        main_menu_button = Button(Image('arkanoid/resources/graphics/game/pause/main_menu_button.png', (162 * constants.X_COEFFICIENT, 180 * constants.Y_COEFFICIENT), topleft=(639 * constants.X_COEFFICIENT, 420 * constants.Y_COEFFICIENT)), 'glow',  key=pg.K_ESCAPE, feedback='pg.mixer.stop()\nfor buff in self.active_buffs_group:\n if buff.timer:\n  buff.timer.cancel()\ndesired_func = "run_main_menu"\noutput = desired_func')
        full_volume_button = Button(Image('arkanoid/resources/graphics/game/pause/full_volume_button.png', (162 * constants.X_COEFFICIENT, 180 * constants.Y_COEFFICIENT), topleft=(838 * constants.X_COEFFICIENT, 420 * constants.Y_COEFFICIENT)), 'glow', feedback='constants.PREVOLUME = constants.VOLUME\nconstants.VOLUME = 0\nfor music in constants.MUSICS:\n music.update()\nfor sound in constants.SOUNDS:\n sound.update()')
        no_volume_button = Button(Image('arkanoid/resources/graphics/game/pause/no_volume_button.png', (162 * constants.X_COEFFICIENT, 180 * constants.Y_COEFFICIENT), topleft=(838 * constants.X_COEFFICIENT, 420 * constants.Y_COEFFICIENT)), 'glow', feedback='constants.VOLUME = constants.PREVOLUME\nfor music in constants.MUSICS:\n music.update()\nfor sound in constants.SOUNDS:\n sound.update()')
        resume_button = Button(Label('RESUME', 130 * constants.FONT_COEFFICIENT, 'pixeboy', 'green', center=(constants.WIN_RECT.right / 2, 670 * constants.Y_COEFFICIENT)), 'glow', key=pg.K_SPACE, silent=True, feedback='if self.started is True:\n self.run_countdown(last_frame)\nelse:\n constants.PAUSE_OUT_SOUND.play()\npg.mixer.unpause()\ndesired_func = "play"\noutput = desired_func')
        while True:
            constants.CLOCK.tick(constants.FPS)
            events = pg.event.get()
            globs = globals()
            locs = locals()
            for event in events:
                if event.type == pg.QUIT:
                    pg.mixer.fadeout(850)
                    desired_func = constants.WIN.copy()
            pause_bg.show()
            pause_label.show()
            if output := restart_button.update(events, globs, locs): desired_func = output
            if output := main_menu_button.update(events, globs, locs): desired_func = output
            if constants.VOLUME == 0:
                no_volume_button.update(events, globs, locs)
            else:
                full_volume_button.update(events, globs, locs)
            if output := resume_button.update(events, globs, locs): desired_func = output
            if desired_func:
                if func_name != desired_func:
                    return desired_func
                else:
                    desired_func = None
                    continue
            pg.display.update()

    def run_countdown(self, last_frame):
        three = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/pause/three.png'), (160 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)).convert_alpha()
        two = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/pause/two.png'), (160 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)).convert_alpha()
        one = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/pause/one.png'), (76 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)).convert_alpha()
        go = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/pause/go.png'), (451 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)).convert_alpha()
        countdown_list = [three, two, one, go]

        for i in range(4):
            if i in range(0, 2):
                x = 640 * constants.X_COEFFICIENT
                constants.COUNTDOWN_SOUND.play()
            if i == 2:
                x = 682 * constants.X_COEFFICIENT
                constants.COUNTDOWN_SOUND.play()
            if i == 3:
                x = 494.5 * constants.X_COEFFICIENT
                constants.PAUSE_OUT_SOUND.play()
            constants.WIN.blit(last_frame, (0, 0))
            constants.WIN.blit(countdown_list[i], (x, 350 * constants.Y_COEFFICIENT))
            pg.display.update()
            pg.time.wait(600)

    def run_victory(self, func_name='run_victory'):
        desired_func = None
        for buff in self.active_buffs_group:
            if buff.timer:
                buff.timer.cancel()
        self.active_buffs_group.empty()
        if self.number not in constants.PASSED_LEVELS:
            update_game_progress(self.number)
            passed = True
        else:
            passed = False
        constants.VICTORY_SOUND.play()

        cup = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/cup.png'), (200 * constants.X_COEFFICIENT, 200 * constants.Y_COEFFICIENT)).convert()
        level_label = Label('LEVEL', 100 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.right / 2, 150 * constants.Y_COEFFICIENT))
        completed_label = Label('COMPLETED', 100 * constants.FONT_COEFFICIENT, 'pixeloid', 'white', center=(constants.WIN_RECT.right / 2, 270 * constants.Y_COEFFICIENT))
        next_level_button = Button(Label('NEXT LEVEL', 75 * constants.FONT_COEFFICIENT, 'pixeloid', 'green', topleft=(470 * constants.X_COEFFICIENT, 450 * constants.Y_COEFFICIENT)), 'green_arrows', key=pg.K_SPACE, click_sound='start', feedback='constants.VICTORY_SOUND.stop()\ndesired_func = Level(str(int(self.number) + 1)).play()\noutput = desired_func')
        menu_button = Button(Label('MAIN MENU', 75 * constants.FONT_COEFFICIENT, 'pixeloid', 'gray', topleft=(495 * constants.X_COEFFICIENT, 570 * constants.Y_COEFFICIENT)), 'gray_arrows', key=pg.K_ESCAPE, feedback='constants.VICTORY_SOUND.stop()\ndesired_func = "run_main_menu"\noutput = desired_func')
        shape_unlocked_label = Label('NEW BALL SHAPE UNLOCKED!', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'red', bottomleft=(constants.WIN_RECT.width, constants.WIN_RECT.bottom))
        while True:
            constants.CLOCK.tick(constants.FPS)
            events = pg.event.get()
            globs = globals()
            locs = locals()
            for event in events:
                if event.type == pg.QUIT:
                    pg.mixer.fadeout(850)
                    desired_func = constants.WIN.copy()
            constants.WIN.fill('black')
            constants.WIN.blit(cup, (220 * constants.X_COEFFICIENT, 110 * constants.Y_COEFFICIENT))
            constants.WIN.blit(cup, (1010 * constants.X_COEFFICIENT, 110 * constants.Y_COEFFICIENT))
            level_label.show()
            completed_label.show()
            if int(self.number) != constants.MAX_LEVEL:
                if output := next_level_button.update(events, globs, locs): desired_func = output
            if output := menu_button.update(events, globs, locs): desired_func = output
            if passed is True:
                shape_unlocked_label.show()
                shape_unlocked_label.rect.x -= 5
            if desired_func:
                if func_name != desired_func:
                    return desired_func
                else:
                    desired_func = None
                    continue
            pg.display.update()

    def run_defeat(self, func_name='run_defeat'):
        desired_func = None
        for buff in self.active_buffs_group:
            if buff.timer:
                buff.timer.cancel()
        self.active_buffs_group.empty()
        constants.DEFEAT_SOUND.play()

        game_over = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/game_over.png'), (640 * constants.X_COEFFICIENT, 320 * constants.Y_COEFFICIENT)).convert()
        retry_button = Button(Label('RETRY', 75 * constants.FONT_COEFFICIENT, 'pixeloid', 'red', topleft=(595 * constants.X_COEFFICIENT, 450 * constants.Y_COEFFICIENT)), 'red_arrows', key=pg.K_SPACE, feedback='constants.DEFEAT_SOUND.stop()\ndesired_func = Level(self.number).play()\noutput = desired_func')
        menu_button = Button(Label('MAIN MENU', 75 * constants.FONT_COEFFICIENT, 'pixeloid', 'gray', topleft=(495 * constants.X_COEFFICIENT, 570 * constants.Y_COEFFICIENT)), 'gray_arrows', key=pg.K_ESCAPE, feedback='constants.DEFEAT_SOUND.stop()\ndesired_func = "run_main_menu"\noutput = desired_func')
        while True:
            constants.CLOCK.tick(constants.FPS)
            events = pg.event.get()
            globs = globals()
            locs = locals()
            for event in events:
                if event.type == pg.QUIT:
                    pg.mixer.fadeout(850)
                    desired_func = constants.WIN.copy()
            constants.WIN.fill('black')
            constants.WIN.blit(game_over, (400 * constants.X_COEFFICIENT, 50 * constants.Y_COEFFICIENT))
            if output := retry_button.update(events, globs, locs): desired_func = output
            if output := menu_button.update(events, globs, locs): desired_func = output
            if desired_func:
                if func_name != desired_func:
                    return desired_func
                else:
                    desired_func = None
                    continue
            pg.display.update()

