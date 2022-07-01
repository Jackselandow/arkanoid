import pygame
import basics
from main import WIN
from classes import Music, Platform, Ball, Brick
pygame.init()

music = Music('sounds/lvl1_music.mp3', 1)
basics.MUSICS.append(music)


def run_lvl():
    music.update()
    run = True

    level1_text = basics.RETROBLAZE_FONT.render('l e v e l 1', False, basics.GREEN)
    level1_rect = level1_text.get_rect(center=(basics.WIN_RECT.right / 2, basics.upper_menu.bottom / 2))

    while run:
        key_pressed = pygame.key.get_pressed()
        bricks_left_text = basics.PIXEBOY_FONT.render(('BRICKS LEFT: ' + str(len(bricks))), False, basics.WHITE)
        bricks_left_rect = bricks_left_text.get_rect(bottomright=(basics.WIN_RECT.right - 8 * basics.X_COEFFICIENT, basics.upper_menu.bottom - 8 * basics.Y_COEFFICIENT))
        basics.CLOCK.tick(basics.FPS)
        for event in pygame.event.get():
            basics.pause_button.detect_click(event)
            if event.type == pygame.QUIT:
                run = False
        if key_pressed[pygame.K_ESCAPE]:
            basics.pause_button.clicked()

        if len(bricks) == 0:
            from main import run_win
            run_win('level 1')
        WIN.blit(bg, (0, basics.upper_menu.bottom))
        WIN.fill(basics.BLACK, basics.upper_menu)
        WIN.blit(level1_text, level1_rect)
        WIN.blit(bricks_left_text, bricks_left_rect)
        platform.movement()
        ball.movement(bricks, platform)
        platform.show()
        basics.pause_button.detect_mouse_collision()
        basics.pause_button.show()
        ball.show()
        for brick in bricks:
            brick.show()
        pygame.display.update()

    pygame.quit()


def lvl1_main():
    basics.LAST_RUN = lvl1_main
    global bg, platform, ball, bricks
    bg = pygame.transform.scale(pygame.image.load('backgrounds/lvl1_bg.png'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom - basics.upper_menu.height))
    # brick_size = (60 * basics.X_COEFFICIENT, 30 * basics.Y_COEFFICIENT)
    brick_size = (135.2 * basics.X_COEFFICIENT, 29.5 * basics.Y_COEFFICIENT)
    platform = Platform((620 * basics.X_COEFFICIENT, 720 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 30 * basics.Y_COEFFICIENT), 'objects/platform.png', 8 * basics.SPEED_COEFFICIENT)
    ball = Ball((695 * basics.X_COEFFICIENT, 670 * basics.Y_COEFFICIENT), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT), 'objects/ball.png', 5 * basics.SPEED_COEFFICIENT, -1, -1)

    # create 36 bricks
    bricks = []
    brick_x, brick_y = 8 * basics.X_COEFFICIENT, 124 * basics.Y_COEFFICIENT
    delta_brick_x, delta_brick_y = 143.2 * basics.X_COEFFICIENT, 37.5 * basics.Y_COEFFICIENT
    for i in range(56):
        brick_color = 'none'
        if i % 10 == 0 and i != 0:
            brick_x, brick_y = 8 * basics.X_COEFFICIENT, brick_y + delta_brick_y
        if i in [0, 9, 10, 19]:
            brick_color = 'green'
        if i in [1, 2, 7, 8, 11, 12, 17, 18, 21, 22, 27, 28, 31, 32, 37, 38]:
            brick_color = 'purple'
        if i in [3, 4, 5, 6, 13, 16]:
            brick_color = 'yellow'
        if i in [23, 26, 33, 34, 35, 36, 44, 45, 54, 55]:
            brick_color = 'red'
        if brick_color != 'none':
            brick = Brick((brick_x, brick_y), brick_size, brick_color)
            bricks.append(brick)
        brick_x += delta_brick_x

    for msc in basics.MUSICS:
        msc.stop()
    music.play(loops=-1)
    basics.PRELAST_RUN = basics.LAST_RUN
    basics.LAST_RUN = run_lvl
    run_lvl()
    pygame.quit()
