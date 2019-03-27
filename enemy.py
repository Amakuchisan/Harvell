class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Enemy:
    def __init__(self, img_id):
        self.IMG_X = 1
        self.IMG_Y = 5
        self.ENEMY_W = 14
        self.ENEMY_H = 11
        self.col = 9
        self.pos = Vec2(50, 101)
        self.img_enemy = img_id

    def update(self, x):
        self.pos.x += 1
    
    def color(self):
        return self.col