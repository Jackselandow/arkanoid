import pygame
from classes import TextButton, ImageButton, Music, Sound
from progress import get_values
from settings import run_main_settings, run_volume_settings
from levels_menu import run_levels_menu
import main
pygame.init()

# colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 125, 125, 125
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
DARK_GREEN = 38, 133, 38
PURPLE = 255, 0, 255
YELLOW = 255, 255, 0

# basics
WIN_RECT = main.WIN.get_rect()
X_COEFFICIENT = FONT_COEFFICIENT = WIN_RECT.width / 1440
Y_COEFFICIENT = WIN_RECT.height / 900
SPEED_COEFFICIENT = X_COEFFICIENT * Y_COEFFICIENT
CLOCK = pygame.time.Clock()
FPS = 60
LEFT_BORDER = pygame.Rect(-1, 0, 1, WIN_RECT.bottom)
RIGHT_BORDER = pygame.Rect(WIN_RECT.right, 0, 1, WIN_RECT.bottom)
TOP_BORDER = pygame.Rect(0, 115 * Y_COEFFICIENT, WIN_RECT.right, 1)
BOTTOM_BORDER = pygame.Rect(0, WIN_RECT.bottom, WIN_RECT.right, 1)
BLACK_SCREEN = pygame.Surface((WIN_RECT.width, WIN_RECT.height))
BLACK_SCREEN.fill(BLACK)
VOLUME = 1
PREVOLUME = 1
MUSIC_VOLUME = 1
SOUND_VOLUME = 1
LAST_RUN = None
PRELAST_RUN = None
LEVELS_PASSED, NAMES_PASSED_LEVELS = get_values()

# fonts
PIXEBOY_FONT = pygame.font.Font('fonts/pixeboy_font.ttf', int(round(60 * FONT_COEFFICIENT)))
BIG_PIXEBOY_FONT = pygame.font.Font('fonts/pixeboy_font.ttf', int(round(100 * FONT_COEFFICIENT)))
PIXELOID_FONT = pygame.font.Font('fonts/pixeloid_font.ttf', int(round(50 * FONT_COEFFICIENT)))
BIG_PIXELOID_FONT = pygame.font.Font('fonts/pixeloid_font.ttf', int(round(100 * FONT_COEFFICIENT)))
TALES_FONT = pygame.font.Font('fonts/tales_font.ttf', int(round(50 * FONT_COEFFICIENT)))
ENDLESS_FONT = pygame.font.Font('fonts/endless_font.ttf', int(round(100 * FONT_COEFFICIENT)))
BIG_ENDLESS_FONT = pygame.font.Font('fonts/endless_font.ttf', int(round(150 * FONT_COEFFICIENT)))
RETROBLAZE_FONT = pygame.font.Font('fonts/retroblaze_font.ttf', int(round(100 * FONT_COEFFICIENT)))

# music & sounds
menu_music = Music('sounds/menu_music.mp3', 1)
settings_music = Music('sounds/settings_music.mp3', 1)
levels_music = Music('sounds/levels_menu_music.mp3', 1)

CLICK_SOUND = Sound('sounds/button_click.wav', 0.5)
START_SOUND = Sound('sounds/start.wav', 1)
EXPLOSION_SOUND = Sound('sounds/explosion.wav', 0.5)
BOUNCE_SOUND = Sound('sounds/bounce.wav', 0.2)
WIN_SOUND = Sound('sounds/win.wav', 1)
LOSE_SOUND = Sound('sounds/game_over.wav', 1)

MUSICS = [menu_music, settings_music, levels_music]
SOUNDS = [CLICK_SOUND, START_SOUND, EXPLOSION_SOUND, WIN_SOUND, LOSE_SOUND]

# preview objects
preview_bg = pygame.transform.scale(pygame.image.load('backgrounds/preview_bg1.png'), (WIN_RECT.right, WIN_RECT.bottom))

