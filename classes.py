import pygame
import basics
from main import run_pause
from random import choice, randint
from threading import Timer
from math import sqrt
from os import listdir
pygame.init()


class Music:

    def __init__(self, filename, volume):
        self.name = pygame.mixer.Sound(filename)
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
        self.name.set_volume(basics.VOLUME * basics.MUSIC_VOLUME * self.volume)


class Sound:

    def __init__(self, filename, volume):
        self.name = pygame.mixer.Sound(filename)
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
        self.name.set_volume(basics.VOLUME * basics.SOUND_VOLUME * self.volume)


class Label:

    def __init__(self, text, font_size, font, fg, bg=None, antialias=False, **pos):
        self.font = pygame.font.Font(font, int(font_size))
        self.text = self.font.render(text, antialias, fg)
        finished_fonts = ['fonts/pixeboy_font.ttf', 'fonts/connection_font.ttf', 'fonts/retroblaze_font.ttf']
        self.surf = pygame.Surface(self.text.get_size()).convert()
        self.bg = bg
        if bg:
            self.surf.fill(bg)
        if font not in finished_fonts:
            self.surf.blit(self.text, (font_size / 20, 0))
        else:
            self.surf.blit(self.text, (0, 0))
        self.rect = self.text.get_rect(**pos)

    def show(self):
        if self.bg:
            basics.WIN.blit(self.surf, self.rect)
        else:
            basics.WIN.blit(self.text, self.rect)


class Image:

    def __init__(self, file_name, size, **pos):
        self.image = pygame.transform.scale(pygame.image.load(file_name), size).convert_alpha()
        self.rect = self.image.get_rect(**pos)

    def show(self):
        basics.WIN.blit(self.image, self.rect)


class Button:

    def __init__(self, label, image, selection='glow', arrows_color=None, clickable=True, key=None, feedbacks=None):
        if label:
            self.content = label
        elif image:
            self.content = image
        if selection == 'glow':
            selection_surf = pygame.Surface((self.content.rect.size[0] + 16 * basics.X_COEFFICIENT, self.content.rect.size[1] + 16 * basics.Y_COEFFICIENT)).convert()
            selection_surf.fill('white')
            selection_surf.set_alpha(120)
            self.selection_surfs = {selection_surf: selection_surf.get_rect(center=self.content.rect.center)}
        elif selection == 'arrows':
            left_arrow = pygame.transform.scale(pygame.image.load(f'objects/selection_arrows/{arrows_color}_left.png'), (self.content.rect.size[1] / 3.6, self.content.rect.size[1] / 2)).convert_alpha()
            right_arrow = pygame.transform.scale(pygame.image.load(f'objects/selection_arrows/{arrows_color}_right.png'), (self.content.rect.size[1] / 3.6, self.content.rect.size[1] / 2)).convert_alpha()
            self.selection_surfs = {left_arrow: (self.content.rect.left - 8 * basics.X_COEFFICIENT - left_arrow.get_width(), self.content.rect.centery - left_arrow.get_height() / 2), right_arrow: (self.content.rect.right + 8 * basics.X_COEFFICIENT, self.content.rect.centery - right_arrow.get_height() / 2)}
        self.selection = selection
        self.mouse_cooldown = False
        self.key_cooldown = False
        self.sound_cooldown = False
        self.clickable = clickable
        self.key = key
        self.feedbacks = feedbacks

    def detect_mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.content.rect.collidepoint(mouse_pos):
            if self.sound_cooldown is True and self.selection == 'arrows':
                self.sound_cooldown = False
                basics.SELECTION_SOUND.play()
            for surf, pos in self.selection_surfs.items():
                basics.WIN.blit(surf, pos)
            return True
        elif self.sound_cooldown is False:
            self.sound_cooldown = True

    def detect_press(self):
        if self.clickable is True:
            if self.detect_mouse_collision() is True and pygame.mouse.get_pressed()[0] and self.mouse_cooldown is True:
                self.mouse_cooldown = False
                return True
            if not pygame.mouse.get_pressed()[0] and self.mouse_cooldown is False:
                self.mouse_cooldown = True
        if self.key:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[self.key] and self.key_cooldown is True:
                self.key_cooldown = False
                return True
            elif not key_pressed[self.key] and self.key_cooldown is False:
                self.key_cooldown = True

    def give_feedback(self):
        for feedback in self.feedbacks:
            if type(feedback) == list:
                feedback[0](feedback[1])
            else:
                feedback()

    def show(self):
        self.content.show()

    def all_in_one(self):
        if self.detect_press() is True:
            if self.feedbacks:
                self.give_feedback()
            else:
                return True
        self.show()


