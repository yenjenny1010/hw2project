from tkinter import *
import tkinter as tk
import random
import pygame
name = ["1", "2", "3", "4"]
carcolor = ["#FFC0CB", "#800080", "#0000FF", "#008000", "#F5F5DC",
            "#FFFF00", "#FFD700", "#FFA500", "#FF0000", "#808080", "#000000"]
runwaycolor = ['floral white', 'old lace',
               "lemon chiffon", 'antique white', 'peach puff']
running = False
width = 800
height = 60
cars = []
runways = []


class RaceCar(Canvas):
    def __init__(self, master, width, height):
        Canvas.__init__(self, master, width=width, height=height)
        self["bg"] = "white"
        self.sleepTime = 100
        self.x = 10  # initial value
        self.y = 50  # initial value
        self.name = 1
        self.color = "black"
        self.color1 = "black"
        self.color2 = "green"
        self.color3 = "red"
        self.color4 = "white"

    def displayCar(self):
        self.delete("car")
        self.create_rectangle(0, 0, 800,  60, fill=self.color4)
        self.create_line(720, 0, 720, 60)
        self.create_oval(self.x + 10, self.y - 10, self.x +
                         20,  self.y, fill=self.color, tags="car")
        self.create_oval(self.x + 30, self.y - 10, self.x +
                         40,  self.y, fill=self.color1, tags="car")
        self.create_rectangle(self.x, self.y - 20, self.x + 50,
                              self.y - 10, fill=self.color2, tags="car")
        self.create_polygon(self.x + 10, self.y - 20, self.x + 20,  self.y - 30,
                            self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill=self.color3, tags="car")
        self.create_text((self.x-10, self.y), text=self.name)
        
        
    def win(self):
        window1 = tk.Tk()
        window1.title('racecar')
        window1.geometry("300x100+250+150")
        # 文字標示所在視窗# 顯示文字
        label = tk.Label(window1, text=self.name)
        label1 = tk.Label(window1, text="win")
        
        label.pack()
        label1.pack()

    def setname(self, name):
        self.name = name

    def setcolor(self, color):
        self.color = color

    def setcolor1(self, color):
        self.color1 = color

    def setcolor2(self, color):
        self.color2 = color

    def setcolor3(self, color):
        self.color3 = color

    def setcolor4(self, color):
        self.color4 = color


def play():
    soundwav.play()


def play2():
    soundwav2.play()


def stopmusic():
    soundwav.stop()


def keepplaymusic():
    soundwav.unpause()


def run():
    for car in cars:  # ？
        car.displayCar()
    global running
    while running:
        
        for car in cars:  # ？
            car=cars[random.randrange(4)]
            if car.x < 670:
                car.setcolor(carcolor[random.randrange(10)])
                car.setcolor1(carcolor[random.randrange(10)])
                car.setcolor2(carcolor[random.randrange(10)])
                car.setcolor3(carcolor[random.randrange(10)])
                car.setcolor4(carcolor[random.randrange(10)])
                car.displayCar()
                speed = random.randrange(30)
                car.x += speed

            else:
                stopmusic()
                car.displayCar()
                car.win()
                running = False
                play2()
                break

            car.after(50)# Sleep for 10 milliseconds
            car.update()  
def start():
    stopmusic()
    global running
    running=True
    
    play()
    run()
    

def resetAll():
    stopmusic()
    
    global running
    running=False
    for car in cars:
        car.x = 10  # initial value
        car.y = 50
    run()


def stop():
    stopmusic()
    global running
    running = False

def addbutton():
    mybutton1 = tk.Button(window, text='Start', command=start)
    DoThing = tk.Button(window, text='RESTART', command=resetAll)
    mybutton2 = tk.Button(window, text='stop', command=stop)
    
    mybutton1.pack(side=LEFT, padx=10, pady=10)
    DoThing.pack(side=LEFT, padx=10, pady=10)
    mybutton2.pack(side=LEFT, padx=10, pady=10)
    


window = Tk()  # Create a window
window.title("Racing Cars")  # Set a title
pygame.init()
pygame.mixer.init()
soundwav = pygame.mixer.Sound("D:/大學/彰師大一下/程式設計/作業2/jenny's project/hw2project/1.mp3")  # filename.wav檔名
soundwav2 = pygame.mixer.Sound("D:/大學/彰師大一下/程式設計/作業2/jenny's project/hw2project/2.mp3")


for i in range(4):
    cars.append(RaceCar(window, width=width, height=height))
    cars[i].setname(name[i])
    #cars[i].setcolor(carcolor[random.randrange(10)])
    #cars[i].setcolor1(carcolor[random.randrange(10)])
    #cars[i].setcolor2(carcolor[random.randrange(10)])
    #cars[i].setcolor3(carcolor[random.randrange(10)])
    #cars[i].setcolor4(carcolor[random.randrange(10)])
    cars[i].pack()
    
    
addbutton()
run()

window.mainloop()  # Create an event loop
