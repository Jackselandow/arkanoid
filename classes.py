import pygame
import basics
from main import WIN
pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 125, 125, 125
GREEN = 0, 255, 0
PURPLE = 255, 0, 255
YELLOW = 255, 255, 0
RED = 255, 0, 0


class Music:

    def __init__(self, filename, volume):
        self.name = pygame.mixer.Sound(filename)
        self.volume = volume

    def play(self, loops):
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

    def play(self, loops):
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
            WIN.blit(self.text, (self.x, self.y))
        else:
            WIN.blit(self.surface, (self.x, self.y))

    def detect_mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            WIN.blit(self.button_glow, (self.x - 8 * basics.X_COEFFICIENT, self.y - 8 * basics.Y_COEFFICIENT))

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
        WIN.blit(self.image, (self.rect.x, self.rect.y))

    def detect_mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            WIN.blit(self.button_glow, (self.x - 8 * basics.X_COEFFICIENT, self.y - 8 * basics.Y_COEFFICIENT))

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


class Platform:

    def __init__(self, pos, size, surf, vel):
        self.x, self.y = pos
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(surf), size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.vel = vel

    def show(self):
        WIN.blit(self.surface, (self.rect.x, self.rect.y))

    def movement(self):
        # left_center = self.rect.centerx - self.rect.left
        # right_center = self.rect.right - self.rect.centerx
        # mouse_pos = pygame.mouse.get_pos()
        # if not self.rect.colliderect(basics.LEFT_BORDER) and not self.rect.colliderect(basics.RIGHT_BORDER):
        #     self.rect.centerx = mouse_pos[0]
        # elif left_center < mouse_pos[0] < basics.RIGHT_BORDER.x - right_center:
        #     self.rect.centerx = mouse_pos[0]
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] and not self.rect.colliderect(basics.LEFT_BORDER)\
                or key_pressed[pygame.K_a] and not self.rect.colliderect(basics.LEFT_BORDER):
            self.x -= self.vel
            self.rect.x -= self.vel
        if key_pressed[pygame.K_RIGHT] and not self.rect.colliderect(basics.RIGHT_BORDER)\
                or key_pressed[pygame.K_d] and not self.rect.colliderect(basics.RIGHT_BORDER):
            self.x += self.vel
            self.rect.x += self.vel


class Ball:

    def __init__(self, pos, size, surf, vel, x_move, y_move):
        self.x, self.y = pos
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(surf), size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.vel = vel
        self.x_move, self.y_move = x_move, y_move

    def show(self):
        WIN.blit(self.surface, (self.rect.x, self.rect.y))

    def detect_brick_side(self, x_move, y_move, brick):
        if x_move > 0:
            delta_x = self.rect.right - brick.rect.left
        else:
            delta_x = brick.rect.right - self.rect.left
        if y_move > 0:
            delta_y = self.rect.bottom - brick.rect.top
        else:
            delta_y = brick.rect.bottom - self.rect.top

        if abs(delta_x - delta_y) < self.vel:
            x_move, y_move = -x_move, -y_move
        elif delta_x > delta_y:
            y_move = -y_move
        elif delta_y > delta_x:
            x_move = -x_move
        return x_move, y_move

    @staticmethod
    def detect_extra_brick(hit_rects_list, bricks):
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
                bricks.append(extra)
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

    def collision(self, bricks, platform):
        # collision with bricks
        hit_index_list = []
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                hit_index_list.append(bricks.index(brick))
        if len(hit_index_list) > 0:     # executes if there was a collision with brick
            hit_rects_list = []
            grey_bricks_number = 0
            for hit_index in hit_index_list:
                hit_rect0 = bricks[hit_index - hit_index_list.index(hit_index) + grey_bricks_number]
                if hit_rect0.color != 'grey':
                    basics.EXPLOSION_SOUND.play(0)
                    bricks.remove(hit_rect0)
                else:
                    grey_bricks_number += 1
                    basics.BOUNCE_SOUND.play(0)
                hit_rects_list.append(hit_rect0)
            if len(hit_rects_list) > 1:     # executes if there was a collision with many bricks
                self.detect_extra_brick(hit_rects_list, bricks)
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

        # collision with platform
        if self.rect.colliderect(platform.rect) and self.rect.bottom - platform.rect.top <= self.vel:
            basics.BOUNCE_SOUND.play(0)
            if self.rect.collidepoint(platform.rect.topleft):
                self.x_move = -1
            if self.rect.collidepoint(platform.rect.topright):
                self.x_move = 1
            self.y_move *= -1
        elif self.rect.colliderect(platform.rect) and self.rect.bottom - platform.rect.top > self.vel:
            basics.BOUNCE_SOUND.play(0)
            if self.rect.collidepoint(platform.rect.bottomleft):
                self.x_move = -1
            if self.rect.collidepoint(platform.rect.bottomright):
                self.x_move = 1

        # collision with borders
        if self.rect.colliderect(basics.TOP_BORDER) and self.y_move == -1:
            basics.BOUNCE_SOUND.play(0)
            self.y_move = 1
        if self.rect.colliderect(basics.LEFT_BORDER) or self.rect.colliderect(basics.RIGHT_BORDER):
            basics.BOUNCE_SOUND.play(0)
            self.x_move *= -1
        if self.rect.colliderect(basics.BOTTOM_BORDER):
            from main import run_lose
            run_lose()

    def movement(self, bricks, platform):
        self.collision(bricks, platform)

        self.rect.x += self.vel * self.x_move
        self.rect.y += self.vel * self.y_move


class Brick:

    def __init__(self, pos, size, color):
        self.x, self.y = pos
        self.size = size
        self.color = color
        if self.color == 'green':
            self.surface = pygame.transform.scale(pygame.image.load('objects/green_brick.png'), size)
        if self.color == 'purple':
            self.surface = pygame.transform.scale(pygame.image.load('objects/purple_brick.png'), size)
        if self.color == 'yellow':
            self.surface = pygame.transform.scale(pygame.image.load('objects/yellow_brick.png'), size)
        if self.color == 'red':
            self.surface = pygame.transform.scale(pygame.image.load('objects/red_brick.png'), size)
        if self.color == 'grey':
            self.surface = pygame.transform.scale(pygame.image.load('objects/grey_brick.png'), size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        WIN.blit(self.surface, (self.rect.x, self.rect.y))