class LevelControl:

    def __init__(self, bg, music, platform):
        self.started = False
        self.countdown_state = False
        self.countdown_index = 0
        self.press_space_label = Button(Label('Press SPACE to start', 50 * basics.FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', 'red', center=(basics.WIN_RECT.right / 2, basics.WIN_RECT.height / 2)), None, clickable=False, key=pygame.K_SPACE)
        self.press_space_label.content.text.set_alpha(0)
        self.press_space_state = 'appear'
        self.bg = bg
        self.music = music
        self.borders_group = pygame.sprite.Group(basics.TOP_BORDER, basics.LEFT_BORDER, basics.RIGHT_BORDER, basics.BOTTOM_BORDER)
        self.upper_menu = pygame.Rect(0, 0, basics.WIN_RECT.width, 116 * basics.Y_COEFFICIENT)
        self.pause_button = Button(None, Image('objects/pause_button.png', (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), topleft=(8 * basics.X_COEFFICIENT, 8 * basics.Y_COEFFICIENT)), key=pygame.K_ESCAPE, feedbacks=[run_pause])
        self.platform_group = pygame.sprite.GroupSingle(platform)
        self.balls_group = pygame.sprite.Group()
        self.bricks_group = pygame.sprite.Group()
        self.passive_buffs_group = pygame.sprite.Group()
        self.active_buffs_group = pygame.sprite.Group()
        self.active_buffs_types = []

    def detect_start(self):
        if self.started is False and self.press_space_label.all_in_one() is True:
            # press_space_label.content.text.set_alpha(basics.LEVEL.press_space_alpha)
            self.started = True
            self.music.play(loops=-1)
        if self.started is True:
            self.balls_group.update()
        else:
            label_alpha = self.press_space_label.content.text.get_alpha()
            if label_alpha is None:
                label_alpha = 255
            if label_alpha >= 255:
                self.press_space_state = 'disappear'
            elif label_alpha <= 0:
                self.press_space_state = 'appear'
            if self.press_space_state == 'appear':
                self.press_space_label.content.text.set_alpha(label_alpha + 5)
            else:
                self.press_space_label.content.text.set_alpha(label_alpha - 5)
            for ball in self.balls_group:
                ball.hitbox.centerx = self.platform_group.sprite.rect.centerx
                ball.rect.centerx = self.platform_group.sprite.rect.centerx

    def handle_buffs(self):
        self.passive_buffs_group.update()
        if 'x-ray' in self.active_buffs_types:
            self.passive_buffs_group.draw(basics.WIN)
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


class SurfaceMaker:

    def __init__(self):
        self.saved_brick_surfs = {}
        self.saved_platform_surfs = {}
        self.darker_shade = pygame.Color(40, 40, 40)

    def make_brick_surf(self, size, color):
        if (color, size) in self.saved_brick_surfs.keys():
            return self.saved_brick_surfs[(color, size)]
        else:
            init_color = pygame.color.Color(color)
            dark_color = init_color - self.darker_shade
            darker_color = dark_color - self.darker_shade
            dark_color.a = 255
            darker_color.a = 255
            surf = pygame.Surface(size)
            surf.set_colorkey((0, 0, 0))
            surf.fill(darker_color)
            surf.fill(dark_color, (5 * basics.X_COEFFICIENT, 5 * basics.Y_COEFFICIENT, size[0] - 10 * basics.X_COEFFICIENT, size[1] - 10 * basics.Y_COEFFICIENT))
            surf.fill(init_color, (10 * basics.X_COEFFICIENT, 10 * basics.Y_COEFFICIENT, size[0] - 20 * basics.X_COEFFICIENT, size[1] - 20 * basics.Y_COEFFICIENT))
            self.saved_brick_surfs.update({(color, size): surf})
            return surf

    def make_platform_surf(self):
        pass


class Border(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        self.x, self.y = pos
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        # self.image = pygame.Surface(self.size)
        self.mask = pygame.mask.Mask(self.size, True)


class Brick(pygame.sprite.Sprite):

    def __init__(self, pos, size, color, armor=0):
        super().__init__()
        self.x, self.y = pos
        self.size = size
        self.color = color
        if self.color == 'gray':
            self.armor = 0
        else:
            self.armor = armor
        self.image = pygame.Surface(self.size).convert()
        self.alter_appearance()
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.mask = pygame.mask.from_surface(self.image)
        self.content = choice([None, None, None, 'buff'])
        if self.content == 'buff':
            Buff(self)

    def got_hit(self):
        if self.color == 'gray':
            basics.BUMP_SOUND.stop_play()
        else:
            self.armor -= 1
            if self.armor >= 0:
                basics.DAMAGE_SOUND.stop_play()
                self.alter_appearance()
            else:
                basics.EXPLOSION_SOUND.stop_play()
                self.kill()
                for buff in basics.LEVEL.passive_buffs_group:
                    if buff.brick_holder == self and buff.state == 'passive':
                        buff.state = 'fall'

    def alter_appearance(self):
        self.image = basics.SURFACEMAKER.make_brick_surf(self.size, self.color)

        # brick_filling = pygame.image.load(f'objects/bricks/{self.color}.png').convert()
        # self.image.fill('black')
        # if self.armor > 0:
        #     self.image.blit(pygame.transform.scale(pygame.image.load(f'objects/bricks/gray.png').convert(), (self.size[0] - 10 * basics.X_COEFFICIENT, self.size[1] - 10 * basics.Y_COEFFICIENT)), (5 * basics.X_COEFFICIENT, 5 * basics.Y_COEFFICIENT))
        #     inner_size = self.size[0] - 10 * basics.X_COEFFICIENT, self.size[1] - 10 * basics.Y_COEFFICIENT
        #     piece_x, piece_y = 5 * basics.X_COEFFICIENT, 5 * basics.Y_COEFFICIENT
        #     piece_size = (inner_size[0] - (5 * basics.X_COEFFICIENT * self.armor)) / (self.armor + 1), (inner_size[1] - (5 * basics.Y_COEFFICIENT * self.armor)) / (self.armor + 1)
        #     delta_piece_x, delta_piece_y = piece_size[0] + 5 * basics.X_COEFFICIENT, piece_size[1] + 5 * basics.Y_COEFFICIENT
        #     for pos in range((self.armor + 1) ** 2):
        #         if pos % (self.armor + 1) == 0 and pos != 0:
        #             piece_x, piece_y = 5 * basics.X_COEFFICIENT, piece_y + delta_piece_y
        #         self.image.blit(pygame.transform.scale(brick_filling, piece_size), (piece_x, piece_y))
        #         piece_x += delta_piece_x
        # else:
        #     self.image.blit(pygame.transform.scale(brick_filling, (self.size[0] - 10 * basics.X_COEFFICIENT, self.size[1] - 10 * basics.Y_COEFFICIENT)), (5 * basics.X_COEFFICIENT, 5 * basics.Y_COEFFICIENT))


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos, size, surf, vel):
        super().__init__()
        self.x, self.y = pos
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(surf), size).convert_alpha()
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.mask = pygame.mask.from_surface(self.image)
        self.vel = vel

    def update(self):
        if basics.CONTROL_TYPE == 'keyboard':
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT] and not self.rect.colliderect(basics.LEFT_BORDER.rect) or key_pressed[pygame.K_a] and not self.rect.colliderect(basics.LEFT_BORDER.rect):
                self.rect.x -= self.vel * basics.X_COEFFICIENT
            if key_pressed[pygame.K_RIGHT] and not self.rect.colliderect(basics.RIGHT_BORDER.rect) or key_pressed[pygame.K_d] and not self.rect.colliderect(basics.RIGHT_BORDER.rect):
                self.rect.x += self.vel * basics.X_COEFFICIENT
        elif basics.CONTROL_TYPE == 'mouse':
            mouse_pos = pygame.mouse.get_pos()
            left_center = self.rect.centerx - self.rect.left
            right_center = self.rect.right - self.rect.centerx
            if not self.rect.colliderect(basics.LEFT_BORDER.rect) and not self.rect.colliderect(basics.RIGHT_BORDER.rect):
                if not -self.vel * basics.X_COEFFICIENT < mouse_pos[0] - self.rect.centerx < self.vel * basics.X_COEFFICIENT:
                    if mouse_pos[0] >= self.rect.centerx:
                        self.rect.centerx += self.vel * basics.X_COEFFICIENT
                    elif mouse_pos[0] <= self.rect.centerx:
                        self.rect.centerx -= self.vel * basics.X_COEFFICIENT
                else:
                    self.rect.centerx = mouse_pos[0]
            elif left_center < mouse_pos[0] < basics.RIGHT_BORDER.x - right_center:
                if mouse_pos[0] > self.rect.centerx:
                    self.rect.centerx += self.vel * basics.X_COEFFICIENT
                elif mouse_pos[0] < self.rect.centerx:
                    self.rect.centerx -= self.vel * basics.X_COEFFICIENT
        # pygame.draw.rect(basics.WIN, basics.WHITE, self.rect) # draw a rectangle (hitbox) on the screen for tests


