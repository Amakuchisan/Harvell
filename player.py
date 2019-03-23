class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, img_id):
        self.pos = Vec2(0, 105)
        self.img_player = img_id

    def update(self, x):
        self.pos.x += x

    def jump(self, y):
        self.pos.y -= y