# menu objects
menu_bg = pygame.transform.scale(pygame.image.load('backgrounds/menu_bg.jpeg'), (WIN_RECT.right, WIN_RECT.bottom))
arkanoid_logo = pygame.transform.scale(pygame.image.load('objects/arkanoid_logo.png'), (1400 * X_COEFFICIENT, 300 * Y_COEFFICIENT))
author_text = TALES_FONT.render('Jackselandow Edition', False, WHITE)
author_rect = author_text.get_rect(topleft=(0, 5 * Y_COEFFICIENT))
play_button = TextButton('PLAY', (440 * X_COEFFICIENT, 370 * Y_COEFFICIENT), 300 * FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', WHITE, RED, ['none'])
settings_button = TextButton('SETTINGS', (560 * X_COEFFICIENT, 570 * Y_COEFFICIENT), 60 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', WHITE, GREEN, [[CLICK_SOUND.play, 0], run_main_settings])
levels_button = TextButton('LEVELS', (600 * X_COEFFICIENT, 660 * Y_COEFFICIENT), 60 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', WHITE, BLUE, [[CLICK_SOUND.play, 0], run_levels_menu])
exit_button = TextButton('EXIT', (640 * X_COEFFICIENT, 750 * Y_COEFFICIENT), 60 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', WHITE, GREY, [[CLICK_SOUND.play, 0], main.pygame.quit])
version_text = TALES_FONT.render('Version 3.0', False, BLACK)
version_rect = version_text.get_rect(bottomright=(WIN_RECT.right - 8 * X_COEFFICIENT, WIN_RECT.bottom))

# settings objects
settings_bg = pygame.transform.scale(pygame.image.load('backgrounds/settings_bg.jpg'), (WIN_RECT.right, WIN_RECT.bottom))
back_settings_button = TextButton('<', (10 * X_COEFFICIENT, 10 * Y_COEFFICIENT), 100 * FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', RED, GREY, [[CLICK_SOUND.play, 0], 'PRELAST_RUN'])
main_settings_text = BIG_ENDLESS_FONT.render('MAIN SETTINGS', False, YELLOW)
main_settings_rect = main_settings_text.get_rect(center=(WIN_RECT.right / 2, 100 * Y_COEFFICIENT))
volume_settings_button = TextButton('VOLUME', (480 * X_COEFFICIENT, 300 * Y_COEFFICIENT), 120 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', WHITE, 'none', [[CLICK_SOUND.play, 0], run_volume_settings])

back_volume_settings_button = TextButton('<', (10 * X_COEFFICIENT, 10 * Y_COEFFICIENT), 100 * FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', RED, GREY, [[CLICK_SOUND.play, 0], 'LAST_RUN'])
volume_settings_text = ENDLESS_FONT.render('VOLUME SETTINGS', False, YELLOW)
volume_settings_rect = volume_settings_text.get_rect(center=(WIN_RECT.right / 2, 75 * Y_COEFFICIENT))
general_volume_text = PIXELOID_FONT.render('GENERAL VOLUME', False, WHITE)
general_volume_rect = general_volume_text.get_rect(center=(WIN_RECT.right / 2, 175 * Y_COEFFICIENT))
music_volume_text = PIXELOID_FONT.render('MUSIC VOLUME', False, WHITE)
music_volume_rect = music_volume_text.get_rect(center=(WIN_RECT.right / 2, 400 * Y_COEFFICIENT))
sound_volume_text = PIXELOID_FONT.render('SOUND VOLUME', False, WHITE)
sound_volume_rect = sound_volume_text.get_rect(center=(WIN_RECT.right / 2, 625 * Y_COEFFICIENT))
volume_bar = pygame.transform.scale(pygame.image.load('objects/volume_bar.png'), (680 * X_COEFFICIENT, 110 * Y_COEFFICIENT))
red_square = pygame.transform.scale(pygame.image.load('objects/red_square.png'), (50 * X_COEFFICIENT, 50 * Y_COEFFICIENT))
minus_general_volume_button = ImageButton('objects/minus_volume.png', (260 * X_COEFFICIENT, 200 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [[CLICK_SOUND.play, 0], 'none'])
plus_general_volume_button = ImageButton('objects/plus_volume.png', (1080 * X_COEFFICIENT, 200 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [[CLICK_SOUND.play, 0], 'none'])
minus_music_volume_button = ImageButton('objects/minus_volume.png', (260 * X_COEFFICIENT, 425 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [[CLICK_SOUND.play, 0], 'none'])
plus_music_volume_button = ImageButton('objects/plus_volume.png', (1080 * X_COEFFICIENT, 425 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [[CLICK_SOUND.play, 0], 'none'])
minus_sound_volume_button = ImageButton('objects/minus_volume.png', (260 * X_COEFFICIENT, 650 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [[CLICK_SOUND.play, 0], 'none'])
plus_sound_volume_button = ImageButton('objects/plus_volume.png', (1080 * X_COEFFICIENT, 650 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [[CLICK_SOUND.play, 0], 'none'])

# levels menu objects
levels_menu_bg = pygame.transform.scale(pygame.image.load('backgrounds/levels_menu_bg.png'), (WIN_RECT.width, WIN_RECT.height))
back_levels_button = TextButton('<', (10 * X_COEFFICIENT, 10 * Y_COEFFICIENT), 100 * FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', RED, GREY, [[CLICK_SOUND.play, 0], 'PRELAST_RUN'])
levels_text = BIG_ENDLESS_FONT.render('LEVELS', False, YELLOW)
levels_rect = levels_text.get_rect(center=(WIN_RECT.right / 2, 100 * Y_COEFFICIENT))
lvl1_icon_button = ImageButton('objects/lvl1_icon.png', (160 * X_COEFFICIENT, 270 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [[START_SOUND.play, 0], main.run_lvl1])
lvl1_icon_text = TALES_FONT.render('Classic', False, WHITE)
lvl1_icon_rect = lvl1_icon_text.get_rect(center=(320 * X_COEFFICIENT, 472.5 * Y_COEFFICIENT))
lvl2_icon_button = ImageButton('objects/lvl2_icon.png', (560 * X_COEFFICIENT, 270 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [[START_SOUND.play, 0], main.run_lvl2])
lvl2_icon_text = TALES_FONT.render('Middle Ages', False, WHITE)
lvl2_icon_rect = lvl2_icon_text.get_rect(center=(720 * X_COEFFICIENT, 472.5 * Y_COEFFICIENT))
lvl3_icon_button = ImageButton('objects/lvl1_icon.png', (960 * X_COEFFICIENT, 270 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [[START_SOUND.play, 0], main.run_lvl1])
lvl3_icon_text = TALES_FONT.render('Classic', False, WHITE)
lvl3_icon_rect = lvl3_icon_text.get_rect(center=(1120 * X_COEFFICIENT, 472.5 * Y_COEFFICIENT))
# lvl4_icon_button = ImageButton('objects/lvl1_icon.png', (360 * X_COEFFICIENT, 545 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [[START_SOUND.play, 0], main.run_lvl1])
# lvl4_icon_text = TALES_FONT.render('Classic', False, WHITE)
# lvl4_icon_rect = lvl4_icon_text.get_rect(center=(520 * X_COEFFICIENT, 747.5 * Y_COEFFICIENT))
# lvl5_icon_button = ImageButton('objects/lvl1_icon.png', (760 * X_COEFFICIENT, 545 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [[START_SOUND.play, 0], main.run_lvl1])
# lvl5_icon_text = TALES_FONT.render('Classic', False, WHITE)
# lvl5_icon_rect = lvl5_icon_text.get_rect(center=(920 * X_COEFFICIENT, 747.5 * Y_COEFFICIENT))
interference = pygame.transform.scale(pygame.image.load('objects/tv_interference.jpeg'), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT))
locker = pygame.transform.scale(pygame.image.load('objects/locker.png'), (50 * X_COEFFICIENT, 75 * Y_COEFFICIENT))
levels_icons = [lvl1_icon_button, lvl2_icon_button, lvl3_icon_button]

# levels objects
upper_menu = pygame.Rect(0, 0, WIN_RECT.width, 116 * Y_COEFFICIENT)
pause_button = ImageButton('objects/pause_button.png', (8 * X_COEFFICIENT, 8 * Y_COEFFICIENT), (100 * X_COEFFICIENT, 100 * Y_COEFFICIENT), [main.run_pause])
pause_bg = pygame.transform.scale(pygame.image.load('backgrounds/pause_bg.png'), (WIN_RECT.right / 2, WIN_RECT.bottom / 2))
pause_text = BIG_PIXEBOY_FONT.render('GAME PAUSED', False, WHITE)
pause_rect = pause_text.get_rect(center=(WIN_RECT.right / 2, 300 * Y_COEFFICIENT))
restart_button = ImageButton('objects/restart_button.png', (430 * X_COEFFICIENT, 370 * Y_COEFFICIENT), (180 * X_COEFFICIENT, 180 * Y_COEFFICIENT), ['PRELAST_RUN'])
main_menu_button = ImageButton('objects/main_menu_button.png', (630 * X_COEFFICIENT, 370 * Y_COEFFICIENT), (180 * X_COEFFICIENT, 180 * Y_COEFFICIENT), [main.run_menu])
full_volume_button = ImageButton('objects/full_volume_button.png', (830 * X_COEFFICIENT, 370 * Y_COEFFICIENT), (180 * X_COEFFICIENT, 180 * Y_COEFFICIENT), ['none'])
no_volume_button = ImageButton('objects/no_volume_button.png', (830 * X_COEFFICIENT, 370 * Y_COEFFICIENT), (180 * X_COEFFICIENT, 180 * Y_COEFFICIENT), ['none'])
resume_button = TextButton('RESUME', (540 * X_COEFFICIENT, 570 * Y_COEFFICIENT), 130 * FONT_COEFFICIENT, 'fonts/pixeboy_font.ttf', DARK_GREEN, GREEN, [pygame.mixer.unpause, 'LAST_RUN'])

# win & lose screens objects
CUP = pygame.transform.scale(pygame.image.load('objects/cup.png'), (200 * X_COEFFICIENT, 200 * Y_COEFFICIENT))
LEVEL_TEXT = BIG_PIXELOID_FONT.render('LEVEL', False, WHITE)
LEVEL_RECT = LEVEL_TEXT.get_rect(center=(WIN_RECT.right / 2, 150 * Y_COEFFICIENT))
COMPLETED_TEXT = BIG_PIXELOID_FONT.render('COMPLETED', False, WHITE)
COMPLETED_RECT = COMPLETED_TEXT.get_rect(center=(WIN_RECT.right / 2, 270 * Y_COEFFICIENT))
LOSE_SCREEN = pygame.transform.scale(pygame.image.load('objects/lose.png'), (640 * X_COEFFICIENT, 320 * Y_COEFFICIENT))
next_level_button = TextButton('NEXT LEVEL', (470 * X_COEFFICIENT, 450 * Y_COEFFICIENT), 75 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', GREEN, BLACK, [levels_icons[LEVELS_PASSED].clicked])
menu_button = TextButton('MAIN MENU', (495 * X_COEFFICIENT, 570 * Y_COEFFICIENT), 75 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', GREY, BLACK, [[CLICK_SOUND.play, 0], WIN_SOUND.stop, LOSE_SOUND.stop, main.run_menu])
retry_button = TextButton('RETRY', (595 * X_COEFFICIENT, 450 * Y_COEFFICIENT), 75 * FONT_COEFFICIENT, 'fonts/pixeloid_font.ttf', RED, BLACK, [[CLICK_SOUND.play, 0], 'PRELAST_RUN'])
