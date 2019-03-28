class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Background:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.img_background = img_id