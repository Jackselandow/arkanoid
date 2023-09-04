# class Button:
#
#     def __init__(self, label, image, selection='glow', arrows_color=None, clickable=True, key=None, feedbacks=None):
#         if label:
#             self.content = label
#         elif image:
#             self.content = image
#         if selection == 'glow':
#             selection_surf = pg.Surface((self.content.rect.size[0] + 16 * constants.X_COEFFICIENT, self.content.rect.size[1] + 16 * constants.Y_COEFFICIENT)).convert()
#             selection_surf.fill('white')
#             selection_surf.set_alpha(120)
#             self.selection_surfs = {selection_surf: selection_surf.get_rect(center=self.content.rect.center)}
#         elif selection == 'arrows':
#             left_arrow = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/selection_arrows/{arrows_color}_left.png'), (self.content.rect.size[1] / 3.6, self.content.rect.size[1] / 2)).convert_alpha()
#             right_arrow = pg.transform.scale(pg.image.load(f'arkanoid/resources/graphics/ui/selection_arrows/{arrows_color}_right.png'), (self.content.rect.size[1] / 3.6, self.content.rect.size[1] / 2)).convert_alpha()
#             self.selection_surfs = {left_arrow: (self.content.rect.left - 8 * constants.X_COEFFICIENT - left_arrow.get_width(), self.content.rect.centery - left_arrow.get_height() / 2), right_arrow: (self.content.rect.right + 8 * constants.X_COEFFICIENT, self.content.rect.centery - right_arrow.get_height() / 2)}
#         self.selection = selection
#         self.mouse_cooldown = False
#         self.key_cooldown = False
#         self.sound_cooldown = False
#         self.clickable = clickable
#         self.key = key
#         self.feedbacks = feedbacks
#
#     def detect_mouse_collision(self):
#         mouse_pos = pg.mouse.get_pos()
#         if self.content.rect.collidepoint(mouse_pos):
#             if self.sound_cooldown is True and self.selection == 'arrows':
#                 self.sound_cooldown = False
#                 constants.SELECTION_SOUND.play()
#             for surf, pos in self.selection_surfs.items():
#                 constants.WIN.blit(surf, pos)
#             return True
#         elif self.sound_cooldown is False:
#             self.sound_cooldown = True
#
#     def detect_press(self):
#         if self.clickable is True:
#             if self.detect_mouse_collision() is True and pg.mouse.get_pressed()[0] and self.mouse_cooldown is True:
#                 self.mouse_cooldown = False
#                 return True
#             if not pg.mouse.get_pressed()[0] and self.mouse_cooldown is False:
#                 self.mouse_cooldown = True
#         if self.key:
#             key_pressed = pg.key.get_pressed()
#             if key_pressed[self.key] and self.key_cooldown is True:
#                 self.key_cooldown = False
#                 return True
#             elif not key_pressed[self.key] and self.key_cooldown is False:
#                 self.key_cooldown = True
#
#     def give_feedback(self):
#         for feedback in self.feedbacks:
#             if type(feedback) == list:
#                 feedback[0](feedback[1])
#             else:
#                 feedback()
#
#     def show(self):
#         self.content.show()
#
#     def all_in_one(self):
#         if self.detect_press() is True:
#             if self.feedbacks:
#                 self.give_feedback()
#             else:
#                 return True
#         self.show()

# def run_preparation():  # my screen width / height = 1.6
#     # display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#     # display_size = display.get_size()
#     win_size = basics.WIN_RECT.size
#     if win_size[0] / win_size[1] <= 1.6:
#         frame_size = (win_size[0], win_size[0] / 1.6)
#         # win = pygame.display.set_mode((display_size[0], display_size[0] / 1.6), pygame.FULLSCREEN)
#         # win = pygame.Surface((display_size[0], display_size[0] / 1.6))
#         # x_coef, y_coef = 1, display_size[1] / win.get_height()
#     else:
#         frame_size = (win_size[1] * 1.6, win_size[1])
#         # win = pygame.display.set_mode((display_size[1] * 1.6, display_size[1]), pygame.FULLSCREEN)
#         # win = pygame.Surface((display_size[1] * 1.6, display_size[1]))
#         # x_coef, y_coef = , 1
#     # win_rect = win.get_rect(center=basics.DISPLAY.get_rect().center)
#     frame_pos = ((win_size[0] - frame_size[0]) / 2, (win_size[1] - frame_size[1]) / 2)
#     return frame_size, frame_pos


