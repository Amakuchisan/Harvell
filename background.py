class Background:
    def __init__(self, config):
        self.pos = config.default_background_pos
        self.img_background = config.img_background_id

    def update(self, dx):
        self.pos.x += dx