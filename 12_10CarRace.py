from tkinter import *  # Import tkinter
import random


class RaceCar(Canvas):
    def __init__(self, master, width, height):
        Canvas.__init__(self, master, width=width, height=height)
        self["bg"] = "white"
        self.sleepTime = 100
        self.x = 10  # initial value
        self.y = 50  # initial value
        self.name = 1
        self.color = "white"
        # self.displayCar()

    def displayCar(self):
        self.delete("car")
        self.create_oval(self.x + 10, self.y - 10, self.x +
                         20,  self.y, fill=self.color, tags="car")
        self.create_oval(self.x + 30, self.y - 10, self.x +
                         40,  self.y, fill="black", tags="car")
        self.create_rectangle(self.x, self.y - 20, self.x + 50,
                              self.y - 10, fill="green", tags="car")
        self.create_polygon(self.x + 10, self.y - 20, self.x + 20,  self.y - 30,
                            self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill="red", tags="car")

    def setname(self, name):
        self.name = name

    def setcolor(self, color):
        self.color = color


def run():
    while True:
        for car in cars:  # ？
            if car.x < int(car["width"]):
                car.displayCar()
                runway1.displayrunway()
                speed = random.randrange(20)
                car.x += speed
            else:
                car.x = 0

            car.after(50)  # Sleep for 100 milliseconds
            car.update()


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
    runway1 = runway(window, width=width, height=height)

    # runway1.displayrunway()
    cars[i].pack()

    # runway1.pack()

# set car's name
name = ["1", "2", "3", "4"]
for i in range(4):
    cars[i].setname(name[i])
    print(cars[i].name)

color=[]
run()
window.mainloop()  # Create an event loop

# 2怎麼重疊
