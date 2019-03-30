import pyxel
from config import Config
import player
import enemy
import item
import background

WINDOW_H = 120
WINDOW_W = 160
BLOCK_H = 8
BLOCK_W = 16

ENEMY_R = 288
GROUND_BLOCK = 64
BLOCK_N = 65
BLOCK_I = 97 # !
BLOCK_B = 98 # bridge
BLOCK_G = 196
BLOCK_G_ = 197
GOAL = 7

class App:
    def __init__(self):
        self.IMG_PLAYER = 0
        self.IMG_BLOCK = 0
        self.IMG_ITEM = 0
        self.IMG_ENEMY = 1
        self.FLOOR = [GROUND_BLOCK, BLOCK_N, BLOCK_I, BLOCK_B, BLOCK_G, BLOCK_G_]
        self.config = Config()

        self.FLAG_GOAL = False
        self.count = 0
        self.count_background = 0
        self.count_enemy = 0

        pyxel.init(WINDOW_W, WINDOW_H, caption="Harvell")
        pyxel.load("assets/my_resource.pyxel")

        self.mplayer = player.Player(self.config)
        self.menemy = enemy.Enemy(self.config)
        self.background = background.Background(self.config)

        self.Items = []
        # add item
        self.new_item = item.Red()
        self.new_item.create(36, 100)
        self.Items.append(self.new_item)

        pyxel.run(self.update, self.draw)

    def update(self):
        dx = 0
        dx_background = 0
        # item
        # self.Items = []
        # if pyxel.frame_count%5 == 0:
        #     self.menemy.update(self.menemy.pos.x)

        if pyxel.frame_count%100 == 0:
            if len(self.Items) == 0:
                self.Items.append(self.new_item)

        if pyxel.btnp(pyxel.KEY_Q):
            # to debug
            print("0", pyxel.tilemap(0).get(int((self.mplayer.pos.x+1+self.count_background)/8), int((self.mplayer.pos.y)/8)))
            print("1", pyxel.tilemap(1).get(int((self.mplayer.pos.x+1+self.count_background)/8), int((self.mplayer.pos.y)/8)))

        if pyxel.btn(pyxel.KEY_D):
            if self.mplayer.pos.x > 100:
                dx_background = -1
                # dx_background -= 1
                self.count_background += 1
            elif pyxel.tilemap(0).get(int((self.mplayer.pos.x+1+self.count_background)/8), int((self.mplayer.pos.y)/8)) not in self.FLOOR:
            # elif pyxel.tilemap(0).get(int((self.mplayer.pos.x+1+self.count_background)/8), int((self.mplayer.pos.y)/8)) != BLOCK_N:
                dx = 1
        elif pyxel.btn(pyxel.KEY_A):
            if self.mplayer.pos.x < 9:
                dx_background = 1
                # dx_background += 1
                self.count_background -= 1
            elif pyxel.tilemap(0).get(int((self.mplayer.pos.x-1+self.count_background)/8), int((self.mplayer.pos.y)/8)) not in self.FLOOR and self.mplayer.pos.x >= 1:
            # elif pyxel.tilemap(0).get(int((self.mplayer.pos.x-1+self.count_background)/8), int((self.mplayer.pos.y)/8)) != BLOCK_N and self.mplayer.pos.x >= 1:
                dx = -1

        if pyxel.frame_count%10 == 0: # Enemyが動くように
            self.menemy.update(1-dx_background)
            self.count_enemy += 1
            self.menemy.update(dx_background)
            pyxel.cls(3)

        if pyxel.btn(pyxel.KEY_E):
            item_count = len(self.Items)
            if item_count:
                for i in range(item_count):
                    if self.Items[i].get(self.mplayer.pos.x, self.mplayer.pos.y):
                        pyxel.pal(self.mplayer.color(), self.Items[i].color())
                        self.mplayer.setcolor(self.Items[i].color())
                        del self.Items[i]
                        break

        if self.mplayer.flag_landing == False and pyxel.btnp(pyxel.KEY_SPACE): # TODO:着地前のジャンプ対応
            self.mplayer.flag_jump_true()

        if self.mplayer.flag_jump:
            self.mplayer.jump(2)
            self.count += 1
            if (
                self.count % 15 == 0 or ((self.mplayer.pos.y+1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x+self.count_background)/8), int((self.mplayer.pos.y)/8)) in self.FLOOR
                or (self.mplayer.pos.y+1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x+8+self.count_background)/8), int((self.mplayer.pos.y)/8)) in self.FLOOR)
            ):
                self.count = 0
                self.mplayer.flag_jump_false()
                # とりあえず[!]を叩くと橋がかかるようなギミックを
                if (
                    (self.mplayer.pos.y+1)%8 == 0
                    and pyxel.tilemap(0).get(int((self.mplayer.pos.x+4+self.count_background)/8), int((self.mplayer.pos.y)/8)) == BLOCK_I
                ):
                    pyxel.tilemap(0).set(8, 14, 98, 0)
                    pyxel.tilemap(0).set(9, 14, 98, 0)
                    pyxel.tilemap(0).set(10, 14, 98, 0)
        else:
            # ブロックに当たった時の処理を良い感じにしたいが……
            if (
                (self.mplayer.pos.y-1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x+self.count_background)/8), int((self.mplayer.pos.y+7)/8)) in self.FLOOR
                or (self.mplayer.pos.y-1)%8 == 0 and pyxel.tilemap(0).get(int((self.mplayer.pos.x+7+self.count_background)/8), int((self.mplayer.pos.y+7)/8)) in self.FLOOR
            ):
                self.mplayer.normal()
            else:
                if pyxel.tilemap(0).get(int((self.mplayer.pos.x+self.count_background)/8), int((self.mplayer.pos.y+9)/8)) in self.FLOOR:
                    # 着地する直前にやらないとめり込んで見えたことによる、場当たり的対策のif文
                    self.mplayer.normal()
                self.mplayer.down(1)
                if self.mplayer.pos.y > 130:
                    self.mplayer.dead()
        # GOAL
        if (pyxel.tilemap(0).get(int((self.mplayer.pos.x+7+self.count_background)/8), int((self.mplayer.pos.y)/8)) == GOAL):
            self.FLAG_GOAL = True

        if (
            pyxel.tilemap(1).get(int((self.mplayer.pos.x+4-self.count_enemy+self.count_background)/8), int((self.mplayer.pos.y+3)/8)) == ENEMY_R
        ):
            self.mplayer.encount(self.menemy.color())

        if self.FLAG_GOAL == True:
            self.goal(self.mplayer.pos.x)

        self.mplayer.update(dx)
        self.new_item.update(dx_background)
        self.background.update(dx_background)
        self.menemy.update(dx_background)

    def draw(self):
        pyxel.cls(3)

        # draw background
        # pyxel.bltm(self.mplayer.pos.x, 0, 0, 0, 0, 30, 16,)
        pyxel.bltm(self.background.pos.x, self.background.pos.y, self.background.img_background, 0, 0, 56, 16, 0)

        # draw item
        # pyxel.blt(self.item.pos.x, self.item.pos.y, self.IMG_ITEM, 16, 54, 8, 8, 11)
        for i in self.Items:
            pyxel.blt(i.pos.x, i.pos.y, self.IMG_ITEM, 16, 54, 8, 8, 11)

        # draw player
        pyxel.blt(self.mplayer.pos.x, self.mplayer.pos.y, self.IMG_PLAYER, self.mplayer.IMG_X, self.mplayer.IMG_Y, self.mplayer.PLAYER_W, self.mplayer.PLAYER_H, 4) # small

        # draw enemy
        pyxel.bltm(self.menemy.pos.x, self.menemy.pos.y, self.menemy.img_enemy, 0, 0, 30, 16, 4)
        # pyxel.blt(self.menemy.pos.x, self.menemy.pos.y, self.IMG_ENEMY, self.menemy.IMG_X, self.menemy.IMG_Y, self.menemy.ENEMY_W, self.menemy.ENEMY_H, 4)

    def goal(self, x):
        if self.mplayer.pos.y < 100:
            self.mplayer.pos.y += 1
        elif self.mplayer.pos.x < x+10:
            self.mplayer.pos.x += 1

if __name__ == "__main__":
    App()
