#from car import Car
import sys
import random
import pygame
WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        pygame.draw.rect(self.image, self.color, [
                         0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [
                        0, 0, self.width, self.height])


pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

SCREENWIDTH = 800
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("F1賽車遊戲")

all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
car1.rect.x = 60
car1.rect.y = -100
car2 = Car(YELLOW, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = -600
car3 = Car(CYAN, 60, 80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = -300

car4 = Car(BLUE, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = -900

all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)
all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playerCar.moveRight(10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        speed += 0.05
    if keys[pygame.K_DOWN]:
        speed -= 0.05
    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > SCREENHEIGHT:
            car.changeSpeed(random.randint(50, 100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200
    all_sprites_list.update()

    screen.fill(GREEN)
    pygame.draw.rect(screen, GREY, [40, 0, 400, SCREENHEIGHT])
    pygame.draw.line(screen, WHITE, [140, 0], [140, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [240, 0], [240, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [340, 0], [340, SCREENHEIGHT], 5)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False) 
    for car in car_collision_list: 
        print("Car crash!")

