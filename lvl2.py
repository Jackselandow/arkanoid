import pygame
import basics
pygame.init()


def run_lvl():
    basics.LVL2_MUSIC.update()

    level2_text = basics.RETROBLAZE_FONT.render('l e v e l 2', False, basics.GREEN)
    level2_rect = level2_text.get_rect(center=(basics.WIN_RECT.right / 2, upper_menu.bottom / 2))

    while True:
        key_pressed = pygame.key.get_pressed()
        bricks_left_text = basics.PIXEBOY_FONT.render(('BRICKS LEFT: ' + str(len(basics.LEVEL.bricks) - 10)), False, basics.WHITE)
        bricks_left_rect = bricks_left_text.get_rect(bottomright=(basics.WIN_RECT.right - 8 * basics.X_COEFFICIENT, upper_menu.bottom - 8 * basics.Y_COEFFICIENT))
        basics.CLOCK.tick(basics.FPS)
        if basics.LEVEL.countdown_state is False:
            for event in pygame.event.get():
                pause_button.detect_click(event)
            if key_pressed[pygame.K_ESCAPE]:
                pause_button.clicked()

        if len(basics.LEVEL.bricks) - 10 == 0:
            from main import run_win
            run_win('2')
        elif len(basics.LEVEL.balls) == 0:
            from main import run_lose
            run_lose()

        basics.WIN.blit(bg, (0, upper_menu.bottom))
        basics.WIN.fill(basics.BLACK, upper_menu)
        basics.WIN.blit(level2_text, level2_rect)
        basics.WIN.blit(bricks_left_text, bricks_left_rect)
        basics.LEVEL.platform.show()
        pause_button.show()
        for ball in basics.LEVEL.balls:
            ball.show()
        for brick in basics.LEVEL.bricks:
            brick.show()
        if basics.LEVEL.countdown_state is False:
            pause_button.detect_mouse_collision()
            basics.LEVEL.platform.movement()
            detect_lvl_start(key_pressed)
        pygame.display.update()
        if basics.LEVEL.countdown_state is True:
            from main import run_countdown
            run_countdown()
        if basics.LEVEL.countdown_state == 'process':
            basics.LEVEL.countdown_index += 1
            from main import run_countdown
            run_countdown()


def detect_lvl_start(key_pressed):
    if key_pressed[pygame.K_SPACE] and basics.LEVEL.level_started is False:
        press_space_text.set_alpha(basics.LEVEL.press_space_alpha)
        basics.LEVEL.level_started = True
        basics.LVL2_MUSIC.play(loops=-1)
    if basics.LEVEL.level_started is True:
        for ball in basics.LEVEL.balls:
            ball.movement()
    else:
        if basics.LEVEL.press_space_alpha >= 255:
            basics.LEVEL.press_space_state = 'disappear'
        elif basics.LEVEL.press_space_alpha <= 0:
            basics.LEVEL.press_space_state = 'appear'
        if basics.LEVEL.press_space_state == 'appear':
            basics.LEVEL.press_space_alpha += 5
            press_space_text.set_alpha(basics.LEVEL.press_space_alpha)
        else:
            basics.LEVEL.press_space_alpha -= 5
            press_space_text.set_alpha(basics.LEVEL.press_space_alpha)
        basics.WIN.blit(press_space_text, press_space_rect)
        for ball in basics.LEVEL.balls:
            ball.rect.centerx = basics.LEVEL.platform.rect.centerx


def create_bricks():
    brick_x, brick_y = 8 * basics.X_COEFFICIENT, 124 * basics.Y_COEFFICIENT
    brick_size = (81.5 * basics.X_COEFFICIENT, 65 * basics.Y_COEFFICIENT)
    delta_brick_x, delta_brick_y = 89.5 * basics.X_COEFFICIENT, 73 * basics.Y_COEFFICIENT
    for i in range(80):
        brick_color = 'none'
        if i % 16 == 0 and i != 0:
            brick_x, brick_y = 8 * basics.X_COEFFICIENT, brick_y + delta_brick_y
        if i in [4, 11, 17, 21, 26, 30, 34, 38, 41, 45, 51, 60]:
            brick_color = 'yellow'
        if i in [5, 6, 7, 8, 9, 10, 16, 22, 23, 24, 25, 31, 32, 33, 39, 40, 46, 47, 48, 49, 50, 61, 62, 63]:
            brick_color = 'orange'
        if i in [55, 56]:
            brick_color = 'red'
        if i in [0, 15]:
            brick_color = 'blue'
        if i in [64, 65, 66, 67, 68, 75, 76, 77, 78, 79]:
            brick_color = 'grey'
        if brick_color != 'none':
            basics.Brick((brick_x, brick_y), brick_size, brick_color)
        brick_x += delta_brick_x


def lvl2_main():
    basics.LAST_RUN = lvl2_main
    global press_space_text, press_space_rect, upper_menu, pause_button, bg
    basics.LEVEL.__init__()
    
    press_space_text = basics.PIXELOID_FONT.render('Press SPACE to start', False, basics.RED)
    press_space_rect = press_space_text.get_rect(center=(basics.WIN_RECT.right / 2, basics.WIN_RECT.height / 2))
    upper_menu = pygame.Rect(0, 0, basics.WIN_RECT.width, 116 * basics.Y_COEFFICIENT)
    pause_button = basics.ImageButton('objects/pause_button.png', (8 * basics.X_COEFFICIENT, 8 * basics.Y_COEFFICIENT), (100 * basics.X_COEFFICIENT, 100 * basics.Y_COEFFICIENT), [basics.run_pause])
    bg = pygame.transform.scale(pygame.image.load('backgrounds/lvl2_bg.png'), (basics.WIN_RECT.right, basics.WIN_RECT.bottom - upper_menu.height))
    basics.LEVEL.platform = basics.Platform((620 * basics.X_COEFFICIENT, 720 * basics.Y_COEFFICIENT), (200 * basics.X_COEFFICIENT, 30 * basics.Y_COEFFICIENT), 'objects/platform.png', 8)
    basics.LEVEL.balls.append(basics.Ball((695 * basics.X_COEFFICIENT, 670 * basics.Y_COEFFICIENT), (50 * basics.X_COEFFICIENT, 50 * basics.Y_COEFFICIENT), basics.CURRENT_SHAPE, 5))
    create_bricks()

    for msc in basics.MUSICS:
        msc.stop()
    basics.PRELAST_RUN = basics.LAST_RUN
    basics.LAST_RUN = run_lvl
    basics.LEVEL_STARTED = False
    run_lvl()
