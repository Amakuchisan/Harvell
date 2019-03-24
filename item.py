class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Item:
    def __init__(self):
        img_id = 0
        self.img_player = img_id
        self.col = 0 # red

    def update(self, x, y, color):
        self.pos = Vec2(x, y)
        self.col = color

    def get(self, x, y):
        if (
            x <= self.pos.x+8
            and x >= self.pos.x-8
            and y <= self.pos.y+8
            and y >= self.pos.y-8
        ):
            return True

    def color(self):
        return self.col

class Red(Item):
    def __init__(self):
        super().__init__()
        self.item = 8 # red