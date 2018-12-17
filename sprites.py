#this file was created by Marcus Ponce
#thank you Chris Bradfield with Kids Can Code basic outline
#spritesheet by kirbysmith on Deviantart
import pygame as pg
from settings import *
#from tilemap import collide_hit_rect
vec = pg.math.Vector2 
# "sprite sheet class enstantiates the spritesheet file where you can pick parts out from the entire sheet;" 
# "the main purpose is to control the amount of files in your image folder"

#spritesheet class from Mr. Cozort; from Chris Bradfield 
class Spritesheet:
    # class for loading and parsing (understanding the spritesheet) the sprite sheet
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        #grab an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        #image = pg.transform.scale(image, (width // 2, height // 2))
        return image

# "player class creates a controllable player with values assigned to itself including animation, walking,"
# "and the shape of the player being a rectangle"
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking_forward = False
        self.walking_left = False
        self.walking_right = False
        self.walking_back = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images() 
        self.image = self.standing_frame[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        #self.rot = 0 
        
    # "this chunk of code flips between two images when the player moves in"
    # "a certain direction"    
    def load_images(self):
        self.standing_frame = [self.game.spritesheet.get_image(161, 5, 68, 68)]
        for frame in self.standing_frame:
            frame.set_colorkey(BLACK)

        self.walking_forward_frames = [self.game.spritesheet.get_image(161, 5, 68, 68),
                                self.game.spritesheet.get_image(5, 83, 68, 68)]
        for frame in self.walking_forward_frames:
            frame.set_colorkey(BLACK)

        self.walking_left_frames = [self.game.spritesheet.get_image(161, 5, 68, 68),
                                self.game.spritesheet.get_image(83, 83, 68, 68)]
        for frame in self.walking_left_frames:
            frame.set_colorkey(BLACK)

        self.walking_right_frames = [self.game.spritesheet.get_image(5, 83, 68, 68),
                                self.game.spritesheet.get_image(161, 83, 68, 68)]
        for frame in self.walking_right_frames:
            frame.set_colorkey(BLACK)

        self.walking_back_frames = [self.game.spritesheet.get_image(-83, -5, 68, 68),
                                self.game.spritesheet.get_image(83, 83, 68, 68)]
        for frame in self.walking_back_frames:
            frame.set_colorkey(BLACK)

    # def get_keys(self):
    #     self.rot_speed = 0 
    #     self.vel = vec(0, 0)
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_LEFT] or keys[pg.K_a]:
    #         self.rot_speed = PLAYER_ROT_SPEED
    #     if keys[pg.K_RIGHT] or keys[pg.K_d]:
    #         self.rot_speed = -PLAYER_ROT_SPEED
    #     if keys[pg.K_UP] or keys[pg.K_w]:
    #         self.vel = vec(PLAYER_ROT_SPEED, 0).rotate(-self.rot)
    #     if keys[pg.K_DOWN] or keys[pg.K_s]:
    #         self.vel = vec(-PLAYER_ROT_SPEED, 0).rotate(-self.rot)

    #get keys, pre-rotation controls   
    # "get keys allows the keys of a keyboard to be assigned a task"
    # "for this game, the keys WASD and the directional arrows control the direction of the player"
    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
    # "this chunk of code gives walls the ability to stop the player from passing through it"
    # "where there is a wall, this code prevents the player from passing through from any direction"
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

    def update(self):
        self.animate()
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        
        def animate(self): 
            now = pg.time.get_ticks()
            if not self.walking_back and self.walking_left and self.walking_right:
                if now - self.last_update > 350:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.walking_forward)   
                    self.image = self.standing_frame[self.current_frame]
    
        #pre-rotation updates
        # def update(self):
        # self.get_keys()
        # self.pos += self.vel * self.game.dt
        # self.rect.x = self.pos.x
        # self.collide_with_walls('x')
        # self.rect.y = self.pos.y
        # self.collide_with_walls('y')

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE