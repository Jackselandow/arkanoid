import pygame as pg
from arkanoid import progress
from arkanoid.classes import Border, Music, Sound, Button, SurfaceMaker
# from arkanoid.game import Level
# from main import run_lvl1, run_lvl2, run_lvl3, run_lvl4
pg.init()

# DISPLAY = pg.display.set_mode((0, 0), pg.FULLSCREEN)
# WIN = pg.display.set_mode((0, 0), pg.FULLSCREEN)    # my WIN.size = (1440, 900)
WIN = pg.display.set_mode((1440, 900))
# WIN = pg.display.set_mode((900, 750))
# 1200, 750     800, 500
# WIN = pg.Surface((1440, 900))
# SCREEN = pg.display.set_mode((800, 500), pg.RESIZABLE)
# SCREEN_SIZE = SCREEN.get_size()
ARKANOID_ICON = pg.image.load('arkanoid/resources/graphics/ui/arkanoid_icon.png').convert()
pg.display.set_caption('ARKANOID', 'Arkanoid')
pg.display.set_icon(ARKANOID_ICON)

# basics
WIN_RECT = WIN.get_rect()
X_COEFFICIENT = FONT_COEFFICIENT = WIN_RECT.width / 1440
Y_COEFFICIENT = WIN_RECT.height / 900
CLOCK = pg.time.Clock()
FPS = 60
DESIRED_FUNC = None
LAST_RUN = None
PRELAST_RUN = None
SURFACEMAKER = SurfaceMaker()

# LEFT_BORDER = pg.Rect(-1, 0, 1, WIN_RECT.bottom)
# RIGHT_BORDER = pg.Rect(WIN_RECT.right, 0, 1, WIN_RECT.bottom)
# TOP_BORDER = pg.Rect(0, 115 * Y_COEFFICIENT, WIN_RECT.right, 1)
# BOTTOM_BORDER = pg.Rect(0, WIN_RECT.bottom, WIN_RECT.right, 1)

BLACK_SCREEN = pg.Surface((WIN_RECT.width, WIN_RECT.height)).convert()
BLACK_SCREEN.fill((0, 0, 0))
WHITE_SCREEN = pg.Surface((WIN_RECT.width, WIN_RECT.height)).convert()
WHITE_SCREEN.fill((255, 255, 255))

PREVOLUME = VOLUME = progress.get_value('volume', 'general')
MUSIC_VOLUME = progress.get_value('volume', 'music')
SOUND_VOLUME = progress.get_value('volume', 'sound')
PASSED_LEVELS = progress.get_value('level_progress', 'passed_levels') # e.g. = '1,2,3'
if PASSED_LEVELS == '':
    PASSED_LEVELS_LIST = []
else:
    PASSED_LEVELS_LIST = PASSED_LEVELS.split(',') # e.g. ['1', '2', '3']
MAX_LEVEL = 4
CONTROL_TYPE = progress.get_value('preferences', 'control_type')
AVAILABLE_SHAPES = progress.get_value('ball_shapes', 'available')
CURRENT_SHAPE = progress.get_value('ball_shapes', 'current')
SHAPE_ANIMATION = progress.get_value('preferences', 'ball_shape_animation')
BALL_SHAPES = ['faceless', 'red_ball', 'pacman', 'scarabeus', 'shield', 'shuriken']

# music & sounds
MENU_MUSIC = Music('arkanoid/resources/audio/music/main_menu.mp3', 1)
SETTINGS_MUSIC = Music('arkanoid/resources/audio/music/settings_menu.mp3', 1)
LEVELS_MENU_MUSIC = Music('arkanoid/resources/audio/music/levels_menu.mp3', 1)
LVL1_MUSIC = Music('arkanoid/resources/audio/music/lvl1.mp3', 1)
LVL2_MUSIC = Music('arkanoid/resources/audio/music/lvl2.mp3', 1)
LVL3_MUSIC = Music('arkanoid/resources/audio/music/lvl3.mp3', 1)
LVL4_MUSIC = Music('arkanoid/resources/audio/music/lvl4.mp3', 0.4)

CLICK_SOUND1 = Sound('arkanoid/resources/audio/sounds/button_click1.wav', 0.5)
CLICK_SOUND2 = Sound('arkanoid/resources/audio/sounds/button_click2.wav', 0.5)
SELECTION_SOUND = Sound('arkanoid/resources/audio/sounds/selection.mp3', 0.5)
START_SOUND = Sound('arkanoid/resources/audio/sounds/start.wav', 1)
DAMAGE_SOUND = Sound('arkanoid/resources/audio/sounds/damage.wav', 0.5)
EXPLOSION_SOUND = Sound('arkanoid/resources/audio/sounds/explosion.wav', 0.5)
BOUNCE_SOUND = Sound('arkanoid/resources/audio/sounds/bounce.wav', 0.2)
BUMP_SOUND = Sound('arkanoid/resources/audio/sounds/bump.wav', 0.7)
BUFF_SOUND = Sound('arkanoid/resources/audio/sounds/buff.mp3', 0.2)
PAUSE_IN_SOUND = Sound('arkanoid/resources/audio/sounds/pause_in.wav', 1)
PAUSE_OUT_SOUND = Sound('arkanoid/resources/audio/sounds/pause_out.wav', 1)
COUNTDOWN_SOUND = Sound('arkanoid/resources/audio/sounds/countdown.wav', 1)
VICTORY_SOUND = Sound('arkanoid/resources/audio/sounds/victory.wav', 1)
DEFEAT_SOUND = Sound('arkanoid/resources/audio/sounds/defeat.wav', 1)
INTRO_SOUND = Sound('arkanoid/resources/audio/sounds/intro.wav', 1)
POWER_DOWN_SOUND = Sound('arkanoid/resources/audio/sounds/power_down.mp3', 1)
OUTRO_SOUND = Sound('arkanoid/resources/audio/sounds/outro.wav', 1)


MUSICS = [MENU_MUSIC, SETTINGS_MUSIC, LEVELS_MENU_MUSIC, LVL1_MUSIC, LVL2_MUSIC, LVL3_MUSIC, LVL4_MUSIC]
SOUNDS = [CLICK_SOUND1, CLICK_SOUND2, SELECTION_SOUND, DAMAGE_SOUND, EXPLOSION_SOUND, BOUNCE_SOUND, BUMP_SOUND, BUFF_SOUND, PAUSE_IN_SOUND, PAUSE_OUT_SOUND, COUNTDOWN_SOUND, VICTORY_SOUND, DEFEAT_SOUND, INTRO_SOUND, POWER_DOWN_SOUND, OUTRO_SOUND]
