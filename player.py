import pyxel
class Player():
    def __init__(self, config):
        self.IMG_X, self.IMG_Y = config.img_player_point
        self.PLAYER_W = config.default_player_witdth
        self.PLAYER_H = config.default_player_heigh
        self.pos = config.default_player_pos
        self.img_player = config.img_player_id
        self.col = config.default_player_col
        self.flag_jump = False
        self.flag_landing = False

    def update(self, dx):
        self.pos.x += dx
        if dx > 0:
            self.PLAYER_W = 9
        if dx < 0:
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
        self.flag_landing = True

    def flag_jump_false(self):
        self.flag_jump = False

    def flag_landing_false(self):
        self.flag_landing = False

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
        self.flag_landing_false()

    def encount(self, color):
        if(color != self.col):
            self.dead()

    def dead(self):
        self.pos.x = 0
        self.pos.y = 40
        pyxel.pal()