class Ball(pygame.sprite.Sprite):

    def __init__(self, pos, size, shape, vel, x_move=None, y_move=None, frame_index=0, anim_speed=0.2):
        super().__init__()
        self.x, self.y = pos
        self.init_size = size
        self.shape = shape # original shape of the ball
        self.frame_index = frame_index
        if self.shape == 'faceless':
            self.surf_name = choice(basics.AVAILABLE_SHAPES.split(',')[1:]) # faceless ball picks a random surface of the other shapes
        else:
            self.surf_name = self.shape
        self.anim_speed = anim_speed
        self.surf_frames = [pygame.transform.scale(pygame.image.load(f'objects/ball_shapes/{self.surf_name}/{index}.png'), self.init_size).convert_alpha() for index in range(len(listdir(f'objects/ball_shapes/{self.surf_name}/')) - 1)] # creates a list of frames by for-loop, iteration number of which is defined by the number of files in the directory
        self.init_surf = self.surf_frames[self.frame_index]
        self.image = self.init_surf.copy() # a copy of the initial surface which will be modified
        self.surf_rot_angle = 0 # an angle of the surface rotation
        self.rect = pygame.Rect(self.x, self.y, self.init_size[0], self.init_size[1])
        self.hitbox = self.rect.copy() # a rectangle used exclusively for collisions
        self.old_hitbox = self.hitbox.copy()
        self.collision_info_storage = {'bricks': [], 'platform': {}} # a dictionary with the necessary information, which is collected in the first frame of the hitbox collision, used in side detection
        self.mask = pygame.mask.from_surface(self.image)
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
        self.hitbox.x += self.vel * self.x_move * basics.X_COEFFICIENT
        self.hitbox.y += self.vel * self.y_move * basics.Y_COEFFICIENT
        self.rect.center = self.hitbox.center
        # print(f'old_rect: ({self.old_rect.x, self.old_rect.y}), rect: ({self.rect.x, self.rect.y})')
        # pygame.draw.rect(basics.WIN, basics.RED, self.hitbox) # draw a rectangle (hitbox) on the screen for tests

        # ball animation
        if basics.SHAPE_ANIMATION and basics.LEVEL.started is True:

            # shape animation (frame by frame)
            self.frame_index += self.anim_speed
            if self.frame_index >= len(self.surf_frames):
                self.frame_index -= len(self.surf_frames)
            self.image = self.surf_frames[int(self.frame_index)]

            # ball rotation animation
            self.image = pygame.transform.rotate(self.image, self.surf_rot_angle)
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
            self.mask = pygame.mask.from_surface(self.image)

    def detect_brick_collision(self):
        # hit_bricks_list = [brick for brick in basics.LEVEL.bricks_group if brick.rect.colliderect(self.hitbox) and brick not in self.last_collided_bricks]
        # if len(hit_bricks_list) > 0:
        if pygame.sprite.spritecollideany(self, basics.LEVEL.bricks_group):
            collision_info = [{'brick': brick, 'hitbox': self.hitbox, 'old_hitbox': self.old_hitbox, 'x_move': self.x_move, 'y_move': self.y_move} for brick in basics.LEVEL.bricks_group if self.hitbox.colliderect(brick.rect) and brick not in [d['brick'] for d in self.collision_info_storage['bricks']]] # loops every collided with ball's hitbox brick and checks whether the brick is already in the storage and if not, then it keeps the necessary info in the variable
            if len(collision_info) > 0:
                self.collision_info_storage['bricks'].extend(collision_info)
            hit_bricks_by_masks = pygame.sprite.spritecollide(self, basics.LEVEL.bricks_group, False, pygame.sprite.collide_mask) # a list of bricks which collided with the ball by mask
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
                #     hit_rect = pygame.Rect(hit_bricks_list[0].rect.topleft, (hit_bricks_list[-1].rect.right - hit_bricks_list[0].rect.left, hit_bricks_list[-1].rect.bottom - hit_bricks_list[0].rect.top))
                # self.detect_brick_side(hit_rect)
        # else:
        #     self.last_collided_bricks.clear()

    def detect_platform_collision(self):
        # if self.hitbox.colliderect(basics.LEVEL.platform_group.sprite.rect) and self.y_move > 0:
        if self.hitbox.colliderect(basics.LEVEL.platform_group.sprite.rect):
            if len(self.collision_info_storage['platform']) == 0:
                self.collision_info_storage['platform'] = {'platform_rect': basics.LEVEL.platform_group.sprite.rect, 'hitbox': self.hitbox, 'old_hitbox': self.old_hitbox, 'x_move': self.x_move, 'y_move': self.y_move} # adds the necessary info of collision to the storage
            if pygame.sprite.spritecollideany(self, basics.LEVEL.platform_group, pygame.sprite.collide_mask):
                basics.BOUNCE_SOUND.stop_play()
                collision_info = self.collision_info_storage['platform']
                platform_rect, hitbox, old_hitbox, x_move, y_move = collision_info['platform_rect'], collision_info['hitbox'], collision_info['old_hitbox'], collision_info['x_move'], collision_info['y_move']
                if x_move > 0 and old_hitbox.right <= platform_rect.left <= hitbox.right:  # check collision between the right side of the ball and the left side of the platform
                    self.x_move = -abs(self.x_move)
                    self.hitbox.right = basics.LEVEL.platform_group.sprite.rect.left
                elif x_move < 0 and hitbox.left <= platform_rect.right <= old_hitbox.left:  # check collision between the left side of the ball and the right side of the platform
                    self.x_move = abs(self.x_move)
                    self.hitbox.left = basics.LEVEL.platform_group.sprite.rect.right
                if y_move > 0 and old_hitbox.bottom <= platform_rect.top <= hitbox.bottom:  # check collision between the bottom side of the ball and the top side of the platform
                    if 'chaotic_ball' not in basics.LEVEL.active_buffs_types:
                        loc = self.hitbox.centerx - basics.LEVEL.platform_group.sprite.rect.centerx # location of the ball center relatively to platform center
                        max_move = 0.9
                        super_max_move = 0.95
                        new_move = (2 * max_move * loc) / basics.LEVEL.platform_group.sprite.rect.width
                        if new_move < -max_move:
                            new_move = -(max_move + ((2 * (super_max_move - max_move) * (basics.LEVEL.platform_group.sprite.rect.left - self.hitbox.centerx)) / self.hitbox.width))
                        elif new_move > max_move:
                            new_move = max_move + ((2 * (super_max_move - max_move) * (self.hitbox.centerx - basics.LEVEL.platform_group.sprite.rect.right)) / self.hitbox.width)
                        self.x_move = new_move
                    else:
                        self.x_move = randint(0, 95) / 100
                    self.y_move = -sqrt(1 - self.x_move ** 2)
                    self.hitbox.bottom = basics.LEVEL.platform_group.sprite.rect.top
                # elif y_move < 0 and hitbox.top <= platform_rect.bottom <= old_hitbox.top:  # check collision between the top side of the ball and the bottom side of the platform
                #     self.y_move = abs(self.y_move)
                #     self.hitbox.top = basics.LEVEL.platform_group.sprite.rect.bottom
                self.collision_info_storage['platform'] = {}

                # if self.hitbox.bottom - basics.LEVEL.platform_group.sprite.rect.top <= 2 * self.vel * basics.Y_COEFFICIENT:
                #     basics.BOUNCE_SOUND.stop_play()
                #
                # elif self.hitbox.bottom - basics.LEVEL.platform_group.sprite.rect.top > 2 * self.vel * basics.Y_COEFFICIENT:
                #     if basics.BOUNCE_SOUND.get_busy() is False:
                #         basics.BOUNCE_SOUND.play()
                #     if self.hitbox.x < basics.LEVEL.platform_group.sprite.rect.x:
                #         self.x_move = -abs(self.x_move)
                #     if self.hitbox.right > basics.LEVEL.platform_group.sprite.rect.right:
                #         self.x_move = abs(self.x_move)

    def detect_border_collision(self):
        if self.rect.top > basics.BOTTOM_BORDER.rect.bottom:
            self.kill()
        elif pygame.sprite.spritecollideany(self, basics.LEVEL.borders_group):
            if self.y_move < 0 and pygame.sprite.collide_mask(self, basics.TOP_BORDER) is not None:
                basics.BOUNCE_SOUND.stop_play()
                self.y_move = abs(self.y_move)
            if self.x_move < 0 and pygame.sprite.collide_mask(self, basics.LEFT_BORDER) is not None:
                basics.BOUNCE_SOUND.stop_play()
                self.x_move = abs(self.x_move)
            if self.x_move > 0 and pygame.sprite.collide_mask(self, basics.RIGHT_BORDER) is not None:
                basics.BOUNCE_SOUND.stop_play()
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