# def run_loading():
#     import pygame
#     pygame.init()
#     loading_list = [pygame.transform.scale(pygame.image.load(f'objects/loading/{i}.png'), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT)) for i in range(1, 17)]
#     while True: #(can be also index of frame counted, so when index is 18, overwrite this variable's value to 1)
#         for frame in loading_list:
#             basics.CLOCK.tick(10)
#             basics.WIN.blit(basics.WHITE_SCREEN, (0, 0))
#             basics.WIN.blit(frame, (1000 * basics.X_COEFFICIENT, 450 * basics.Y_COEFFICIENT))
#             pygame.display.update()

# mts = 0.9 # a maximum trajectory shift of the ball when hitting the platform
# shift = (2 * mts * loc) / basics.LEVEL.platform.rect.width
# self.x_move += shift
# if self.x_move < -0.9:
#     self.x_move = -0.9
# elif self.x_move > 0.9:
#     self.x_move = 0.9

# if self.x_move > 0:
#     delta_x = self.rect.right - brick_rect.left
# else:
#     delta_x = brick_rect.right - self.rect.left
# if self.y_move > 0:
#     delta_y = self.rect.bottom - brick_rect.top
# else:
#     delta_y = brick_rect.bottom - self.rect.top
#
# if delta_x - delta_y == 0:
#     self.x_move, self.y_move = -self.x_move, -self.y_move
# elif delta_x > delta_y:
#     self.y_move = -self.y_move
# elif delta_y > delta_x:
#     self.x_move = -self.x_move


# try:
#     self.image = pygame.transform.scale(pygame.image.load(f'objects/ball_shapes/{self.surf_name}/{int(self.frame_index + 0.2)}.png'), self.init_size)
# except FileNotFoundError:
#     self.frame_index = 0
# else:
#     self.frame_index += 0.2
# finally:
#     self.image = pygame.transform.scale(pygame.image.load(f'objects/ball_shapes/{self.surf_name}/{int(self.frame_index)}.png'), self.init_size)

# def detect_platform_collision(self):
#     if self.rect.colliderect(basics.LEVEL.platform.rect) and self.y_move > 0:
#         if self.rect.bottom - basics.LEVEL.platform.rect.top <= 2 * self.vel * basics.Y_COEFFICIENT:
#             basics.BOUNCE_SOUND.stop_play()
#             if 'chaotic_ball' not in basics.LEVEL.active_buffs_types:
#                 if self.rect.centerx == basics.LEVEL.platform.rect.centerx:  # 1
#                     self.x_move, self.y_move = 0, -2
#                 elif basics.LEVEL.platform.rect.left + basics.LEVEL.platform.size[
#                     0] / 4 < self.rect.left and self.rect.centerx < basics.LEVEL.platform.rect.centerx:  # 2
#                     self.x_move, self.y_move = -0.5, -1.5
#                 elif basics.LEVEL.platform.rect.centerx < self.rect.centerx and self.rect.right < basics.LEVEL.platform.rect.right - \
#                         basics.LEVEL.platform.size[0] / 4:  # 3
#                     self.x_move, self.y_move = 0.5, -1.5
#                 elif basics.LEVEL.platform.rect.left <= self.rect.left and self.rect.centerx <= basics.LEVEL.platform.rect.centerx:  # 4
#                     self.x_move, self.y_move = -1, -1
#                 elif basics.LEVEL.platform.rect.centerx <= self.rect.centerx and self.rect.right <= basics.LEVEL.platform.rect.right:  # 5
#                     self.x_move, self.y_move = 1, -1
#                 elif self.rect.left < basics.LEVEL.platform.rect.left:  # 6
#                     self.x_move, self.y_move = -1.5, -0.5
#                 elif self.rect.right > basics.LEVEL.platform.rect.right:  # 7
#                     self.x_move, self.y_move = 1.5, -0.5
#             else:
#                 self.x_move = choice([0, -0.5, 0.5, -1, 1, -1.5, 1.5])
#                 self.y_move = choice([-0.5, -1, -1.5])
#         elif self.rect.bottom - basics.LEVEL.platform.rect.top > 2 * self.vel * basics.Y_COEFFICIENT:
#             if basics.BOUNCE_SOUND.get_busy() is False:
#                 basics.BOUNCE_SOUND.play()
#             if self.rect.x < basics.LEVEL.platform.rect.x:
#                 self.x_move = -abs(self.x_move)
#             if self.rect.right > basics.LEVEL.platform.rect.right:
#                 self.x_move = abs(self.x_move)




