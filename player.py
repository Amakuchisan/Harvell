class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, img_id):
        self.pos = Vec2(0, 100)
        self.img_player = img_id

    def update(self, x, y):
        self.pos.x += x
        self.pos.y += 0