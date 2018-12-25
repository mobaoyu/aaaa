import pygame
from plane_sprites import *
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load('./images/background.png')
# 2.游戏窗口blit绘制图像
screen.blit(bg, (0, 0))
# 3.更新窗口

# 绘制英雄飞机
# 1.加载图像数据
hero = pygame.image.load('./images/me1.png')
# 2.游戏窗口blit绘制图像
screen.blit(hero, (150, 500))
# 3.更新窗口
pygame.display.update()
# 创建游戏时钟对象
clock = pygame.time.Clock()
# 记录英雄初始化位置
hero_rect = pygame.Rect(150, 500, 102, 126)
# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)
i = 0
while True:
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 卸载pygame模块
            pygame.quit()
            # exit终止当前正在执行的程序，break只是退出当前循环
            exit()
    # 修改飞机位置
    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用更新和绘图方法
    enemy_group.update()

    enemy_group.draw(screen)
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    pygame.display.update()

pygame.quit()