class Shape(pygame.sprite.Sprite):

    def __init__(self, pos, size, surf_name, frame_index=0, anim_speed=0.2):
        super().__init__()
        self.x, self.y = pos
        self.size = size
        self.surf_name = surf_name
        self.frame_index = frame_index
        self.anim_speed = anim_speed
        self.surf_frames = [pygame.transform.scale(pygame.image.load(f'objects/ball_shapes/{self.surf_name}/{index}.png'), self.size).convert_alpha() for index in range(len(listdir(f'objects/ball_shapes/{self.surf_name}/')) - 1)] # creates a list of frames by for-loop, iteration number of which is defined by the number of files in the directory
        self.image = self.surf_frames[self.frame_index]
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        if self.surf_name == 'faceless':
            self.name = 'Faceless'
            self.description = 'A mysterious ball that can take different shapes'
        elif self.surf_name == 'red_ball':
            self.name = 'Red Ball'
            self.description = 'Just a usual red ball. What else do you need?'
        elif self.surf_name == 'pac-man':
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
        if basics.SHAPE_ANIMATION:
            self.frame_index += self.anim_speed
            if self.frame_index >= len(self.surf_frames):
                self.frame_index -= len(self.surf_frames)
            self.image = self.surf_frames[int(self.frame_index)]


