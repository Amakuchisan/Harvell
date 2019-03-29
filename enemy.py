from vec2 import Vec2
class Enemy:
    def __init__(self, config):

        self.IMG_X, self.IMG_Y = config.img_enemy_point
        self.ENEMY_W = config.default_enemy_witdth
        self.ENEMY_H = config.default_enemy_heigh
        self.pos = config.default_enemy_pos
        self.img_enemy = config.img_enemy_id
        self.col = config.default_enemy_col

    def update(self, x):
        self.pos.x += 1

    def color(self):
        return self.col