#this file was created by Marcus Ponce
#thanks Chris Bradfield with Kids Can Code basic format
#credit to kirbysmith on Deviantart for creating sprites
#credit to Kenny's free art and assets packs for other tiles

import pygame as pg 

#define some colors (R,G,B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = ()
FLOOR_BLUE = (122, 188, 201)
LIGHT_GREEN = (148, 239, 153)
SPRITESHEET = "nico_spritesheet_updated.png"

#game settings
WIDTH = 1024  #16* 64 or 32*32 or 64*16
HEIGHT = 768 #16* 48 or 32*24 or 64*12
FPS = 60
TITLE = "Tilemap Project"
BGCOLOR = LIGHT_GREEN

TILESIZE = 72
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#graphics
WALL_IMG = 'element_red_square.png'
#player settings
PLAYER_SPEED = 300
#PLAYER_ROT_SPEED = 250
#PLAYER_IMG = 'nicoStand.png'
#PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
