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
from tkinter import * # Import tkinter

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

        
window.mainloop() # Create an event loop
