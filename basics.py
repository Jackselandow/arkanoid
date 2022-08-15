import pygame
from main import run_menu, run_pause, run_countdown, run_win, run_lose, run_lvl1, run_lvl2, run_lvl3
from classes import Music, Sound, TextButton, ImageButton, Platform, Ball, Brick, Shape, LevelControl, handle_buffs
from progress import get_value, update_value, update_game_progress
from settings import run_main_settings, run_general_settings, run_volume_settings, run_ball_shape_settings
from levels_menu import run_levels_menu
pygame.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    # my WIN.size = (1440, 900)
# WIN = pygame.display.set_mode((900, 750))
# 1200, 750     800, 500
ARKANOID_ICON = pygame.image.load('objects/bricks.png')
pygame.display.set_caption('ARKANOID', 'Arkanoid')
pygame.display.set_icon(ARKANOID_ICON)

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
ORANGE = 255, 160, 0

# basics
WIN_RECT = WIN.get_rect()
X_COEFFICIENT = FONT_COEFFICIENT = WIN_RECT.width / 1440
Y_COEFFICIENT = WIN_RECT.height / 900
CLOCK = pygame.time.Clock()
FPS = 60
LAST_RUN = None
PRELAST_RUN = None

LEFT_BORDER = pygame.Rect(-1, 0, 1, WIN_RECT.bottom)
RIGHT_BORDER = pygame.Rect(WIN_RECT.right, 0, 1, WIN_RECT.bottom)
TOP_BORDER = pygame.Rect(0, 115 * Y_COEFFICIENT, WIN_RECT.right, 1)
BOTTOM_BORDER = pygame.Rect(0, WIN_RECT.bottom, WIN_RECT.right, 1)
BLACK_SCREEN = pygame.Surface((WIN_RECT.width, WIN_RECT.height))
BLACK_SCREEN.fill((0, 0, 0))

PREVOLUME = VOLUME = get_value('Volume', 'general', None)
MUSIC_VOLUME = get_value('Volume', 'music', None)
SOUND_VOLUME = get_value('Volume', 'sound', None)
PASSED_LEVELS = get_value('Level Progress', 'passed_levels', None)
if PASSED_LEVELS == '':
    PASSED_LEVELS_LIST = []
else:
    PASSED_LEVELS_LIST = PASSED_LEVELS.split(',')
CONTROL_TYPE = get_value('Preferences', 'control_type', None)
AVAILABLE_SHAPES = get_value('Ball Shapes', 'available', None)
CURRENT_SHAPE = get_value('Ball Shapes', 'current', None)
BALL_SHAPES = ['faceless', 'red_ball', 'pac-man', 'scarabeus', 'shield']

# fonts
PIXEBOY_FONT = pygame.font.Font('fonts/pixeboy_font.ttf', int(60 * FONT_COEFFICIENT))
BIG_PIXEBOY_FONT = pygame.font.Font('fonts/pixeboy_font.ttf', int(100 * FONT_COEFFICIENT))
PIXELOID_FONT = pygame.font.Font('fonts/pixeloid_font.ttf', int(50 * FONT_COEFFICIENT))
BIG_PIXELOID_FONT = pygame.font.Font('fonts/pixeloid_font.ttf', int(100 * FONT_COEFFICIENT))
TALES_FONT = pygame.font.Font('fonts/tales_font.ttf', int(50 * FONT_COEFFICIENT))
ENDLESS_FONT = pygame.font.Font('fonts/endless_font.ttf', int(100 * FONT_COEFFICIENT))
SMALL_ENDLESS_FONT = pygame.font.Font('fonts/endless_font.ttf', int(75 * FONT_COEFFICIENT))
BIG_ENDLESS_FONT = pygame.font.Font('fonts/endless_font.ttf', int(150 * FONT_COEFFICIENT))
RETROBLAZE_FONT = pygame.font.Font('fonts/retroblaze_font.ttf', int(100 * FONT_COEFFICIENT))

# music & sounds
MENU_MUSIC = Music('sounds/menu_music.mp3', 1)
SETTINGS_MUSIC = Music('sounds/settings_music.mp3', 1)
LEVELS_MENU_MUSIC = Music('sounds/levels_menu_music.mp3', 1)
LVL1_MUSIC = Music('sounds/lvl1_music.mp3', 1)
LVL2_MUSIC = Music('sounds/lvl2_music.mp3', 1)
LVL3_MUSIC = Music('sounds/lvl3_music.mp3', 1)

CLICK_SOUND1 = Sound('sounds/button_click1.wav', 0.5)
CLICK_SOUND2 = Sound('sounds/button_click2.wav', 0.5)
START_SOUND = Sound('sounds/start.wav', 1)
EXPLOSION_SOUND = Sound('sounds/explosion.wav', 0.5)
BOUNCE_SOUND = Sound('sounds/bounce.wav', 0.2)
BUFF_SOUND = Sound('sounds/buff.mp3', 0.2)
PAUSE_IN_SOUND = Sound('sounds/pause_in.wav', 1)
PAUSE_OUT_SOUND = Sound('sounds/pause_out.wav', 1)
COUNTDOWN_SOUND = Sound('sounds/countdown.wav', 1)
WIN_SOUND = Sound('sounds/win.wav', 1)
LOSE_SOUND = Sound('sounds/game_over.wav', 1)

MUSICS = [MENU_MUSIC, SETTINGS_MUSIC, LEVELS_MENU_MUSIC, LVL1_MUSIC, LVL2_MUSIC, LVL3_MUSIC]
SOUNDS = [CLICK_SOUND1, START_SOUND, EXPLOSION_SOUND, BOUNCE_SOUND, BUFF_SOUND, PAUSE_IN_SOUND, PAUSE_OUT_SOUND, COUNTDOWN_SOUND, WIN_SOUND, LOSE_SOUND]

LEVEL = LevelControl()

lvl1_icon_button = ImageButton('objects/levels_icons/lvl1_icon.png', (160 * X_COEFFICIENT, 270 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [START_SOUND.play, run_lvl1])
lvl2_icon_button = ImageButton('objects/levels_icons/lvl2_icon.png', (560 * X_COEFFICIENT, 270 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [START_SOUND.play, run_lvl2])
lvl3_icon_button = ImageButton('objects/levels_icons/lvl3_icon.png', (960 * X_COEFFICIENT, 270 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [START_SOUND.play, run_lvl3])
# lvl4_icon_button = ImageButton('objects/levels_icons/lvl4_icon.png', (360 * X_COEFFICIENT, 545 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [START_SOUND.play, main.run_lvl4])
# lvl5_icon_button = ImageButton('objects/levels_icons/lvl5_icon.png', (760 * X_COEFFICIENT, 545 * Y_COEFFICIENT), (320 * X_COEFFICIENT, 160 * Y_COEFFICIENT), [START_SOUND.play, main.run_lvl5])
LEVELS_ICONS = [lvl1_icon_button, lvl2_icon_button, lvl3_icon_button]