class Buff(pygame.sprite.Sprite):

    def __init__(self, brick_holder):
        super().__init__()
        basics.LEVEL.passive_buffs_group.add(self)
        self.state = 'passive'
        self.type = choice(['slow_ball', 'fast_ball', 'slow_platform', 'fast_platform', 'more_balls', 'chaotic_ball', 'x-ray', 'ghost_ball'])
        self.brick_holder = brick_holder
        self.size = 40 * basics.X_COEFFICIENT, 40 * basics.Y_COEFFICIENT
        self.image = pygame.transform.scale(pygame.image.load(f'objects/buffs/{self.type}.png'), self.size).convert_alpha()
        self.rect = self.image.get_rect(center=brick_holder.rect.center)
        self.timer = Timer(7.5, self.cancel_buff)

    def update(self): # detect buff state
        if self.state == 'fall':
            if self.rect.colliderect(basics.LEVEL.platform_group.sprite.rect):
                basics.BUFF_SOUND.stop_play()
                self.state = 'active'
                basics.LEVEL.passive_buffs_group.remove(self)
                basics.LEVEL.active_buffs_group.add(self)
                basics.LEVEL.active_buffs_types.append(self.type)
                self.apply_buff()
            elif self.rect.top > basics.BOTTOM_BORDER.rect.bottom:
                self.kill()
            else:
                self.rect.y += 5 * basics.Y_COEFFICIENT
                basics.WIN.blit(self.image, (self.rect.x, self.rect.y))

    def apply_buff(self):
        if self.type == 'slow_ball':
            for ball in basics.LEVEL.balls_group:
                ball.vel *= 0.75
        elif self.type == 'fast_ball':
            for ball in basics.LEVEL.balls_group:
                ball.vel *= 1.25
        elif self.type == 'slow_platform':
            basics.LEVEL.platform_group.sprite.vel *= 0.75
        elif self.type == 'fast_platform':
            basics.LEVEL.platform_group.sprite.vel *= 1.25
        elif self.type == 'more_balls':
            first_ball = basics.LEVEL.balls_group.sprites()[0]
            basics.LEVEL.balls_group.add(Ball((basics.LEVEL.platform_group.sprite.rect.centerx - (first_ball.init_size[0] / 2), first_ball.y), first_ball.init_size, first_ball.shape, first_ball.vel))
            basics.LEVEL.balls_group.add(Ball((basics.LEVEL.platform_group.sprite.rect.centerx - (first_ball.init_size[0] / 2), first_ball.y), first_ball.init_size, first_ball.shape, first_ball.vel))
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
        basics.LEVEL.active_buffs_types.remove(self.type)
        if self.type == 'slow_ball':
            for ball in basics.LEVEL.balls_group:
                ball.vel *= 1.25
        elif self.type == 'fast_ball':
            for ball in basics.LEVEL.balls_group:
                ball.vel *= 0.75
        elif self.type == 'slow_platform':
            basics.LEVEL.platform_group.sprite.vel *= 1.25
        elif self.type == 'fast_platform':
            basics.LEVEL.platform_group.sprite.vel *= 0.75
        elif self.type == 'ghost_ball':
            for ball in basics.LEVEL.balls_group:
                ball.alpha = 255
                ball.visibility_state = 'disappear'
                ball.image.set_alpha(ball.alpha)
