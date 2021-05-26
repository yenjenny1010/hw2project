"""import pygame
pygame.init()
screen = pygame.display.set_mode((640, 70))
pygame.display.set_caption("水平移動")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
ball = pygame.Surface((30,30)) #建立球矩形繪圖區
ball.fill((255,255,255)) #矩形區塊背景為白色
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0) #畫藍色球
rect1 = ball.get_rect() #取得球矩形區塊
rect1.center = (320,45) #球起始位置
x, y = rect1.topleft #球左上角坐標
dx = 3 #球運動速度
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30) #每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.blit(background, (0,0)) #清除繪圖視窗
        x += dx #改變水平位置
        rect1.center = (x,y)
    if(rect1.left <= 0 or rect1.right >= screen.get_width()): #到達左右邊界
        dx *= -1
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()"""
"""from tkinter import * # Import tkinter

class RaceCar(Canvas):
    def __init__(self, master, width, height):
        Canvas.__init__(self, master, width = width, height = height)
        self["bg"] = "white"
        self.sleepTime = 100
        self.x = 10
        self.y = 50
        #self.displayCar()
        #self.run()
        
    def displayCar(self):
        self.delete("car") 
    
        self.create_oval(self.x + 10, self.y - 10, self.x + 20,  self.y, fill = "black", tags = "car")
        self.create_oval(self.x + 30, self.y - 10, self.x + 40,  self.y, fill = "black", tags = "car")
        self.create_rectangle(self.x, self.y - 20, self.x + 50,  self.y - 10, fill = "green", tags = "car")
        self.create_polygon(self.x + 10, self.y - 20, self.x + 20,  self.y - 30, 
            self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill = "red", tags = "car")

def run():
    while True:
        for car in cars:
            if car.x < int(car["width"]):
                car.displayCar()
                car.x += 2
            else:
                car.x = 0
            
            car.after(50) # Sleep for 100 milliseconds
            car.update()
            
window = Tk() # Create a window
window.title("Racing Cars") # Set a title

width = 250
height = 48

cars = []
for i in range(4):
    cars.append(RaceCar(window, width = width, height = height))
    cars[i].pack()
run()

        
window.mainloop() # Create an event loop"""

"""import tkinter as tk
import random 
import time

 

window = tk.Tk() #視窗叫出
window.title('the car racing game')#視窗名稱
window.geometry('800x400') #視窗大小
window.resizable(False, False) #視窗改變大小(設定否)

class racecar():#類別車子
    def Canvas__init__(self,x=0,y=50):
        self["background"] = "white" #背景
        self.x=x
        self.y=y
        self.sleeptime=100
        #self.color=color
    
    def displaycar(self):#車子的顯示
        self.delete("car")
        
        self.create_oval(self.x + 10, self.y - 10, self.x + 20,  self.y, fill = "black", tags = "car")
        self.create_oval(self.x + 30, self.y - 10, self.x + 40,  self.y, fill = "black", tags = "car")
        self.create_rectangle(self.x, self.y - 20, self.x + 50,  self.y - 10, fill = "self.color", tags = "car")
        self.create_polygon(self.x + 10, self.y - 20, self.x + 20,  self.y - 30, 
            self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill = "red", tags = "car")
    
    def sety(self,y):
        self.y=y
    def gety(self):
        return self.y
    def setx(self,x):
        self.x=x
    def getx(self):
        return self.x
    def setcolor(self,color):
        self.color=color
    def getcolor(self):
        return self.color
    
    def carrun(self):
        while True:
            if self.x <= 720:
                self.displaycar()
                carspeed=random.randint(0, 15)
                self.x +=carspeed
                self.update()
            else:
                self.update()
                break
            
carA=racecar()
carA.sety(110)
carA.setcolor("pink")
carB=racecar()
carB.sety(170)
carB.setcolor("purple")
carC=racecar()
carC.sety(250)
carC.setcolor("cyan")
carD=racecar()
carD.sety(320)
carD.setcolor("green")

def runway():
    canvas.create_polygon(0,80, 0,140 ,800,80, 800,140, fill = "blue")
    Canvas.create_polygon(0,160, 0,220 ,800,160, 800,220, fill = "blue")
    Canvas.create_polygon(0,240, 0,300 ,800,240, 800,300, fill = "blue")
    Canvas.create_polygon(0,320, 0,380 ,800,320, 800,380, fill = "blue")
"""
#runway()
"""coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start=0, extent=150, fill="blue")"""
class Ball: 
    def __init__(self, canvas): 
     self.canvas = canvas 
     self.id = canvas.create_oval(10, 10, 25, 25, fill='red') 
     self.canvas.move(self.id, 25, 25) 
     self.x = 0 
     self.y = -1 
     self.canvas_height = self.canvas.winfo_height 
     self.canvas_width = self.canvas.winfo_width 