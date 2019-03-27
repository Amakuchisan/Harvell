import pyxel
import player
import enemy
import item
import background

WINDOW_H = 120
WINDOW_W = 160
# PLAYER_W = 9
BLOCK_H = 8
BLOCK_W = 16

GROUND_BLOCK = 64
BLOCK1 = 65

#COLOR
RED = 8

class App:
    def __init__(self):
        self.IMG_PLAYER = 0
        self.IMG_BLOCK = 0
        self.IMG_ITEM = 0
        self.IMG_ENEMY = 1
        self.IMG_BACKGROUND = 0
        self.FLOOR = [GROUND_BLOCK, BLOCK1]

        self.count = 0

        pyxel.init(WINDOW_W, WINDOW_H, caption="Harvell")
        pyxel.load("assets/my_resource.pyxel")

        self.mplayer = player.Player(self.IMG_PLAYER)
        self.menemy = enemy.Enemy(self.IMG_ENEMY)
        self.background = background.Background(self.IMG_BACKGROUND)
        self.Items = []
        # add item
        self.new_item = item.Red()
        self.new_item.update(36, 100, RED)
        self.Items.append(self.new_item)

        pyxel.run(self.update, self.draw)

    def update(self):
        dx = 0
        # item
        # self.Items = []
        if pyxel.frame_count%5 == 0:
            self.menemy.update(self.menemy.pos.x)
        if pyxel.frame_count%100 == 0:
            if len(self.Items) == 0:
                self.Items.append(self.new_item)

        if pyxel.btnp(pyxel.KEY_Q):
            print() # to debug

        if pyxel.btn(pyxel.KEY_D):
            if pyxel.tilemap(0).get(int((self.mplayer.pos.x+1)/8), int((self.mplayer.pos.y)/8)) != BLOCK1:
            # if pyxel.tilemap(0).get(int((self.mplayer.pos.x+1)/8), int((self.mplayer.pos.y)/8)) not in self.FLOOR:
                dx = 1
        if pyxel.btn(pyxel.KEY_A):
            if pyxel.tilemap(0).get(int((self.mplayer.pos.x-1)/8), int((self.mplayer.pos.y)/8)) != BLOCK1 and self.mplayer.pos.x >= 1:
                dx = -1

        if pyxel.btn(pyxel.KEY_E):
            item_count = len(self.Items)
            if item_count:
                for i in range(item_count):
                    if self.Items[i].get(self.mplayer.pos.x, self.mplayer.pos.y):
                        pyxel.pal(self.mplayer.color(), self.Items[i].color())
                        self.mplayer.setcolor(self.Items[i].color())
                        del self.Items[i]
                        break

        if pyxel.btnp(pyxel.KEY_SPACE): # TODO:着地前のジャンプ対応
            self.mplayer.flag_jump_true()

        if self.mplayer.flag_jump:
            self.mplayer.jump(2)
            self.count += 1
            if self.count % 15 == 0 or ((self.mplayer.pos.y+1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x)/8), int((self.mplayer.pos.y)/8)) in self.FLOOR or (self.mplayer.pos.y+1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x+8)/8), int((self.mplayer.pos.y)/8)) in self.FLOOR):
                self.count = 0
                self.mplayer.flag_jump_false()
        else:
            if (self.mplayer.pos.y-1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x)/8), int((self.mplayer.pos.y+7)/8)) in self.FLOOR or (self.mplayer.pos.y-1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x+7)/8), int((self.mplayer.pos.y+7)/8)) in self.FLOOR:
                if pyxel.btn(pyxel.KEY_G):
                    print(self.mplayer.flag_jump)
                    print(pyxel.tilemap(0).get(int((self.mplayer.pos.x+4)/10), int((self.mplayer.pos.y+39)/10)))
                self.mplayer.normal()
            else:
                if pyxel.tilemap(0).get(int((self.mplayer.pos.x)/8), int((self.mplayer.pos.y+9)/8)) in self.FLOOR:
                    self.mplayer.normal()
                self.mplayer.down(1)
                if self.mplayer.pos.y > 130:
                    self.mplayer.pos.x = 0
                    self.mplayer.pos.y = 0

        self.mplayer.update(dx)

    def draw(self):
        pyxel.cls(0)

        # draw background
        # pyxel.bltm(self.mplayer.pos.x, 0, 0, 0, 0, 30, 16,) # how to scroll
        pyxel.bltm(self.background.pos.x, self.background.pos.y, self.IMG_BACKGROUND, 0, 0, 30, 16,)

        # draw item
        # pyxel.blt(self.item.pos.x, self.item.pos.y, self.IMG_ITEM, 16, 54, 8, 8, 11)
        for i in self.Items:
            pyxel.blt(i.pos.x, i.pos.y, self.IMG_ITEM, 16, 54, 8, 8, 11)

        # draw player
        pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, self.mplayer.IMG_X, self.mplayer.IMG_Y, self.mplayer.PLAYER_W, self.mplayer.PLAYER_H, 4) # small

        # draw enemy
        pyxel.blt(self.menemy.pos.x, self.menemy.pos.y, self.IMG_ENEMY, self.menemy.IMG_X, self.menemy.IMG_Y, self.menemy.ENEMY_W, self.menemy.ENEMY_H, 4)


if __name__ == "__main__":
    App()
