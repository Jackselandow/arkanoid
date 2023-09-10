from math import sqrt
from os import listdir
from random import choice, randint
from threading import Timer
import pygame as pg
from arkanoid import constants
pg.init()


class Music:

    def __init__(self, filename, volume):
        self.name = pg.mixer.Sound(filename)
        self.volume = volume
        self.update()

    def play(self, loops=0):
        self.name.play(loops)

    def stop(self):
        self.name.stop()

    def set_volume(self, value):
        self.volume = value

    def get_volume(self):
        volume = self.name.get_volume()
        return volume

    def get_busy(self):
        if self.name.get_num_channels() == 0:
            get_busy = False
        else:
            get_busy = True
        return get_busy

    def update(self):
        self.name.set_volume(constants.VOLUME * constants.MUSIC_VOLUME * self.volume)


class Sound:

    def __init__(self, filename, volume):
        self.name = pg.mixer.Sound(filename)
        self.volume = volume
        self.update()

    def play(self, loops=0):
        self.name.play(loops)

    def stop(self):
        self.name.stop()

    def stop_play(self):
        self.stop()
        self.play()

    def set_volume(self, value):
        self.volume = value

    def get_volume(self):
        volume = self.name.get_volume()
        return volume

    def get_current_length(self):
        length = self.name.get_length()
        return length

    def get_busy(self):
        if self.name.get_num_channels() == 0:
            get_busy = False
        else:
            get_busy = True
        return get_busy

    def update(self):
        self.name.set_volume(constants.VOLUME * constants.SOUND_VOLUME * self.volume)


class Label:

    def __init__(self, text, font_size, font_name, fg, bg=None, antialias=False, **pos):
        font_path = f'arkanoid/resources/fonts/{font_name}.ttf'
        self.font = pg.font.Font(font_path, int(font_size))
        self.text = self.font.render(text, antialias, fg)
        finished_fonts = ['pixeboy', 'connection', 'retroblaze']
        self.surf = pg.Surface(self.text.get_size()).convert()
        self.bg = bg
        if bg:
            self.surf.fill(bg)
        if font_name not in finished_fonts:
            self.surf.blit(self.text, (font_size / 20, 0))
        else:
            self.surf.blit(self.text, (0, 0))
        self.rect = self.text.get_rect(**pos)

    def show(self):
        if self.bg:
            constants.WIN.blit(self.surf, self.rect)
        else:
            constants.WIN.blit(self.text, self.rect)


class Image:

    def __init__(self, file_path, size, **pos):
        self.image = pg.transform.scale(pg.image.load(file_path), size).convert_alpha()
        self.rect = self.image.get_rect(**pos)

    def show(self):
        constants.WIN.blit(self.image, self.rect)


