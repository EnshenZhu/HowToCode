import time

import pygame

pygame.init()
pygame.joystick.init()
done=False

while (done != True):
    time.sleep(3)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        axes = joystick.get_numaxes()
        print('================')
        for i in range(axes):
            axis = joystick.get_axis(i)
            print(axis)
# ————————————————
# 版权声明：本文为CSDN博主「怪皮蛇皮怪」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43958086/article/details/109139735
