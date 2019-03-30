from vec2 import Vec2
class Item:
    def __init__(self):
        img_id = 0
        self.img_item = img_id
        self.col = 0

    def update(self, dx):
        self.pos.x += dx

    def create(self, x, y):
        self.pos = Vec2(x, y)

    def get(self, x, y):
        if (
            self.pos.x-8 <= x <= self.pos.x+8
            and self.pos.y-8 <= y <= self.pos.y+8
        ):
            return True

    def color(self):
        return self.col

class Red(Item):
    def __init__(self):
        super().__init__()
        self.col = 8 # red