class Button:

    def __init__(self, content, selection_type, interactive=True, key=None, click_sound=1, silent=False, feedback=None):
        self.content = content
        if 'glow' in selection_type:
            self.selection_type = 'glow'
            white_glow = pg.Surface((self.content.rect.size[0] + 16 * constants.X_COEFFICIENT, self.content.rect.size[1] + 16 * constants.Y_COEFFICIENT)).convert()
            white_glow.fill('white')
            white_glow.set_alpha(120)
            self.selection_surfs = {white_glow: white_glow.get_rect(center=self.content.rect.center)}
            red_glow = white_glow.copy()
            red_glow.fill('red')
            self.press_surfs = {red_glow: red_glow.get_rect(center=self.content.rect.center)}
        elif 'arrows' in selection_type:
            self.selection_type = 'arrows'
            arrows_color = selection_type.split('_')[0]
            left_arrow = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/selection_arrows/{arrows_color}_left.png'), (self.content.rect.size[1] / 3.6, self.content.rect.size[1] / 2)).convert_alpha()
            right_arrow = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/selection_arrows/{arrows_color}_right.png'), (self.content.rect.size[1] / 3.6, self.content.rect.size[1] / 2)).convert_alpha()
            left_press_arrow = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/selection_arrows/{arrows_color}_left_press.png'), left_arrow.get_size()).convert_alpha()
            right_press_arrow = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/selection_arrows/{arrows_color}_right_press.png'), right_arrow.get_size()).convert_alpha()
            self.selection_surfs = {left_arrow: (self.content.rect.left - 1.3 * left_arrow.get_width(), self.content.rect.centery - left_arrow.get_height() / 2), right_arrow: (self.content.rect.right + 0.3 * right_arrow.get_width(), self.content.rect.centery - right_arrow.get_height() / 2)}
            self.press_surfs = {left_press_arrow: (self.content.rect.left - 1.3 * left_press_arrow.get_width(), self.content.rect.centery - left_press_arrow.get_height() / 2), right_press_arrow: (self.content.rect.right + 0.3 * right_press_arrow.get_width(), self.content.rect.centery - right_press_arrow.get_height() / 2)}
        self.interactive = interactive
        self.key = key
        self.silent = silent
        if click_sound == 1:
            self.click_sound = constants.CLICK_SOUND1
        elif click_sound == 2:
            self.click_sound = constants.CLICK_SOUND2
        elif click_sound == 'start':
            self.click_sound = constants.START_SOUND
        self.sound_cooldown = True
        self.selection_detected = False
        self.press_detected = [False, False] # first element - mouse, second - keyboard
        self.release_detected = [False, False]
        self.feedback = feedback

    def check_selection(self):
        mouse_pos = pg.mouse.get_pos()
        if self.content.rect.collidepoint(mouse_pos):
            self.selection_detected = True
        else:
            self.selection_detected = False

    def check_press(self, events):
        if self.selection_detected is True:
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.press_detected[0] = True
        else:
            self.press_detected[0] = False
        if self.key:
            for event in events:
                if event.type == pg.KEYDOWN and event.key == self.key:
                    self.press_detected[1] = True

    def check_release(self, events):
        if self.press_detected[0] is True:
            for event in events:
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    self.release_detected[0] = True
        if self.press_detected[1] is True:
            for event in events:
                if event.type == pg.KEYUP and event.key == self.key:
                    self.release_detected[1] = True

    def give_feedback(self, globs, locs):
        output = None
        exec(self.feedback, globs, locs)
        output = locs['output']
        return output

    def update(self, events, globs, locs):
        if self.interactive is True:
            self.check_selection()
            self.check_press(events)
            self.check_release(events)
            if sum(self.release_detected) > 0:
                self.selection_detected = False
                self.press_detected = [False, False]
                self.release_detected = [False, False]
                self.click_sound.play()
                self.show()
                return self.give_feedback(globs, locs)
            elif sum(self.press_detected) > 0:
                for surf, pos in self.press_surfs.items():
                    constants.WIN.blit(surf, pos)
            elif self.selection_detected is True:
                if self.selection_type == 'arrows' and self.silent is False and self.sound_cooldown is False:
                    self.sound_cooldown = True
                    constants.SELECTION_SOUND.play()
                for surf, pos in self.selection_surfs.items():
                    constants.WIN.blit(surf, pos)
            elif self.sound_cooldown is True:
                self.sound_cooldown = False
        self.show()

    def show(self):
        self.content.show()


# class LevelControl:
#
#     def __init__(self, bg, music, platform):
#         self.started = False
#         self.countdown_state = False
#         self.countdown_index = 0
#         self.press_space_label = Button(Label('Press SPACE to start', 50 * constants.FONT_COEFFICIENT, 'pixeloid', 'red', center=(constants.WIN_RECT.right / 2, constants.WIN_RECT.height / 2)), None, clickable=False, key=pg.K_SPACE)
#         self.press_space_label.content.text.set_alpha(0)
#         self.press_space_state = 'appear'
#         self.bg = bg
#         self.music = music
#         self.borders_group = pg.sprite.Group(constants.TOP_BORDER, constants.LEFT_BORDER, constants.RIGHT_BORDER, constants.BOTTOM_BORDER)
#         self.upper_menu = pg.Rect(0, 0, constants.WIN_RECT.width, 116 * constants.Y_COEFFICIENT)
#         self.pause_button = Button(None, Image('resources/graphics/game/pause_button.png', (100 * constants.X_COEFFICIENT, 100 * constants.Y_COEFFICIENT), topleft=(8 * constants.X_COEFFICIENT, 8 * constants.Y_COEFFICIENT)), key=pg.K_ESCAPE, feedbacks=[run_pause])
#         self.platform_group = pg.sprite.GroupSingle(platform)
#         self.balls_group = pg.sprite.Group()
#         self.bricks_group = pg.sprite.Group()
#         self.passive_buffs_group = pg.sprite.Group()
#         self.active_buffs_group = pg.sprite.Group()
#         self.active_buffs_types = []
#
#     def detect_start(self):
#         if self.started is False and self.press_space_label.all_in_one() is True:
#             # press_space_label.content.text.set_alpha(constants.LEVEL.press_space_alpha)
#             self.started = True
#             self.music.play(loops=-1)
#         if self.started is True:
#             self.balls_group.update()
#         else:
#             label_alpha = self.press_space_label.content.text.get_alpha()
#             if label_alpha is None:
#                 label_alpha = 255
#             if label_alpha >= 255:
#                 self.press_space_state = 'disappear'
#             elif label_alpha <= 0:
#                 self.press_space_state = 'appear'
#             if self.press_space_state == 'appear':
#                 self.press_space_label.content.text.set_alpha(label_alpha + 5)
#             else:
#                 self.press_space_label.content.text.set_alpha(label_alpha - 5)
#             for ball in self.balls_group:
#                 ball.hitbox.centerx = self.platform_group.sprite.rect.centerx
#                 ball.rect.centerx = self.platform_group.sprite.rect.centerx
#
#     def handle_buffs(self):
#         self.passive_buffs_group.update()
#         if 'x-ray' in self.active_buffs_types:
#             self.passive_buffs_group.draw(constants.WIN)
#         if 'ghost_ball' in self.active_buffs_types:
#             for ball in self.balls_group:
#                 if ball.alpha == -100:
#                     ball.visibility_state = 'appear'
#                 elif ball.alpha == 255:
#                     ball.visibility_state = 'disappear'
#                 if ball.visibility_state == 'appear':
#                     ball.alpha += 5
#                     ball.image.set_alpha(ball.alpha)
#                 elif ball.visibility_state == 'disappear':
#                     ball.alpha -= 5
#                     ball.image.set_alpha(ball.alpha)


