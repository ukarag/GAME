# game options and settings

# set up constants that we need later
TITLE = "Mario"
WIDTH = 1024
HEIGHT = 768
FPS = 60
FONT_NAME = "arial"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"


# Tile
TILESIZE = int(32)


PLAYER_SPEED = 100
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 128

# Starting Platforms
PLATFORM_LIST = [(0, HEIGHT-40, WIDTH, 40),
                 (WIDTH/2-50, HEIGHT*3/4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)
                 ]


# Define some useful colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (225, 225, 0)
FORESTGREEN = (34,139,34)
LIGHTBLUE = (102, 205, 170)
GRAY = (64, 64, 64)
COOLBLUE = (0, 102, 204)
PINK = (204, 0, 204)
BGCOLOR = GRAY