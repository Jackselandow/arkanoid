import pygame
import basics
from random import choice
from threading import Timer
pygame.init()


class Music:

    def __init__(self, filename, volume):
        self.name = pygame.mixer.Sound(filename)
        self.volume = volume

    def play(self, loops=0):
        self.update()
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

    def play(self, loops=0):
        self.update()
        self.name.play(loops)

    def stop(self):
        self.name.stop()

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


class TextButton:

    def __init__(self, text, pos, size, font, fg, bg, feedbacks):
        self.x, self.y = pos
        self.font = pygame.font.Font(font, int(size))
        self.text = self.font.render(text, False, fg)
        self.size = self.text.get_size()
        self.bg = bg
        self.surface = pygame.Surface(self.size)
        if self.bg != 'none':
            self.surface.fill(bg)
        if font != 'fonts/pixeboy_font.ttf':
            self.surface.blit(self.text, (3 * basics.FONT_COEFFICIENT, 0))
        else:
            self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.button_glow = pygame.Surface((self.size[0] + 16 * basics.X_COEFFICIENT, self.size[1] + 16 * basics.Y_COEFFICIENT))
        self.button_glow.fill(basics.WHITE)
        self.button_glow.set_alpha(120)
        self.feedbacks = feedbacks

    def show(self):
        if self.bg == 'none':
            basics.WIN.blit(self.text, (self.x, self.y))
        else:
            basics.WIN.blit(self.surface, (self.x, self.y))

    def detect_mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            basics.WIN.blit(self.button_glow, (self.x - 8 * basics.X_COEFFICIENT, self.y - 8 * basics.Y_COEFFICIENT))

    def detect_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            return self.clicked()

    def clicked(self):
        for feedback in self.feedbacks:
            if type(feedback) == list:
                feedback[0](feedback[1])
            elif feedback != 'none':
                if feedback == 'LAST_RUN':
                    feedback = basics.LAST_RUN
                elif feedback == 'PRELAST_RUN':
                    feedback = basics.PRELAST_RUN
                feedback()
            else:
                return True


class ImageButton:

    def __init__(self, image, pos, size, feedbacks):
        self.x, self.y = pos
        self.image = pygame.transform.scale(pygame.image.load(image), size)
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.button_glow = pygame.Surface((self.size[0] + 16 * basics.X_COEFFICIENT, self.size[1] + 16 * basics.Y_COEFFICIENT))
        self.button_glow.fill(basics.WHITE)
        self.button_glow.set_alpha(120)
        self.feedbacks = feedbacks

    def show(self):
        basics.WIN.blit(self.image, (self.rect.x, self.rect.y))

    def detect_mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            basics.WIN.blit(self.button_glow, (self.x - 8 * basics.X_COEFFICIENT, self.y - 8 * basics.Y_COEFFICIENT))

    def detect_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            return self.clicked()

    def clicked(self):
        for feedback in self.feedbacks:
            if type(feedback) == list:
                feedback[0](feedback[1])
            elif feedback != 'none':
                if feedback == 'LAST_RUN':
                    feedback = basics.LAST_RUN
                elif feedback == 'PRELAST_RUN':
                    feedback = basics.PRELAST_RUN
                feedback()
            else:
                return True


class LevelControl:

    def __init__(self):
        self.level_started = False
        self.countdown_state = False
        self.countdown_index = 0
        self.press_space_state = 'appear'
        self.press_space_alpha = 0
        self.platform = None
        self.balls = []
        self.bricks = []
        self.passive_buffs = []
        self.active_buffs = []
        self.active_buffs_types = []


class Platform:

    def __init__(self, pos, size, surf, vel):
        self.x, self.y = pos
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(surf), size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.vel = vel

    def show(self):
        basics.WIN.blit(self.surface, (self.rect.x, self.rect.y))

    def movement(self):
        if basics.CONTROL_TYPE == 'keyboard':
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT] and not self.rect.colliderect(basics.LEFT_BORDER) \
                    or key_pressed[pygame.K_a] and not self.rect.colliderect(basics.LEFT_BORDER):
                self.rect.x -= self.vel * basics.X_COEFFICIENT
            if key_pressed[pygame.K_RIGHT] and not self.rect.colliderect(basics.RIGHT_BORDER) \
                    or key_pressed[pygame.K_d] and not self.rect.colliderect(basics.RIGHT_BORDER):
                self.rect.x += self.vel * basics.X_COEFFICIENT
        elif basics.CONTROL_TYPE == 'mouse':
            mouse_pos = pygame.mouse.get_pos()
            left_center = self.rect.centerx - self.rect.left
            right_center = self.rect.right - self.rect.centerx
            if not self.rect.colliderect(basics.LEFT_BORDER) and not self.rect.colliderect(basics.RIGHT_BORDER):
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


