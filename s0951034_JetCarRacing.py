from tkinter import *
import tkinter as tk
import random
import pygame
name = ["1", "2", "3", "4"]
color = ["#FF0000", "#003153", "#FF4D00", "#FFA500", "#7f00FF",
            "#FFD700", "#FFFF00", "#CCFF00", "#CCCCFF", "#FF00FF", "#007FFF","#0000FF","#7FFFD4","#E0FFFF","#F0F8FF","#30D5C8"]
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
                            self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill=self.color3, tags="car",outline="black")
        self.create_text((self.x, self.y), text=self.name, tags="car")

    def win(self):
        window1 = tk.Tk()
        window1.title('racecar')
        window1.geometry("300x100+250+150")
        # 文字標示所在視窗# 顯示文字
        label = tk.Label(window1, text=self.name)
        label1 = tk.Label(window1, text="win")
        label.pack()
        label1.pack()
        print(self.name,"win the game")

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
    for car in cars:  
        car.displayCar()
    global running
    while running:
        random.shuffle(cars)
        for car in cars:  
            if car.x < 670:
                car.setcolor(color[random.randrange(16)])
                car.setcolor1(color[random.randrange(16)])
                car.setcolor2(color[random.randrange(16)])
                car.setcolor3(color[random.randrange(16)])
                car.setcolor4(color[random.randrange(16)])
                car.displayCar()
                speed = random.randrange(60)
                speed/=2
                car.x +=speed
            else:
                stopmusic()
                play2()
                car.win()
                running = False
                for i in range(200):
                    car.displayCar()
                    car.setcolor(color[random.randrange(16)])
                    car.setcolor1(color[random.randrange(16)])
                    car.setcolor2(color[random.randrange(16)])
                    car.setcolor3(color[random.randrange(16)])
                    car.setcolor4(color[random.randrange(16)])
                    car.create_text((100, 30), text="WIN", tags="car",font=('Courier',40))
                    car.update()
                    car.after(1)
                break
            car.after(30)  # Sleep for 10 milliseconds
            car.update()


def start():
    stopmusic()
    global running
    if cars[0].x >= 670 or cars[1].x >= 670 or cars[2].x >= 670 or cars[3].x >= 670:
        running == False
    else:
        running = True
        play()
        run()


def resetAll():
    stopmusic()
    global running
    running = False
    for car in cars:
        car.x = 10  # initial value
        car.y = 50
    run()


def stop():
    stopmusic()
    global running
    running = False


def addbutton():
    mybutton1 = tk.Button(window, text='start', command=start)
    mybutton3 = tk.Button(window, text='restart', command=resetAll)
    mybutton2 = tk.Button(window, text='stop', command=stop)
    mybutton1.pack(side=LEFT, padx=10, pady=10)
    mybutton3.pack(side=LEFT, padx=10, pady=10)
    mybutton2.pack(side=LEFT, padx=10, pady=10)


window = Tk()  # Create a window
window.title("Racing Cars")  # Set a title
pygame.init()
pygame.mixer.init()
soundwav = pygame.mixer.Sound(
    "D:/大學/彰師大一下/程式設計/作業2/jenny's project/hw2project/1.mp3")  
soundwav2 = pygame.mixer.Sound(
    "D:/大學/彰師大一下/程式設計/作業2/jenny's project/hw2project/2.mp3")


for i in range(4):
    cars.append(RaceCar(window, width=width, height=height))
    cars[i].setname(name[i])
    # cars[i].setcolor(color[random.randrange(10)])
    # cars[i].setcolor1(color[random.randrange(10)])
    # cars[i].setcolor2(color[random.randrange(10)])
    # cars[i].setcolor3(color[random.randrange(10)])
    # cars[i].setcolor4(color[random.randrange(10)])
    cars[i].pack()


addbutton()
run()

window.mainloop()  # Create an event loop
