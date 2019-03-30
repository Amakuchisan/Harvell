class Enemy:
    def __init__(self, config):
        self.pos = config.default_enemy_pos
        self.img_enemy = config.img_enemy_id
        self.col = config.default_enemy_col

    def update(self, dx):
        self.pos.x += dx

    def color(self):
        return self.col


# class Enemy1:
#     def __init__(self, config):

#         self.IMG_X, self.IMG_Y = config.img_enemy_point
#         self.ENEMY_W = config.default_enemy_witdth
#         self.ENEMY_H = config.default_enemy_heigh
#         self.img_enemy = config.img_enemy_id