# def detect_collision(self):
#     # collision with bricks
#     hit_index_list = []
#     for brick in basics.LEVEL.bricks:
#         if self.rect.colliderect(brick.rect) and brick not in self.last_collided_bricks:
#             hit_index_list.append(basics.LEVEL.bricks.index(brick))
#             self.last_collided_bricks = []
#             self.last_collided_bricks.append(brick)
#             if brick.color != 'gray' and brick.armor == 0:
#                 for buff in basics.LEVEL.passive_buffs:
#                     if buff.brick_holder == brick and buff.state == 'passive':
#                         buff.state = 'fall'
#     if len(hit_index_list) > 0:     # executes if there was a collision with brick
#         hit_rects_list = []
#         gray_bricks_number = 0
#         for hit_index in hit_index_list:
#             hit_rect0 = basics.LEVEL.bricks[hit_index - hit_index_list.index(hit_index) + gray_bricks_number]
#             if hit_rect0.color != 'gray':
#                 hit_rect0.handle_armor()
#             else:
#                 gray_bricks_number += 1
#                 basics.BOUNCE_SOUND.stop()
#                 basics.BOUNCE_SOUND.play()
#             hit_rects_list.append(hit_rect0)
#         if len(hit_rects_list) > 1:     # executes if there was a collision with many bricks
#             self.detect_extra_brick(hit_rects_list)
#             ball_move = []
#             right_x_move, right_y_move = self.x_move, self.y_move
#             similar_x, similar_y = self.detect_similar_coordinates(hit_rects_list)
#             for hit_rect in hit_rects_list:
#                 x_move0, y_move0 = self.detect_brick_side(self.x_move, self.y_move, hit_rect)
#                 ball_move.append((x_move0, y_move0))
#             for move in ball_move:
#                 if move[0] != self.x_move and similar_y is False:
#                     right_x_move = move[0]
#                 if move[1] != self.y_move and similar_x is False:
#                     right_y_move = move[1]
#             self.x_move, self.y_move = right_x_move, right_y_move
#         else:   # executes if there was a collision with one brick
#             self.x_move, self.y_move = self.detect_brick_side(self.x_move, self.y_move, hit_rects_list[0])
#     else:   # executes if there wasn't any collision with bricks
#         self.last_collided_bricks = []
#
#     # collision with platform
#     if self.rect.colliderect(basics.LEVEL.platform.rect) and self.y_move > 0:
#         if self.rect.bottom - basics.LEVEL.platform.rect.top <= 2 * self.vel * basics.Y_COEFFICIENT:
#             basics.BOUNCE_SOUND.stop()
#             basics.BOUNCE_SOUND.play()
#             if 'chaotic_ball' not in basics.LEVEL.active_buffs_types:
#                 if self.rect.centerx == basics.LEVEL.platform.rect.centerx:  # 1
#                     self.x_move, self.y_move = 0, -2
#                 elif basics.LEVEL.platform.rect.left + basics.LEVEL.platform.size[0] / 4 < self.rect.left and self.rect.centerx < basics.LEVEL.platform.rect.centerx:  # 2
#                     self.x_move, self.y_move = -0.5, -1.5
#                 elif basics.LEVEL.platform.rect.centerx < self.rect.centerx and self.rect.right < basics.LEVEL.platform.rect.right - basics.LEVEL.platform.size[0] / 4:    # 3
#                     self.x_move, self.y_move = 0.5, -1.5
#                 elif basics.LEVEL.platform.rect.left <= self.rect.left and self.rect.centerx <= basics.LEVEL.platform.rect.centerx:   # 4
#                     self.x_move, self.y_move = -1, -1
#                 elif basics.LEVEL.platform.rect.centerx <= self.rect.centerx and self.rect.right <= basics.LEVEL.platform.rect.right:   # 5
#                     self.x_move, self.y_move = 1, -1
#                 elif self.rect.left < basics.LEVEL.platform.rect.left:   # 6
#                     self.x_move, self.y_move = -1.5, -0.5
#                 elif self.rect.right > basics.LEVEL.platform.rect.right:   # 7
#                     self.x_move, self.y_move = 1.5, -0.5
#             else:
#                 self.x_move = choice([0, -0.5, 0.5, -1, 1, -1.5, 1.5])
#                 self.y_move = choice([-0.5, -1, -1.5])
#                 self.y_move = -(2 - abs(self.x_move))
#         elif self.rect.bottom - basics.LEVEL.platform.rect.top > 2 * self.vel * basics.Y_COEFFICIENT:
#             if basics.BOUNCE_SOUND.get_busy() is False:
#                 basics.BOUNCE_SOUND.play()
#             if self.rect.x < basics.LEVEL.platform.rect.x:
#                 self.x_move = -abs(self.x_move)
#             if self.rect.right > basics.LEVEL.platform.rect.right:
#                 self.x_move = abs(self.x_move)
#
#     # collision with borders
#     if self.rect.colliderect(basics.TOP_BORDER) and self.y_move < 0:
#         basics.BOUNCE_SOUND.stop()
#         basics.BOUNCE_SOUND.play()
#         self.y_move = -self.y_move
#     if self.rect.colliderect(basics.LEFT_BORDER) or self.rect.colliderect(basics.RIGHT_BORDER):
#         basics.BOUNCE_SOUND.stop()
#         basics.BOUNCE_SOUND.play()
#         self.x_move = -self.x_move
#     if self.rect.y > basics.BOTTOM_BORDER.bottom:
#         basics.LEVEL.balls.remove(self)
#
# def detect_brick_side(self, x_move, y_move, brick):
#     if x_move > 0:
#         delta_x = self.rect.right - brick.rect.left
#     else:
#         delta_x = brick.rect.right - self.rect.left
#     if y_move > 0:
#         delta_y = self.rect.bottom - brick.rect.top
#     else:
#         delta_y = brick.rect.bottom - self.rect.top
#
#     if delta_x - delta_y == 0:
#         x_move, y_move = -x_move, -y_move
#     elif delta_x > delta_y:
#         y_move = -y_move
#     elif delta_y > delta_x:
#         x_move = -x_move
#     return x_move, y_move
#
# @staticmethod
# def detect_extra_brick(hit_rects_list):
#     extra_bricks = []
#     for hit_rect in hit_rects_list:
#         has_similar_x, has_similar_y = False, False
#         for check_rect in hit_rects_list:
#             if hit_rects_list.index(hit_rect) != hit_rects_list.index(check_rect):
#                 if hit_rect.x == check_rect.x:
#                     has_similar_x = True
#                 if hit_rect.y == check_rect.y:
#                     has_similar_y = True
#         if has_similar_x is True and has_similar_y is True:
#             extra_bricks.append(hit_rect)
#     for extra in extra_bricks:
#         if extra.color != 'gray':
#             basics.LEVEL.bricks.append(extra)
#         hit_rects_list.remove(extra)
#
# @staticmethod
# def detect_similar_coordinates(hit_rects_list):
#     similar_x, similar_y = False, False
#     for hit_rect in hit_rects_list:
#         for check_rect in hit_rects_list:
#             if hit_rects_list.index(hit_rect) != hit_rects_list.index(check_rect):
#                 if similar_x is False:
#                     if hit_rect.x == check_rect.x:
#                         similar_x = True
#                 if similar_y is False:
#                     if hit_rect.y == check_rect.y:
#                         similar_y = True
#     return similar_x, similar_y

