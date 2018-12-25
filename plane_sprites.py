import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 游戏刷新帧率
SEC = 60
# 飞机定时器常量
CREAT_ENEMY_TIME = pygame.USEREVENT
# 英雄发现子弹事件
Hero_FIRE = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
            :param image_name: 图像路径
            :param speed: 图像Y轴或者X轴每秒变化数量
    """
    def __init__(self, image_name, speed=1, upspeed=0):

        # 父类不是Object类，都需要调用父类的初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.upspeed = upspeed

    def update(self, *args):
        self.rect.y += self.speed


class BackGroud(GameSprite):
    """背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，并且制定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.随机制定敌机速度
        self.speed = random.randint(1, 3)
        # 3.随机制定敌机初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        # 1.调用父类方法，垂直向下飞行
        super().update()
        # 2.判断是否飞出屏幕，飞出则从敌机精灵组中删除，释放内存
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出，销毁")
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 创建英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):

        self.rect.x += self.speed
        self.rect.y += self.upspeed
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        print("she")
        for i in (0, 1):
            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i * 30
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("销毁子弹")
