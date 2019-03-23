class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, img_id):
        self.IMG = 16
        self.PLAYER_W = 9
        self.pos = Vec2(0, 101)
        self.img_player = img_id

    def update(self, x):
        self.pos.x += x
        if x > 0:
            self.PLAYER_W = 9
        if x < 0:
            self.PLAYER_W = -9

    def jump(self, y):
        self.IMG = 26
        self.pos.y -= y

    def down(self, y):
        self.IMG = 35
        self.pos.y += y