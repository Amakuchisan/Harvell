class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Block:
    def __init__(self, img_id):
        self.pos = Vec2(60, 90)
        self.img_player = img_id

    def update_floor(self, x, y):
        if (
            x <= self.pos.x+16
            and x >= self.pos.x-8
            and y == self.pos.y-11
        ):
            y = self.pos.y
        else:
            return True