class Ball:

    def __init__(self, pos, size, surf, vel, x_move=choice([1, -1]), y_move=-1):
        self.x, self.y = pos
        self.size = size
        self.surf = surf
        if surf == 'faceless':
            surf = choice(basics.AVAILABLE_SHAPES.split(',')[1:])
        self.surface = pygame.transform.scale(pygame.image.load(f'objects/ball_shapes/{surf}.png'), size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.vel = vel
        self.alpha = 255
        self.visibility_state = 'disappear'
        self.x_move, self.y_move = x_move, y_move
        self.last_collided_bricks = []

    def show(self):
        basics.WIN.blit(self.surface, (self.rect.x, self.rect.y))

    def detect_brick_side(self, x_move, y_move, brick):
        if x_move > 0:
            delta_x = self.rect.right - brick.rect.left
        else:
            delta_x = brick.rect.right - self.rect.left
        if y_move > 0:
            delta_y = self.rect.bottom - brick.rect.top
        else:
            delta_y = brick.rect.bottom - self.rect.top

        if delta_x - delta_y == 0:
            x_move, y_move = -x_move, -y_move
        elif delta_x > delta_y:
            y_move = -y_move
        elif delta_y > delta_x:
            x_move = -x_move
        return x_move, y_move

    @staticmethod
    def detect_extra_brick(hit_rects_list):
        extra_bricks = []
        for hit_rect in hit_rects_list:
            has_similar_x, has_similar_y = False, False
            for check_rect in hit_rects_list:
                if hit_rects_list.index(hit_rect) != hit_rects_list.index(check_rect):
                    if hit_rect.x == check_rect.x:
                        has_similar_x = True
                    if hit_rect.y == check_rect.y:
                        has_similar_y = True
            if has_similar_x is True and has_similar_y is True:
                extra_bricks.append(hit_rect)
        for extra in extra_bricks:
            if extra.color != 'grey':
                basics.LEVEL.bricks.append(extra)
            hit_rects_list.remove(extra)

    @staticmethod
    def detect_similar_coordinates(hit_rects_list):
        similar_x, similar_y = False, False
        for hit_rect in hit_rects_list:
            for check_rect in hit_rects_list:
                if hit_rects_list.index(hit_rect) != hit_rects_list.index(check_rect):
                    if similar_x is False:
                        if hit_rect.x == check_rect.x:
                            similar_x = True
                    if similar_y is False:
                        if hit_rect.y == check_rect.y:
                            similar_y = True
        return similar_x, similar_y

    def collision(self):
        # collision with bricks
        hit_index_list = []
        for brick in basics.LEVEL.bricks:
            if self.rect.colliderect(brick.rect) and brick not in self.last_collided_bricks:
                hit_index_list.append(basics.LEVEL.bricks.index(brick))
                self.last_collided_bricks = []
                self.last_collided_bricks.append(brick)
                if brick.color != 'grey':
                    for buff in basics.LEVEL.passive_buffs:
                        if buff.brick_holder == brick and buff.state == 'passive':
                            buff.state = 'fall'
        if len(hit_index_list) > 0:     # executes if there was a collision with brick
            hit_rects_list = []
            grey_bricks_number = 0
            for hit_index in hit_index_list:
                hit_rect0 = basics.LEVEL.bricks[hit_index - hit_index_list.index(hit_index) + grey_bricks_number]
                if hit_rect0.color != 'grey':
                    basics.EXPLOSION_SOUND.play()
                    basics.LEVEL.bricks.remove(hit_rect0)
                else:
                    grey_bricks_number += 1
                    basics.BOUNCE_SOUND.stop()
                    basics.BOUNCE_SOUND.play()
                hit_rects_list.append(hit_rect0)
            if len(hit_rects_list) > 1:     # executes if there was a collision with many bricks
                self.detect_extra_brick(hit_rects_list)
                ball_move = []
                right_x_move, right_y_move = self.x_move, self.y_move
                similar_x, similar_y = self.detect_similar_coordinates(hit_rects_list)
                for hit_rect in hit_rects_list:
                    x_move0, y_move0 = self.detect_brick_side(self.x_move, self.y_move, hit_rect)
                    ball_move.append((x_move0, y_move0))
                for move in ball_move:
                    if move[0] != self.x_move and similar_y is False:
                        right_x_move = move[0]
                    if move[1] != self.y_move and similar_x is False:
                        right_y_move = move[1]
                self.x_move, self.y_move = right_x_move, right_y_move
            else:   # executes if there was a collision with one brick
                self.x_move, self.y_move = self.detect_brick_side(self.x_move, self.y_move, hit_rects_list[0])
        else:   # executes if there wasn't any collision with bricks
            self.last_collided_bricks = []

        # collision with platform
        if self.rect.colliderect(basics.LEVEL.platform.rect) and self.y_move > 0:
            if self.rect.bottom - basics.LEVEL.platform.rect.top <= 2 * self.vel * basics.Y_COEFFICIENT:
                basics.BOUNCE_SOUND.stop()
                basics.BOUNCE_SOUND.play()
                if 'chaotic_ball' not in basics.LEVEL.active_buffs_types:
                    if self.rect.centerx == basics.LEVEL.platform.rect.centerx:  # 1
                        self.x_move, self.y_move = 0, -2
                    elif basics.LEVEL.platform.rect.left + basics.LEVEL.platform.size[0] / 4 < self.rect.left and self.rect.centerx < basics.LEVEL.platform.rect.centerx:  # 2
                        self.x_move, self.y_move = -0.5, -1.5
                    elif basics.LEVEL.platform.rect.centerx < self.rect.centerx and self.rect.right < basics.LEVEL.platform.rect.right - basics.LEVEL.platform.size[0] / 4:    # 3
                        self.x_move, self.y_move = 0.5, -1.5
                    elif basics.LEVEL.platform.rect.left <= self.rect.left and self.rect.centerx <= basics.LEVEL.platform.rect.centerx:   # 4
                        self.x_move, self.y_move = -1, -1
                    elif basics.LEVEL.platform.rect.centerx <= self.rect.centerx and self.rect.right <= basics.LEVEL.platform.rect.right:   # 5
                        self.x_move, self.y_move = 1, -1
                    elif self.rect.left < basics.LEVEL.platform.rect.left:   # 6
                        self.x_move, self.y_move = -1.5, -0.5
                    elif self.rect.right > basics.LEVEL.platform.rect.right:   # 7
                        self.x_move, self.y_move = 1.5, -0.5
                else:
                    self.x_move = choice([0, -0.5, 0.5, -1, 1, -1.5, 1.5])
                    self.y_move = -(2 - abs(self.x_move))
            elif self.rect.bottom - basics.LEVEL.platform.rect.top > 2 * self.vel * basics.Y_COEFFICIENT:
                if basics.BOUNCE_SOUND.get_busy() is False:
                    basics.BOUNCE_SOUND.play()
                if self.rect.x < basics.LEVEL.platform.rect.x:
                    self.x_move = -abs(self.x_move)
                if self.rect.right > basics.LEVEL.platform.rect.right:
                    self.x_move = abs(self.x_move)

        # collision with borders
        if self.rect.colliderect(basics.TOP_BORDER) and self.y_move < 0:
            basics.BOUNCE_SOUND.stop()
            basics.BOUNCE_SOUND.play()
            self.y_move = -self.y_move
        if self.rect.colliderect(basics.LEFT_BORDER) or self.rect.colliderect(basics.RIGHT_BORDER):
            basics.BOUNCE_SOUND.stop()
            basics.BOUNCE_SOUND.play()
            self.x_move = -self.x_move
        if self.rect.y > basics.BOTTOM_BORDER.bottom:
            basics.LEVEL.balls.remove(self)

    def movement(self):
        self.collision()
        self.rect.x += self.vel * self.x_move * basics.X_COEFFICIENT
        self.rect.y += self.vel * self.y_move * basics.Y_COEFFICIENT


class Brick:

    def __init__(self, pos, size, color):
        basics.LEVEL.bricks.append(self)
        self.x, self.y = pos
        self.size = size
        self.color = color
        self.surface = pygame.Surface(self.size)
        self.surface.fill(basics.BLACK)
        self.surface.blit(pygame.transform.scale(pygame.image.load(f'objects/bricks/{self.color}.png'), (size[0] - 10 * basics.X_COEFFICIENT, size[1] - 10 * basics.Y_COEFFICIENT)), (5 * basics.X_COEFFICIENT, 5 * basics.Y_COEFFICIENT))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.content = choice([None, None, None, 'buff'])
        if self.content == 'buff':
            Buff(self)

    def show(self):
        basics.WIN.blit(self.surface, (self.rect.x, self.rect.y))


class Shape:

    def __init__(self, pos, size, surf):
        self.x, self.y = pos
        self.size = size
        self.surf_name = surf
        self.surface = pygame.transform.scale(pygame.image.load(f'objects/ball_shapes/{self.surf_name}.png'), size)
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

    def show(self):
        basics.WIN.blit(self.surface, (self.rect.x, self.rect.y))


class Buff:

    def __init__(self, brick_holder):
        basics.LEVEL.passive_buffs.append(self)
        self.state = 'passive'
        self.type = choice(['slow_ball', 'fast_ball', 'slow_platform', 'fast_platform', 'more_balls', 'chaotic_ball', 'x-ray', 'ghost_ball'])
        self.brick_holder = brick_holder
        self.size = 40 * basics.X_COEFFICIENT, 40 * basics.Y_COEFFICIENT
        self.x, self.y = brick_holder.rect.centerx - (self.size[0] / 2), brick_holder.y
        self.surface = pygame.transform.scale(pygame.image.load(f'objects/buffs/{self.type}.png'), self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.timer = Timer(7.5, self.cancel_buff)

    def detect_state(self):
        if self.state == 'fall':
            if self.rect.colliderect(basics.LEVEL.platform.rect):
                basics.BUFF_SOUND.stop()
                basics.BUFF_SOUND.play()
                self.state = 'active'
                basics.LEVEL.passive_buffs.remove(self)
                basics.LEVEL.active_buffs.append(self)
                basics.LEVEL.active_buffs_types.append(self.type)
                self.apply_buff()
            elif self.rect.top > basics.BOTTOM_BORDER.bottom:
                basics.LEVEL.passive_buffs.remove(self)
            else:
                self.rect.y += 5 * basics.Y_COEFFICIENT
                self.show()

    def apply_buff(self):
        if self.type == 'slow_ball':
            for ball in basics.LEVEL.balls:
                ball.vel *= 0.75
        elif self.type == 'fast_ball':
            for ball in basics.LEVEL.balls:
                ball.vel *= 1.25
        elif self.type == 'slow_platform':
            basics.LEVEL.platform.vel *= 0.75
        elif self.type == 'fast_platform':
            basics.LEVEL.platform.vel *= 1.25
        elif self.type == 'more_balls':
            first_ball = basics.LEVEL.balls[0]
            basics.LEVEL.balls.append(basics.Ball((basics.LEVEL.platform.rect.centerx - (first_ball.size[0] / 2), first_ball.y), first_ball.size, first_ball.surf, first_ball.vel, -1))
            basics.LEVEL.balls.append(basics.Ball((basics.LEVEL.platform.rect.centerx - (first_ball.size[0] / 2), first_ball.y), first_ball.size, first_ball.surf, first_ball.vel, 1))
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
        basics.LEVEL.active_buffs.remove(self)
        basics.LEVEL.active_buffs_types.remove(self.type)
        if self.type == 'slow_ball':
            for ball in basics.LEVEL.balls:
                ball.vel *= 1.25
        elif self.type == 'fast_ball':
            for ball in basics.LEVEL.balls:
                ball.vel *= 0.75
        elif self.type == 'slow_platform':
            basics.LEVEL.platform.vel *= 1.25
        elif self.type == 'fast_platform':
            basics.LEVEL.platform.vel *= 0.75
        elif self.type == 'ghost_ball':
            for ball in basics.LEVEL.balls:
                ball.alpha = 255
                ball.visibility_state = 'disappear'
                ball.surface.set_alpha(ball.alpha)

    def show(self):
        basics.WIN.blit(self.surface, (self.rect.x, self.rect.y))


def handle_buffs():
    for buff in basics.LEVEL.passive_buffs:
        buff.detect_state()
    if 'x-ray' in basics.LEVEL.active_buffs_types:
        for buff in basics.LEVEL.passive_buffs:
            buff.show()
    if 'ghost_ball' in basics.LEVEL.active_buffs_types:
        for ball in basics.LEVEL.balls:
            if ball.alpha == -100:
                ball.visibility_state = 'appear'
            elif ball.alpha == 255:
                ball.visibility_state = 'disappear'
            if ball.visibility_state == 'appear':
                ball.alpha += 5
                ball.surface.set_alpha(ball.alpha)
            elif ball.visibility_state == 'disappear':
                ball.alpha -= 5
                ball.surface.set_alpha(ball.alpha)
