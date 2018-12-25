import pygame
from plane_sprites import *


class PlaneGame:
    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.创建私有方法，调用该方法创建精灵和精灵组
        self.creat_sprites()
        # 4.设置定时器事件
        pygame.time.set_timer(CREAT_ENEMY_TIME, 1000)
        pygame.time.set_timer(Hero_FIRE, 500)

    def creat_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = BackGroud()
        bg2 = BackGroud(is_alt=True)

        self.back_groud = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组，敌机精灵在监听到定时器事件时再创建并且添加到精灵组中
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄和英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # 1.设置刷新帧率
            self.clock.tick(SEC)
            # 2.事件监听
            self.__even_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新绘制精灵组
            self.__update_sprites()
            # 5.更新屏幕显示
            pygame.display.update()
            pass
        print("开始游戏")

    def __even_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_TIME:
                print("敌机出场")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == Hero_FIRE:
                self.hero.fire()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
            print("right")
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif key_pressed[pygame.K_UP]:
            self.hero.upspeed = -2
        elif key_pressed[pygame.K_DOWN]:
            self.hero.upspeed = 2
        else:
            self.hero.speed = 0
            self.hero.upspeed = 0

    def __check_collide(self):
        # 子弹碰撞检测
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 敌机碰撞英雄检测
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        if len(enemies):
            self.hero.kill()
            print("英雄牺牲")
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_groud.update()
        self.back_groud.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)


    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    pg = PlaneGame()
    pg.start_game()
