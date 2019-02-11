import random
import pygame

# 命
MyPlaneLife = 1
# 屏幕大小
SCREEN_RECT = pygame.__rect_constructor(0, 0, 480, 700)
# 刷新频率
FRAME_PER_SEC = 60
FRAME_PER_SEC2 = 600
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹的定时器常量
FIRE_EVENT = pygame.USEREVENT + 1
# 鼠标点击事件常量
MOUSE_BUTTON_DOWN = pygame.USEREVENT + 2


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed_x=0, speed_y=1):
        """初始化

        :param image_name: 飞机图片
        :param speed_x: 飞机水平速度
        :param speed_y: 飞机竖直速度
        """
        # 引用父类的
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, *args):
        """更新

        :param args:
        """
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x


class Background(GameSprite):
    """创建游戏背景"""

    def __init__(self, is_alt=False):

        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 调用父类的方法实现
        super().update()

        # 判断是否移出屏幕，若移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class MainMenu(GameSprite):
    """创建主菜单"""

    def __init__(self):

        super().__init__("./images/again.png", 0, 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery


class Enemy(GameSprite):

    def __init__(self):

        super().__init__("./images/enemy1.png")

        self.speed_y = random.randint(1, 3)

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            # print("飞机飞出屏幕")

            self.kill()


class MyPlane(GameSprite):
    """我的飞机"""

    def __init__(self):

        # 调用父类方法，设置image&speed_x&speed_y
        super().__init__("./images/me1.png", 0, 0)

        # 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 60

        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def fire(self):

        bullet = Bullet()

        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        # bullet.rect.x = 20
        # bullet.rect.y = 20

        self.bullets.add(bullet)

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed_x
        # 英雄在竖直方向移动
        self.rect.y += self.speed_y
        if self.rect.x < -40:
            self.rect.x = -40
        elif self.rect.right > SCREEN_RECT.right + 40:
            self.rect.right = SCREEN_RECT.right + 40

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def __del__(self):

        print("gameover")


class Bullet(GameSprite):
    """子弹"""

    def __init__(self):

        super().__init__("./images/bullet1.png", 0, -2)

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()
