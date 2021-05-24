import pygame as pg
import random
import sys
import os
import time

pg.init()


class RaceCar:
    def __init__(self, x=0, y=0, displacement=0):  # set initial value
        self.sleepTime = 100
        self.x = x
        self.y = y
        self.displacement = displacement

    def displaycar(self,j):

        pg.draw.rect(bg, (255, j, 255), [0, self.y, 50, 30])

    def sety(self, y):
        self.y = y

    def setdisplacement(self, displacement):
        self.displacement = displacement

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getdisplacement(self):
        return self.displacement


car1 = RaceCar()
car2 = RaceCar()
car2.sety(135)
car3 = RaceCar
car4 = RaceCar


def paintrunway():
    #pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)

    pg.draw.rect(bg, (255, 222, 173), [0, 60, 800, 60])
    pg.draw.rect(bg, (238, 232, 170), [0, 120, 800, 60])
    pg.draw.rect(bg, (238, 0, 170), [0, 180, 800, 60])
    # pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
    pg.draw.rect(bg, (255, 160, 122), [0, 240, 800, 60])
    pg.draw.line(bg, (0, 0, 0), [720, 60], [720, 300], 2)


# 設定視窗
width, height = 800, 300  # 跑道800*60
pg.display.set_caption('Car Race')
screen = pg.display.set_mode((width, height))
# 建立畫布bg
pg.display.set_caption('Car Race')
bg = pg.Surface(screen.get_size())  # 跟screen一樣大
bg.fill((255, 255, 255))  # 畫布的顏色
# 顯示
paintrunway()
car1.displaycar(255)
car2.displaycar(0)
screen.blit(bg, (0, 0))  # (背景變數, 繪製位置)  #繪製覆蓋整個視窗
pg.display.update()  # 要更新繪圖視窗內容，才能顯示繪製的圖形，語法為

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()
