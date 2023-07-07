import pygame
from main import run_lvl1, run_lvl2, run_lvl3, run_lvl4
from classes import Border, Music, Sound, Button, LevelControl
from progress import get_value
pygame.init()

# DISPLAY = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    # my WIN.size = (1440, 900)
# WIN = pygame.display.set_mode((900, 750))
# 1200, 750     800, 500
# WIN = pygame.Surface((1440, 900))
# SCREEN = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
# SCREEN_SIZE = SCREEN.get_size()
ARKANOID_ICON = pygame.image.load('objects/bricks.png')
pygame.display.set_caption('ARKANOID', 'Arkanoid')
pygame.display.set_icon(ARKANOID_ICON)

# colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GRAY = 125, 125, 125
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

# LEFT_BORDER = pygame.Rect(-1, 0, 1, WIN_RECT.bottom)
# RIGHT_BORDER = pygame.Rect(WIN_RECT.right, 0, 1, WIN_RECT.bottom)
# TOP_BORDER = pygame.Rect(0, 115 * Y_COEFFICIENT, WIN_RECT.right, 1)
# BOTTOM_BORDER = pygame.Rect(0, WIN_RECT.bottom, WIN_RECT.right, 1)

LEFT_BORDER = Border((-1, 115 * Y_COEFFICIENT), (1, WIN_RECT.height))
RIGHT_BORDER = Border((WIN_RECT.right, 115 * Y_COEFFICIENT), (1, WIN_RECT.height))
TOP_BORDER = Border((0, 115 * Y_COEFFICIENT), (WIN_RECT.width, 1))
BOTTOM_BORDER = Border(WIN_RECT.bottomleft, (WIN_RECT.width, 1))

BLACK_SCREEN = pygame.Surface((WIN_RECT.width, WIN_RECT.height))
BLACK_SCREEN.fill((0, 0, 0))
WHITE_SCREEN = pygame.Surface((WIN_RECT.width, WIN_RECT.height))
WHITE_SCREEN.fill((255, 255, 255))

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
SHAPE_ANIMATION = get_value('Preferences', 'ball_shape_animation', None)
BALL_SHAPES = ['faceless', 'red_ball', 'pac-man', 'scarabeus', 'shield', 'shuriken']

# music & sounds
MENU_MUSIC = Music('sounds/menu_music.mp3', 1)
SETTINGS_MUSIC = Music('sounds/settings_music.mp3', 1)
LEVELS_MENU_MUSIC = Music('sounds/levels_menu_music.mp3', 1)
LVL1_MUSIC = Music('sounds/lvl1_music.mp3', 1)
LVL2_MUSIC = Music('sounds/lvl2_music.mp3', 1)
LVL3_MUSIC = Music('sounds/lvl3_music.mp3', 1)
LVL4_MUSIC = Music('sounds/lvl4_music.mp3', 0.4)

CLICK_SOUND1 = Sound('sounds/button_click1.wav', 0.5)
CLICK_SOUND2 = Sound('sounds/button_click2.wav', 0.5)
SELECTION_SOUND = Sound('sounds/selection.mp3', 0.5)
START_SOUND = Sound('sounds/start.wav', 1)
DAMAGE_SOUND = Sound('sounds/damage.wav', 0.5)
EXPLOSION_SOUND = Sound('sounds/explosion.wav', 0.5)
BOUNCE_SOUND = Sound('sounds/bounce.wav', 0.2)
BUMP_SOUND = Sound('sounds/bump.wav', 0.7)
BUFF_SOUND = Sound('sounds/buff.mp3', 0.2)
PAUSE_IN_SOUND = Sound('sounds/pause_in.wav', 1)
PAUSE_OUT_SOUND = Sound('sounds/pause_out.wav', 1)
COUNTDOWN_SOUND = Sound('sounds/countdown.wav', 1)
WIN_SOUND = Sound('sounds/win.wav', 1)
LOSE_SOUND = Sound('sounds/game_over.wav', 1)
PREVIEW_SOUND = Sound('sounds/preview.wav', 1)
POWER_DOWN_SOUND = Sound('sounds/power_down.mp3', 1)
POSTVIEW_SOUND = Sound('sounds/postview.wav', 1)


MUSICS = [MENU_MUSIC, SETTINGS_MUSIC, LEVELS_MENU_MUSIC, LVL1_MUSIC, LVL2_MUSIC, LVL3_MUSIC, LVL4_MUSIC]
SOUNDS = [CLICK_SOUND1, CLICK_SOUND2, SELECTION_SOUND, DAMAGE_SOUND, EXPLOSION_SOUND, BOUNCE_SOUND, BUMP_SOUND, BUFF_SOUND, PAUSE_IN_SOUND, PAUSE_OUT_SOUND, COUNTDOWN_SOUND, WIN_SOUND, LOSE_SOUND, PREVIEW_SOUND, POWER_DOWN_SOUND, POSTVIEW_SOUND]

LEVEL = LevelControl(None, None, None)

lvl1_icon_button = Button(None, None, None, feedbacks=[START_SOUND.play, run_lvl1])
lvl2_icon_button = Button(None, None, None, feedbacks=[START_SOUND.play, run_lvl2])
lvl3_icon_button = Button(None, None, None, feedbacks=[START_SOUND.play, run_lvl3])
lvl4_icon_button = Button(None, None, None, feedbacks=[START_SOUND.play, run_lvl4])
# lvl5_icon_button = Button(None, None, None, feedbacks=[START_SOUND.play, run_lvl5])
LEVELS_ICONS = [lvl1_icon_button, lvl2_icon_button, lvl3_icon_button, lvl4_icon_button]
