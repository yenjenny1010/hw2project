from tkinter import *
import tkinter as tk
import random
name = ["1", "2", "3", "4"]
carcolor = ["#FFC0CB", "#800080", "#0000FF", "#008000", "#F5F5DC",
    "#FFFF00", "#FFD700", "#FFA500", "#FF0000", "#808080", "#000000"]
runwaycolor = ['floral white', 'old lace',
    "lemon chiffon", 'antique white', 'peach puff']


class RaceCar(Canvas):
    def __init__(self, master, width, height):
        Canvas.__init__(self, master, width=width, height=height)
        self["bg"] = "white"
        self.sleepTime = 100
        self.x = 10  # initial value
        self.y = 50  # initial value
        self.name = 1
        self.color = "white"
        self.color1 = "white"
        self.color2 = "white"
        self.color3 = "white"
        self.color4 = "white"
        # self.displayCar()

    def displayCar(self):
        self.delete("car")

        self.create_rectangle(0, 0, 800,  60, fill=self.color4, tags="car")
        self.create_line(720, 0, 720, 60)
        self.create_oval(self.x + 10, self.y - 10, self.x +
                         20,  self.y, fill=self.color, tags="car")
        self.create_oval(self.x + 30, self.y - 10, self.x +
                         40,  self.y, fill=self.color1, tags="car")
        self.create_rectangle(self.x, self.y - 20, self.x + 50,
                              self.y - 10, fill=self.color2, tags="car")
        self.create_polygon(self.x + 10, self.y - 20, self.x + 20,  self.y - 30,
                            self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill=self.color3, tags="car")

        """if self.x>=20:

            label = tk.Label(window,               # 文字標示所在視窗
                 text = 'Hello, world', tags="car")
            label.pack()     """

    def win(self):
        window1 = tk.Tk()
        window1.title('racecar')
        window1.geometry("300x100+250+150")
        label = tk.Label(window1,                 # 文字標示所在視窗
                         text=self.name )  # 顯示文字
        label1 = tk.Label(window1,                 # 文字標示所在視窗
                         text="win" )
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


running=1

def run():
    running=1
    while running:
        
        for car in cars:  # ？
            if car.x < 680:

                car.setcolor(carcolor[random.randrange(10)])
                car.setcolor1(carcolor[random.randrange(10)])
                car.setcolor2(carcolor[random.randrange(10)])
                car.setcolor3(carcolor[random.randrange(10)])
                car.setcolor4(carcolor[random.randrange(10)])
                car.displayCar()
                speed = random.randrange(35)
                car.x += speed
            else:
                car.win()
                running=False
            car.after(50)
            car.update()  # Sleep for 100 milliseconds
        car.update()
      
            
            

            # if car.x


class runway(Canvas):
    def __init__(self, master, width, height):
        Canvas.__init__(self, master, width=width, height=height)

    def displayrunway(self):
        self.create_rectangle(0, 0, 800,  30, fill="green", tags="runway")
        self.update()


window = Tk()  # Create a window
window.title("Racing Cars")  # Set a title
width = 800
height = 60

cars = []
runways = []
for i in range(4):
    runways.append(runway(window, width=width, height=height))
    cars.append(RaceCar(window, width=width, height=height))
    cars[i].setname(name[i])
    cars[i].setcolor(carcolor[random.randrange(10)])
    cars[i].setcolor1(carcolor[random.randrange(10)])
    cars[i].setcolor2(carcolor[random.randrange(10)])
    cars[i].setcolor3(carcolor[random.randrange(10)])
    cars[i].setcolor4(carcolor[random.randrange(10)])
    cars[i].pack()


def resetAll():
    running=True
    for car in cars:
        car.x = 10  # initial value
        car.y = 50
    run()
def stop():
    running=False
    
def keepgoing():
    running=True
DoThing = tk.Button(window, text='RESTART',command=resetAll)
mybutton2 = tk.Button(window, text='stop', command=stop)
mybutton3 = tk.Button(window, text='keep going', command=keepgoing)
mybutton2.pack(side=LEFT,padx=10, pady=10)
DoThing.pack(side=LEFT,padx=10, pady=10)   
mybutton3.pack(side=LEFT,padx=10, pady=10)

run()   

  # Create an event loop
window.mainloop()