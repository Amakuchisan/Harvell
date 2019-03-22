import pyxel
import player

WINDOW_H = 120
WINDOW_W = 160
PLAYER_H = 16
PLAYER_W = 16

class App:
    def __init__(self):
        self.IMG_ID0_X = 60
        self.IMG_ID0_Y = 65
        self.IMG_PLAYER = 0

        pyxel.init(WINDOW_W, WINDOW_H, caption="Harvell")
        pyxel.load("assets/my_resource.pyxel")

        self.mplayer = player.Player(self.IMG_PLAYER)

        pyxel.run(self.update, self.draw)

    def update(self):
        dx = 0
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_D):
            dx = 1
        if pyxel.btn(pyxel.KEY_A):
            dx = -1

        self.mplayer.update(dx, 0)

    def draw(self):
        pyxel.cls(0)
        # pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, 0, 0, PLAYER_W, PLAYER_H, 4) # big
        pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, 16, 0, PLAYER_W, PLAYER_H, 4) # small

if __name__ == "__main__":
    App()
