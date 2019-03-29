import pyxel
from vec2 import Vec2

class Player():
    def __init__(self, config):
        self.IMG_X, self.IMG_Y = int(config['IMG_X']), int(config['IMG_Y'])
        self.PLAYER_W = int(config['default_player_witdth'])
        self.PLAYER_H = int(config['default_player_heigh'])
        self.pos = Vec2(int(config['default_player_pos_x']), int(config['default_player_pos_y']))
        self.img_player = int(config['img_id'])
        self.col = int(config['default_col'])
        self.flag_jump = False

    def update(self, x):
        self.pos.x += x
        if x > 0:
            self.PLAYER_W = 9
        if x < 0:
            self.PLAYER_W = -9

    def color(self):
        return self.col

    def setcolor(self, color):
        self.col = color # int
        return self.col

    def flag_jump_true(self):
        self.PLAYER_H = 11
        self.IMG_Y = 5
        self.flag_jump = True

    def flag_jump_false(self):
        self.flag_jump = False

    def jump(self, y):
        self.IMG_X = 26
        self.pos.y -= y

    def down(self, y):
        self.IMG_X = 35
        self.IMG_Y = 7
        self.pos.y += y
        self.PLAYER_H = 13

    def normal(self):
        self.IMG_X = 16
        self.IMG_Y = 5
        self.PLAYER_H = 7

    def encount(self, color):
        if(color != self.col):
            self.dead()

    def dead(self):
        self.pos.x = 0
        self.pos.y = 0
        pyxel.pal()