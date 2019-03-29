from vec2 import Vec2
class Background:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.img_background = img_id

    def update(self, dx):
        self.pos.x += dx