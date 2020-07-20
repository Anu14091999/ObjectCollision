import time
import pygame
import random
import math

pygame.init()

width = 900
height = 650

obj_width = 43

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Object Crash")
clock = pygame.time.Clock()


objectimg = pygame.image.load("standing.png")

GameIcon = pygame.image.load("IconGame.png")
pygame.display.set_icon(GameIcon)

pause = False

    # for counting the score

def score(count):
    font = pygame.font.SysFont("comicsansms", 20)
    disp = font.render("Score:" +str(count), True, (255, 255, 255))
    win.blit(disp, (450, 5))

    # for drawing the object

def obj(objx, objy, objw, objh, color):
    pygame.draw.rect(win, color, [objx, objy, objw, objh])

def imgobj(x, y):
    win.blit(objectimg, (int(x), int(y)))

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 255))
    return textSurface, textSurface.get_rect()

    # when there is a collision between objects

def collide():
    largeText = pygame.font.SysFont('freesansbold.ttf', 120)
    TextSurf, TextRect = text_objects("Crashed", largeText)
    TextRect.center = ((width // 2), (height // 2))
    win.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        button("Play Again!", 250, 450, 50, (0, 255, 0), gameLoop)
        button("Quit", 650, 450, 50, (255, 0, 0), quitGame)

        pygame.display.update()
        clock.tick(15)

    # for creating buttons for different actions

def button(msg, x1, y1, r, color1, action=None):

    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if (math.sqrt(((pos[0] - x1) ** 2) + ((pos[1] - y1) ** 2)) < r):
        if click[0] == 1 and action != None:
            action()
    pygame.draw.circle(win, color1, (x1, y1), r)

    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (((x1 - 25) + (r // 2)), ((y1 - 25) + (r // 2)))
    win.blit(TextSurf, TextRect)

def quitGame():
    pygame.quit()
    quit()

def resume():
    global pause
    pause = False

def paused():
    largeText = pygame.font.Font('freesansbold.ttf', 120)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((width // 2), (height // 2))
    win.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        button("Resume", 250, 450, 50, (0, 255, 0), resume)
        button("Quit", 650, 450, 50, (255, 0, 0), quitGame)


        pygame.display.update()
        clock.tick(10)

def start():
    st = True
    while st:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        win.fill((0, 0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 120)
        TextSurf, TextRect = text_objects("Crash Object", largeText)
        TextRect.center = ((width // 2), (height // 2))
        win.blit(TextSurf, TextRect)

        button("Play", 250, 450, 50, (0, 255, 0), gameLoop)
        button("Quit", 650, 450, 50, (255, 0, 0), quitGame)


        pygame.display.update()
        clock.tick(10)

def gameLoop():
    global pause

    x = width * 0.5
    y = height * 0.87

    newX = 0

    obj_x = random.randrange(0, width)
    obj_y = -650
    obj_speed = 5
    obj_w = 60
    obj_h = 60

    objc = 0

    Score = 0

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    newX = -5
                if event.key == pygame.K_RIGHT:
                    newX = 5

                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    newX = 0

        x += newX

        win.fill((0, 0, 0))

        obj(obj_x, obj_y, obj_w, obj_h, (0, 255, 0))
        obj_y += obj_speed
        imgobj(x, y)

        score(Score)

        if x > width - obj_width or x < 0:
            collide()

        if obj_y > height:
            obj_y = 0 - obj_h
            obj_x = random.randrange(0, width)
            Score += 1
            obj_speed += 0.5

        if y < obj_y + obj_h:

            if x > obj_x and x < obj_x + obj_w or x + obj_width > obj_x and x + obj_width < obj_x + obj_w:
                collide()

        pygame.display.update()
        clock.tick(60)
start()
gameLoop()
quitGame()