class SurfaceMaker:

    def __init__(self):
        self.saved_brick_surfs = {}
        self.saved_platform_surfs = {}
        self.darker_shade = pg.Color(40, 40, 40)

    def make_brick_surf(self, size, color, armor):
        if (color, size, armor) in self.saved_brick_surfs.keys():
            return self.saved_brick_surfs[(color, size, armor)]
        else:
            init_color = pg.color.Color(color)
            dark_color = init_color - self.darker_shade
            darker_color = dark_color - self.darker_shade
            dark_color.a = 255
            darker_color.a = 255
            new_surf = pg.Surface(size)
            new_surf.set_colorkey((0, 0, 0))
            new_surf.fill(darker_color)
            new_surf.fill(dark_color, (5 * constants.X_COEFFICIENT, 5 * constants.Y_COEFFICIENT, size[0] - 10 * constants.X_COEFFICIENT, size[1] - 10 * constants.Y_COEFFICIENT))
            new_surf.fill(init_color, (10 * constants.X_COEFFICIENT, 10 * constants.Y_COEFFICIENT, size[0] - 20 * constants.X_COEFFICIENT, size[1] - 20 * constants.Y_COEFFICIENT))
            if armor > 0:
                armor_surf = pg.Surface(size)
                armor_surf.fill('gray49')
                piece_x, piece_y = 0, 0
                piece_size = (armor_surf.get_width() - (5 * constants.X_COEFFICIENT * armor)) / (armor + 1), (armor_surf.get_height() - (5 * constants.Y_COEFFICIENT * armor)) / (armor + 1)
                delta_piece_x, delta_piece_y = piece_size[0] + 5 * constants.X_COEFFICIENT, piece_size[1] + 5 * constants.Y_COEFFICIENT
                for pos in range((armor + 1) ** 2):
                    if pos % (armor + 1) == 0 and pos != 0:
                        piece_x, piece_y = 0, piece_y + delta_piece_y
                    armor_surf.fill('white', ((piece_x, piece_y), piece_size))
                    piece_x += delta_piece_x
                armor_surf.set_colorkey('white')
                new_surf.blit(armor_surf, (0, 0))
            self.saved_brick_surfs.update({(color, size, armor): new_surf})
            return new_surf

    def make_platform_surf(self, size):
        if tuple(size) in self.saved_platform_surfs.keys():
            return self.saved_brick_surfs[size]
        else:
            new_surf = pg.Surface(size).convert_alpha()
            new_surf.set_colorkey((0, 0, 0))
            left_piece = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/platform/left.png'), (size[1] * (6 / 5), size[1])).convert_alpha()
            core_piece = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/platform/core.png'), (size[1] * (4 / 5), size[1])).convert_alpha()
            right_piece = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/platform/right.png'), (size[1] * (6 / 5), size[1])).convert_alpha()
            body_piece = pg.transform.scale(pg.image.load('arkanoid/resources/graphics/game/platform/body.png'), ((size[0] - left_piece.get_width() - core_piece.get_width() - right_piece.get_width()) / 2, size[1])).convert_alpha()
            new_surf.blit(left_piece, (0, 0))
            new_surf.blit(body_piece, (left_piece.get_width(), 0))
            new_surf.blit(core_piece, (left_piece.get_width() + body_piece.get_width(), 0))
            new_surf.blit(body_piece, (left_piece.get_width() + body_piece.get_width() + core_piece.get_width(), 0))
            new_surf.blit(right_piece, (left_piece.get_width() + body_piece.get_width() * 2 + core_piece.get_width(), 0))
            self.saved_brick_surfs.update({tuple(size): new_surf})
            return new_surf


