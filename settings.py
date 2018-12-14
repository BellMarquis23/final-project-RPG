#this file was created by Marcus Ponce
#thanks Chris Bradfield with Kids Can Code basic format

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
SPRITESHEET = "nico_spritesheet_updated.png"

#game settings
WIDTH = 1024  #16* 64 or 32*32 or 64*16
HEIGHT = 768 #16* 48 or 32*24 or 64*12
FPS = 60
TITLE = "Tilemap Project"
BGCOLOR = DARKGREY

TILESIZE = 72
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player settings
PLAYER_SPEED = 300
#PLAYER_ROT_SPEED = 250
#PLAYER_IMG = 'nicoStand.png'
#PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
