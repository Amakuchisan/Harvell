import pyxel
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player():
    def __init__(self, img_id):
        self.IMG_X = 16
        self.IMG_Y = 5
        self.PLAYER_W = 9
        self.PLAYER_H = 7 # big is 11
        self.pos = Vec2(0, 105)
        self.img_player = img_id
        self.col = 9
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