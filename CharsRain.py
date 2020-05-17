# -*- coding = utf-8 -*-

'''
准备资源：
    一个字体文件
使用库：
    random：用于随机字符
    pygame：用于创建窗口
思路：将窗口分列，绘制满屏的字符，字符每一帧向下一格，下一帧的时候用不透明蒙版覆盖
     创建一个蒙版不透明图像（用于覆盖上一帧的图像，设置透明度以起到字符渐透明的效果）
'''
import random
import pygame

PANEL_width = 600
PANEL_highly = 500
FONT_PX = 15

pygame.init()

# 初始化一个准备显示的窗口或屏幕
win = pygame.display.set_mode((PANEL_width, PANEL_highly))

# 根据给定的字体或系统字体创建窗口字体
font = pygame.font.SysFont("字体.ttf", 25)

# 创建图像
bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)

# 更改图像的像素格式
pygame.Surface.convert(bg_suface)

# 用纯色填充Surface
# pygame.Color(0, 0, 0, 28) r g b 透明度
bg_suface.fill(pygame.Color(0, 0, 0, 28))
win.fill((0, 0, 0))


chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
         'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

texts = [
    # 创建文本surface图像@来自pygame.font.SysFont.render  并将字体设置为绿色
    font.render(str(chars[i]), False, (0, 255, 0)) for i in range(26)   # for循环赋值用法
]

# 按屏幕的宽带计算可以在画板上放几列坐标并生成一个列表
column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]

while True:
    # 从队列中获取事件
    for event in pygame.event.get():
        # 退出界面
        if event.type == pygame.QUIT:
            exit()
        # 获取按键事件
        elif event.type == pygame.KEYDOWN:
            # 按键队列
            chang = pygame.key.get_pressed()
            if (chang[32]):  # 空格退出
                exit()

    # 将暂停30毫秒
    pygame.time.delay(30)

    # 重新编辑图像第二个参数是坐上角坐标
    win.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
        # 选择文本
        text = random.choice(texts)

        # 绘画text图像
        win.blit(text, (i * FONT_PX, drops[i] * FONT_PX))

        drops[i] += 1
        if drops[i] * 10 > PANEL_highly or random.random() > 0.95:
            drops[i] = 0

    # 更新帧到整个待显示的surface对象到屏幕上
    pygame.display.flip()
