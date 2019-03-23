import pyxel
import player

WINDOW_H = 120
WINDOW_W = 160
PLAYER_H = 7
PLAYER_W = 9

class App:
    def __init__(self):
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

        if pyxel.btn(pyxel.KEY_SPACE):
            self.mplayer.jump(1)
        elif self.mplayer.pos.y < 105: # 105 is initial height, player should be stop on block
            self.mplayer.jump(-2)

        self.mplayer.update(dx)

    def draw(self):
        pyxel.cls(0)

        # draw background
        # pyxel.bltm(self.mplayer.pos.x, 0, 0, 0, 0, 30, 16,) # how to scroll
        pyxel.bltm(0, 0, 0, 0, 0, 30, 16,)

        # draw player
        # pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, 0, 0, PLAYER_W, PLAYER_H, 4) # big
        pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, 16, 9, PLAYER_W, PLAYER_H, 4) # small

if __name__ == "__main__":
    App()