class Border(pg.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        self.x, self.y = pos
        self.size = size
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        # self.image = pg.Surface(self.size)
        self.mask = pg.mask.Mask(self.size, True)


class Brick(pg.sprite.Sprite):

    def __init__(self, level, pos, size, color, armor=0):
        super().__init__()
        self.level = level
        self.x, self.y = pos
        self.size = size
        self.color = color
        if self.color == 'gray':
            self.armor = 0
        else:
            self.armor = armor
        self.image = pg.Surface(self.size).convert()
        self.update_appearance()
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        self.mask = pg.mask.from_surface(self.image)
        self.content = choice([None, None, None, 'buff'])
        if self.content == 'buff':
            Buff(self.level, self)

    def got_hit(self):
        if self.color == 'gray':
            constants.BUMP_SOUND.stop_play()
        else:
            self.armor -= 1
            if self.armor >= 0:
                constants.DAMAGE_SOUND.stop_play()
                self.update_appearance()
            else:
                constants.EXPLOSION_SOUND.stop_play()
                self.kill()
                for buff in self.level.passive_buffs_group:
                    if buff.brick_holder == self and buff.state == 'passive':
                        buff.state = 'fall'

    def update_appearance(self):
        self.image = constants.SURFACEMAKER.make_brick_surf(self.size, self.color, self.armor)

        # brick_filling = pg.image.load(f'objects/bricks/{self.color}.png').convert()
        # self.image.fill('black')
        # if self.armor > 0:
        #     self.image.blit(pg.transform.scale(pg.image.load(f'objects/bricks/gray.png').convert(), (self.size[0] - 10 * constants.X_COEFFICIENT, self.size[1] - 10 * constants.Y_COEFFICIENT)), (5 * constants.X_COEFFICIENT, 5 * constants.Y_COEFFICIENT))
        #     inner_size = self.size[0] - 10 * constants.X_COEFFICIENT, self.size[1] - 10 * constants.Y_COEFFICIENT
        #     piece_x, piece_y = 5 * constants.X_COEFFICIENT, 5 * constants.Y_COEFFICIENT
        #     piece_size = (inner_size[0] - (5 * constants.X_COEFFICIENT * self.armor)) / (self.armor + 1), (inner_size[1] - (5 * constants.Y_COEFFICIENT * self.armor)) / (self.armor + 1)
        #     delta_piece_x, delta_piece_y = piece_size[0] + 5 * constants.X_COEFFICIENT, piece_size[1] + 5 * constants.Y_COEFFICIENT
        #     for pos in range((self.armor + 1) ** 2):
        #         if pos % (self.armor + 1) == 0 and pos != 0:
        #             piece_x, piece_y = 5 * constants.X_COEFFICIENT, piece_y + delta_piece_y
        #         self.image.blit(pg.transform.scale(brick_filling, piece_size), (piece_x, piece_y))
        #         piece_x += delta_piece_x
        # else:
        #     self.image.blit(pg.transform.scale(brick_filling, (self.size[0] - 10 * constants.X_COEFFICIENT, self.size[1] - 10 * constants.Y_COEFFICIENT)), (5 * constants.X_COEFFICIENT, 5 * constants.Y_COEFFICIENT))


class Platform(pg.sprite.Sprite):

    def __init__(self, level, pos, size, vel):
        super().__init__()
        self.level = level
        self.x, self.y = pos
        self.size = size
        self.desired_size = size.copy() # is needed for buffs 'wide_platform' and 'narrow_platform' handling
        self.width_scaler = None # is a piece of the difference between size and desire_size which gradually scales width to the desired one
        self.image = constants.SURFACEMAKER.make_platform_surf(self.size)
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        self.mask = pg.mask.from_surface(self.image)
        self.vel = vel

    def update(self):
        if constants.CONTROL_TYPE == 'keyboard':
            key_pressed = pg.key.get_pressed()
            if key_pressed[pg.K_LEFT] or key_pressed[pg.K_a]:
                self.rect.x -= self.vel * constants.X_COEFFICIENT
            if key_pressed[pg.K_RIGHT] or key_pressed[pg.K_d]:
                self.rect.x += self.vel * constants.X_COEFFICIENT
        elif constants.CONTROL_TYPE == 'mouse':
            mouse_pos = pg.mouse.get_pos()
            if not self.rect.colliderect(self.level.left_border.rect) and not self.rect.colliderect(self.level.right_border.rect):
                if not -self.vel * constants.X_COEFFICIENT < mouse_pos[0] - self.rect.centerx < self.vel * constants.X_COEFFICIENT:
                    if mouse_pos[0] >= self.rect.centerx:
                        self.rect.centerx += self.vel * constants.X_COEFFICIENT
                    elif mouse_pos[0] <= self.rect.centerx:
                        self.rect.centerx -= self.vel * constants.X_COEFFICIENT
                else:
                    self.rect.centerx = mouse_pos[0]
        if self.rect.left < self.level.left_border.rect.right: # checks if the platform is located within the bounds and teleports it to the closest border (left or right) if the previous condition is false
            self.rect.left = self.level.left_border.rect.right
        elif self.rect.right > self.level.right_border.rect.left:
            self.rect.right = self.level.right_border.rect.left
        # hitbox = (pg.Surface(self.rect.size)).convert_alpha()
        # hitbox.fill((255, 255, 255, 125))
        # constants.WIN.blit(hitbox, self.rect) # draw a rectangle (hitbox) on the screen for tests

    def update_appearance(self):
        rect_center = self.rect.center
        self.rect = pg.Rect((0, 0), self.size)
        self.rect.center = rect_center
        self.image = constants.SURFACEMAKER.make_platform_surf(self.size)
        self.mask = pg.mask.from_surface(self.image)


class Ball(pg.sprite.Sprite):

    def __init__(self, level, pos, size, shape, vel, x_move=None, y_move=None, frame_index=0, anim_speed=0.2):
        super().__init__()
        self.level = level
        self.x, self.y = pos
        self.init_size = size
        self.shape = shape # original shape of the ball
        self.frame_index = frame_index
        if self.shape == 'faceless':
            self.surf_name = choice(constants.AVAILABLE_SHAPES.split(',')[1:]) # faceless ball picks a random surface of the other shapes
        else:
            self.surf_name = self.shape
        self.anim_speed = anim_speed
        self.surf_frames = [pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/game/ball_shapes/{self.surf_name}/{index}.png'), self.init_size).convert_alpha() for index in range(len(listdir(f'arkanoid/resources/graphics/game/ball_shapes/{self.surf_name}/')))] # creates a list of frames by for-loop, iteration number of which is defined by the number of files in the directory
        self.init_surf = self.surf_frames[self.frame_index]
        self.image = self.init_surf.copy() # a copy of the initial surface which will be modified
        self.surf_rot_angle = 0 # an angle of the surface rotation
        self.rect = pg.Rect(self.x, self.y, self.init_size[0], self.init_size[1])
        self.hitbox = self.rect.copy() # a rectangle used exclusively for collisions
        self.old_hitbox = self.hitbox.copy()
        self.collision_info_storage = {'bricks': [], 'platform': {}} # a dictionary with the necessary information, which is collected in the first frame of the hitbox collision, used in side detection
        self.mask = pg.mask.from_surface(self.image)
        self.vel = vel
        self.alpha = 255
        self.visibility_state = 'disappear'
        if not x_move: # at the beginning if the original trajectory is not specified, it is chosen randomly
            x_move = randint(0, 95) / 100
        if not y_move:
            y_move = -sqrt(1 - x_move ** 2) # scales y_move relatively to x_move
        self.x_move, self.y_move = x_move, y_move

    def update(self):
        # collision detection and ball movement
        self.detect_brick_collision()
        self.detect_platform_collision()
        self.detect_border_collision()
        self.old_hitbox = self.hitbox.copy()
        self.hitbox.x += self.vel * self.x_move * constants.X_COEFFICIENT
        self.hitbox.y += self.vel * self.y_move * constants.Y_COEFFICIENT
        self.rect.center = self.hitbox.center
        # print(f'old_rect: ({self.old_rect.x, self.old_rect.y}), rect: ({self.rect.x, self.rect.y})')
        # hitbox_surf = (pg.Surface(self.hitbox.size)).convert_alpha()
        # hitbox_surf.fill((255, 0, 0, 125))
        # constants.WIN.blit(hitbox_surf, self.hitbox)  # draw a rectangle (hitbox) on the screen for tests

        # ball animation
        if constants.SHAPE_ANIMATION and self.level.started is True:

            # shape animation (frame by frame)
            self.frame_index += self.anim_speed
            if self.frame_index >= len(self.surf_frames):
                self.frame_index -= len(self.surf_frames)
            self.image = self.surf_frames[int(self.frame_index)]

            # ball rotation animation
            self.image = pg.transform.rotate(self.image, self.surf_rot_angle)
            if self.surf_rot_angle <= -360:
                self.surf_rot_angle = 0 + (self.surf_rot_angle % -360) # sets the angle to the scope of 360 if the ball starts making a 2nd loop of rotation
            elif self.surf_rot_angle >= 360:
                self.surf_rot_angle = 0 + (self.surf_rot_angle % 360)
            elif self.surf_name == 'shuriken':
                self.surf_rot_angle += -self.x_move * 10 # shuriken rotates faster compared to other shapes
            else:
                self.surf_rot_angle += -self.x_move * 5
            rot_rect = self.image.get_rect(center = self.rect.center)  # a rectangle that will contain a rotated surface which is slightly bigger than the original one
            self.rect = rot_rect
            self.mask = pg.mask.from_surface(self.image)

    def detect_brick_collision(self):
        # hit_bricks_list = [brick for brick in constants.LEVEL.bricks_group if brick.rect.colliderect(self.hitbox) and brick not in self.last_collided_bricks]
        # if len(hit_bricks_list) > 0:
        if pg.sprite.spritecollideany(self, self.level.bricks_group):
            collision_info = [{'brick': brick, 'hitbox': self.hitbox, 'old_hitbox': self.old_hitbox, 'x_move': self.x_move, 'y_move': self.y_move} for brick in self.level.bricks_group if self.hitbox.colliderect(brick.rect) and brick not in [d['brick'] for d in self.collision_info_storage['bricks']]] # loops every collided with ball's hitbox brick and checks whether the brick is already in the storage and if not, then it keeps the necessary info in the variable
            if len(collision_info) > 0:
                self.collision_info_storage['bricks'].extend(collision_info)
            hit_bricks_by_masks = pg.sprite.spritecollide(self, self.level.bricks_group, False, pg.sprite.collide_mask) # a list of bricks which collided with the ball by mask
            if len(hit_bricks_by_masks) > 0:
                for info_dict in self.collision_info_storage['bricks']:
                    if info_dict['brick'] in hit_bricks_by_masks:
                        info_dict['brick'].got_hit()
                        self.detect_brick_side(info_dict)
                        self.collision_info_storage['bricks'].remove(info_dict)
        else:
            self.collision_info_storage['bricks'].clear()
            # for brick in hit_bricks_list:
                    # brick_index = hit_bricks_list.index(brick)
                    # brick.got_hit()
                    # self.last_collided_bricks.append(brick)
                # if len(hit_bricks_list) == 1:
                #     hit_rect = hit_bricks_list[0].rect
                # else:
                #     hit_rect = pg.Rect(hit_bricks_list[0].rect.topleft, (hit_bricks_list[-1].rect.right - hit_bricks_list[0].rect.left, hit_bricks_list[-1].rect.bottom - hit_bricks_list[0].rect.top))
                # self.detect_brick_side(hit_rect)
        # else:
        #     self.last_collided_bricks.clear()

    def detect_platform_collision(self):
        # if self.hitbox.colliderect(constants.LEVEL.platform_group.sprite.rect) and self.y_move > 0:
        if self.hitbox.colliderect(self.level.platform.rect):
            if len(self.collision_info_storage['platform']) == 0:
                self.collision_info_storage['platform'] = {'platform_rect': self.level.platform.rect, 'hitbox': self.hitbox, 'old_hitbox': self.old_hitbox, 'x_move': self.x_move, 'y_move': self.y_move} # adds the necessary info of collision to the storage
            if pg.sprite.spritecollideany(self, self.level.platform_group, pg.sprite.collide_mask):
                constants.BOUNCE_SOUND.stop_play()
                collision_info = self.collision_info_storage['platform']
                platform_rect, hitbox, old_hitbox, x_move, y_move = collision_info['platform_rect'], collision_info['hitbox'], collision_info['old_hitbox'], collision_info['x_move'], collision_info['y_move']
                if x_move > 0 and old_hitbox.right <= platform_rect.left <= hitbox.right:  # check collision between the right side of the ball and the left side of the platform
                    self.x_move = -abs(self.x_move)
                    self.hitbox.right = self.level.platform.rect.left
                elif x_move < 0 and hitbox.left <= platform_rect.right <= old_hitbox.left:  # check collision between the left side of the ball and the right side of the platform
                    self.x_move = abs(self.x_move)
                    self.hitbox.left = self.level.platform.rect.right
                if y_move > 0 and old_hitbox.bottom <= platform_rect.top <= hitbox.bottom:  # check collision between the bottom side of the ball and the top side of the platform
                    if 'chaotic_ball' not in self.level.active_buffs_types:
                        loc = self.hitbox.centerx - self.level.platform.rect.centerx # location of the ball center relatively to platform center
                        max_move = 0.9
                        super_max_move = 0.95
                        new_move = (2 * max_move * loc) / self.level.platform.rect.width
                        if new_move < -max_move:
                            new_move = -(max_move + ((2 * (super_max_move - max_move) * (self.level.platform.rect.left - self.hitbox.centerx)) / self.hitbox.width))
                        elif new_move > max_move:
                            new_move = max_move + ((2 * (super_max_move - max_move) * (self.hitbox.centerx - self.level.platform.rect.right)) / self.hitbox.width)
                        self.x_move = new_move
                    else:
                        self.x_move = randint(0, 95) / 100
                    self.y_move = -sqrt(1 - self.x_move ** 2)
                    self.hitbox.bottom = self.level.platform.rect.top
                # elif y_move < 0 and hitbox.top <= platform_rect.bottom <= old_hitbox.top:  # check collision between the top side of the ball and the bottom side of the platform
                #     self.y_move = abs(self.y_move)
                #     self.hitbox.top = constants.LEVEL.platform_group.sprite.rect.bottom
                self.collision_info_storage['platform'] = {}

                # if self.hitbox.bottom - constants.LEVEL.platform_group.sprite.rect.top <= 2 * self.vel * constants.Y_COEFFICIENT:
                #     constants.BOUNCE_SOUND.stop_play()
                #
                # elif self.hitbox.bottom - constants.LEVEL.platform_group.sprite.rect.top > 2 * self.vel * constants.Y_COEFFICIENT:
                #     if constants.BOUNCE_SOUND.get_busy() is False:
                #         constants.BOUNCE_SOUND.play()
                #     if self.hitbox.x < constants.LEVEL.platform_group.sprite.rect.x:
                #         self.x_move = -abs(self.x_move)
                #     if self.hitbox.right > constants.LEVEL.platform_group.sprite.rect.right:
                #         self.x_move = abs(self.x_move)

    def detect_border_collision(self):
        # if self.rect.top > self.level.bottom_border.rect.bottom:
        #     self.kill()
        # elif pg.sprite.spritecollideany(self, self.level.borders_group):
        if pg.sprite.spritecollideany(self, self.level.borders_group):
            if self.y_move < 0 and pg.sprite.collide_mask(self, self.level.top_border) is not None:
                constants.BOUNCE_SOUND.stop_play()
                self.y_move = abs(self.y_move)
            if self.y_move > 0 and pg.sprite.collide_mask(self, self.level.bottom_border) is not None:
                constants.BOUNCE_SOUND.stop_play()
                self.y_move = -abs(self.y_move)
            if self.x_move < 0 and pg.sprite.collide_mask(self, self.level.left_border) is not None:
                constants.BOUNCE_SOUND.stop_play()
                self.x_move = abs(self.x_move)
            if self.x_move > 0 and pg.sprite.collide_mask(self, self.level.right_border) is not None:
                constants.BOUNCE_SOUND.stop_play()
                self.x_move = -abs(self.x_move)

    def detect_brick_side(self, collision_info):
        brick_rect, hitbox, old_hitbox, x_move, y_move = collision_info['brick'].rect, collision_info['hitbox'], collision_info['old_hitbox'], collision_info['x_move'], collision_info['y_move']
        if x_move > 0 and old_hitbox.right <= brick_rect.left <= hitbox.right: # check collision between the right side of the ball and the left side of the brick
            self.x_move = -abs(x_move)
            # print(f"brick's left      self.x_move = {self.x_move}")
            self.hitbox.right = brick_rect.left
        elif x_move < 0 and hitbox.left <= brick_rect.right <= old_hitbox.left: # check collision between the left side of the ball and the right side of the brick
            self.x_move = abs(x_move)
            # print(f"brick's right      self.x_move = {self.x_move}")
            self.hitbox.left = brick_rect.right
        if y_move > 0 and old_hitbox.bottom <= brick_rect.top <= hitbox.bottom: # check collision between the bottom side of the ball and the top side of the brick
            self.y_move = -abs(y_move)
            # print(f"brick's top      self.y_move = {self.y_move}")
            self.hitbox.bottom = brick_rect.top
        elif y_move < 0 and hitbox.top <= brick_rect.bottom <= old_hitbox.top: # check collision between the top side of the ball and the bottom side of the brick
            self.y_move = abs(y_move)
            # print(f"brick's bottom      self.y_move = {self.y_move}")
            self.hitbox.top = brick_rect.bottom


class Shape(pg.sprite.Sprite):

    def __init__(self, pos, size, surf_name, frame_index=0, anim_speed=0.2):
        super().__init__()
        self.x, self.y = pos
        self.size = size
        self.surf_name = surf_name
        self.frame_index = frame_index
        self.anim_speed = anim_speed
        self.surf_frames = [pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/game/ball_shapes/{self.surf_name}/{index}.png'), self.size).convert_alpha() for index in range(len(listdir(f'arkanoid/resources/graphics/game/ball_shapes/{self.surf_name}/')))] # creates a list of frames by for-loop, iteration number of which is defined by the number of files in the directory
        self.image = self.surf_frames[self.frame_index]
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        if self.surf_name == 'faceless':
            self.name = 'Faceless'
            self.description = 'A mysterious ball that can take different shapes'
        elif self.surf_name == 'red_ball':
            self.name = 'Red Ball'
            self.description = 'Just a usual red ball. What else do you need?'
        elif self.surf_name == 'pacman':
            self.name = 'Pac-Man'
            self.description = 'A creature from the well-known arcade game'
        elif self.surf_name == 'scarabeus':
            self.name = 'Scarabeus'
            self.description = 'A golden amulet which symbolizes the God Khepri'
        elif self.surf_name == 'shield':
            self.name = 'Shield'
            self.description = 'A medieval shield that has been lost by a knight'
        elif self.surf_name == 'shuriken':
            self.name = 'Shuriken'
            self.description = "A concealed throwing weapon in a samurai's arsenal"

    def update(self):
        if constants.SHAPE_ANIMATION:
            self.frame_index += self.anim_speed
            if self.frame_index >= len(self.surf_frames):
                self.frame_index -= len(self.surf_frames)
            self.image = self.surf_frames[int(self.frame_index)]


class Buff(pg.sprite.Sprite):

    def __init__(self, level, brick_holder):
        super().__init__()
        self.level = level
        self.level.passive_buffs_group.add(self)
        self.state = 'passive'
        self.type = choice(['slow_ball', 'fast_ball', 'narrow_platform', 'wide_platform', 'more_balls', 'chaotic_ball', 'x-ray', 'ghost_ball'])
        self.brick_holder = brick_holder
        self.size = 40 * constants.X_COEFFICIENT, 40 * constants.Y_COEFFICIENT
        self.image = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/game/buffs/{self.type}.png'), self.size).convert_alpha()
        self.rect = self.image.get_rect(center=brick_holder.rect.center)
        self.timer = Timer(7.5, self.cancel_buff)

    def update(self): # detect buff state
        if self.state == 'fall':
            if self.rect.colliderect(self.level.platform.rect):
                constants.BUFF_SOUND.stop_play()
                self.state = 'active'
                self.level.passive_buffs_group.remove(self)
                self.level.active_buffs_group.add(self)
                self.level.active_buffs_types.append(self.type)
                self.apply_buff()
            elif self.rect.top > self.level.bottom_border.rect.bottom:
                self.kill()
            else:
                self.rect.y += 5 * constants.Y_COEFFICIENT
                constants.WIN.blit(self.image, (self.rect.x, self.rect.y))

    def apply_buff(self):
        if self.type == 'slow_ball':
            for ball in self.level.balls_group:
                ball.vel *= 0.75
        elif self.type == 'fast_ball':
            for ball in self.level.balls_group:
                ball.vel *= 1.25
        elif self.type == 'narrow_platform':
            if self.level.platform.size[0] > 136 * constants.X_COEFFICIENT: # 95 pixels is a minimum platform width
                self.level.platform.desired_size[0] *= 0.7
                width_diff = self.level.platform.desired_size[0] - self.level.platform.size[0]
                self.level.platform.width_scaler = width_diff / 30
                self.timer = Timer(10, self.cancel_buff)
            else:
                self.kill()
                self.level.active_buffs_types.remove(self.type)
        elif self.type == 'wide_platform':
            if self.level.platform.size[0] < 1107 * constants.X_COEFFICIENT:  # 1440 pixels is a maximum platform width
                self.level.platform.desired_size[0] *= 1.3
                width_diff = self.level.platform.desired_size[0] - self.level.platform.size[0]
                self.level.platform.width_scaler = width_diff / 30
                self.timer = Timer(10, self.cancel_buff)
            else:
                self.kill()
                self.level.active_buffs_types.remove(self.type)
        elif self.type == 'more_balls':
            first_ball = self.level.balls_group.sprites()[0]
            self.level.balls_group.add(Ball(self.level, (self.level.platform.rect.centerx - (first_ball.init_size[0] / 2), first_ball.y), first_ball.init_size, first_ball.shape, first_ball.vel))
            self.level.balls_group.add(Ball(self.level, (self.level.platform.rect.centerx - (first_ball.init_size[0] / 2), first_ball.y), first_ball.init_size, first_ball.shape, first_ball.vel))
            self.timer = None
        elif self.type == 'chaotic_ball':
            self.timer = Timer(20, self.cancel_buff)
        elif self.type == 'x-ray':
            self.timer = Timer(3, self.cancel_buff)
        elif self.type == 'ghost_ball':
            self.timer = Timer(10, self.cancel_buff)
        if self.timer:
            self.timer.start()

    def cancel_buff(self):
        self.kill()
        self.level.active_buffs_types.remove(self.type)
        if self.type == 'slow_ball':
            for ball in self.level.balls_group:
                ball.vel /= 0.75
        elif self.type == 'fast_ball':
            for ball in self.level.balls_group:
                ball.vel /= 1.25
        elif self.type == 'narrow_platform':
            self.level.platform.desired_size[0] /= 0.7
            width_diff = self.level.platform.desired_size[0] - self.level.platform.size[0]
            self.level.platform.width_scaler = width_diff / 30
        elif self.type == 'wide_platform':
            self.level.platform.desired_size[0] /= 1.3
            width_diff = self.level.platform.desired_size[0] - self.level.platform.size[0]
            self.level.platform.width_scaler = width_diff / 30
        elif self.type == 'ghost_ball':
            for ball in self.level.balls_group:
                ball.alpha = 255
                ball.visibility_state = 'disappear'
                ball.image.set_alpha(ball.alpha)
