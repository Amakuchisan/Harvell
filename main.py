import pyxel
import player
import enemy
import block
import item
import background

WINDOW_H = 120
WINDOW_W = 160
PLAYER_H = 11 # small is 7
PLAYER_pos_y = 5
# PLAYER_W = 9
BLOCK_H = 8
BLOCK_W = 16

GROUND_BLOCK = 64

#COLOR
RED = 8

class App:
    def __init__(self):
        self.IMG_PLAYER = 0
        self.IMG_BLOCK = 0
        self.IMG_ITEM = 0
        self.IMG_ENEMY = 1
        self.IMG_BACKGROUND = 0

        self.count = 0

        pyxel.init(WINDOW_W, WINDOW_H, caption="Harvell")
        pyxel.load("assets/my_resource.pyxel")

        self.mplayer = player.Player(self.IMG_PLAYER)
        self.menemy = enemy.Enemy(self.IMG_ENEMY)
        self.block = block.Block(self.IMG_BLOCK)
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
            print(int(self.mplayer.pos.x/10), int((self.mplayer.pos.y+40)/10))
            # print(pyxel.image(0).get(self.mplayer.pos.x, self.mplayer.pos.y))
            # print(pyxel.tilemap(0).get(4, 10))
            # print(pyxel.tilemap(0).get(4, 11))
            # print(pyxel.tilemap(0).get(4, 12))
            # print(pyxel.tilemap(0).get(4, 13))
            # print(pyxel.tilemap(0).get(4, 14))
            # print(pyxel.tilemap(0).get(4, 15))

        if pyxel.btn(pyxel.KEY_D):
            dx = 1
        if pyxel.btn(pyxel.KEY_A):
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

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.mplayer.flag_jump_true()

        if self.mplayer.flag_jump:
            self.mplayer.jump(2)
            self.count += 1
            if self.count % 13 == 0:
                self.count = 0
                self.mplayer.down(2)
        else:
            if pyxel.tilemap(0).get(int(self.mplayer.pos.x/10), int((self.mplayer.pos.y+40)/10)) != GROUND_BLOCK:
                self.mplayer.down(2)
            else:
                self.mplayer.IMG = 16 #!101or101, TODO

        self.mplayer.update(dx)

    def draw(self):
        pyxel.cls(0)

        # draw background
        # pyxel.bltm(self.mplayer.pos.x, 0, 0, 0, 0, 30, 16,) # how to scroll
        pyxel.bltm(self.background.pos.x, self.background.pos.y, self.IMG_BACKGROUND, 0, 0, 30, 16,)

        # draw block
        pyxel.blt(self.block.pos.x, self.block.pos.y, self.IMG_BLOCK, 16, 16, BLOCK_W, BLOCK_H, )

        # draw item
        # pyxel.blt(self.item.pos.x, self.item.pos.y, self.IMG_ITEM, 16, 54, 8, 8, 11)
        for i in self.Items:
            pyxel.blt(i.pos.x, i.pos.y, self.IMG_ITEM, 16, 54, 8, 8, 11)

        # draw player
        # pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, 0, 0, PLAYER_W, PLAYER_H, 4) # big
        pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, self.mplayer.IMG, PLAYER_pos_y, self.mplayer.PLAYER_W, PLAYER_H, 4) # small

        # draw enemy
        pyxel.blt(self.menemy.pos.x, self.menemy.pos.y, self.IMG_ENEMY, self.menemy.IMG_X, self.menemy.IMG_Y, self.menemy.ENEMY_W, self.menemy.ENEMY_H, 4)


if __name__ == "__main__":
    App()
