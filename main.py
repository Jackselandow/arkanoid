import basics


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



def main_run():
    run_preview()


def run_preview():
    basics.LAST_RUN = run_preview
    from main_menu import preview
    preview()


def run_menu(alpha=-5):
    basics.LAST_RUN = run_menu
    basics.PRELAST_RUN = basics.LAST_RUN
    from main_menu import main_menu
    main_menu(alpha)


def run_settings():
    basics.LAST_RUN = run_settings
    from settings import main_settings
    main_settings()


def run_levels_menu():
    basics.LAST_RUN = run_levels_menu
    from levels_menu import levels_menu
    levels_menu()


def run_pause():
    from pause import pause
    pause()


def run_countdown():
    from pause import countdown
    countdown()


def run_win(passed_level):
    from win_lose import win
    win(passed_level)


def run_lose():
    from win_lose import lose
    lose()


def run_lvl1():
    basics.LAST_RUN = run_lvl1
    from lvl1 import lvl1_main
    lvl1_main()


def run_lvl2():
    basics.LAST_RUN = run_lvl2
    from lvl2 import lvl2_main
    lvl2_main()


def run_lvl3():
    basics.LAST_RUN = run_lvl3
    from lvl3 import lvl3_main
    lvl3_main()


def run_lvl4():
    basics.LAST_RUN = run_lvl4
    from lvl4 import lvl4_main
    lvl4_main()


if __name__ == "__main__":
    main_run()
