import pygame
import threeD as ThreeD
import numpy as np
from math import *
import sys

TD = ThreeD.ThreeD()

# only pure pythom. Creating a 3D cube and with math transform it in 2D, for pygame print it ;)

size = (width, height) = 800, 600
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A 3D cube in python.")

scale = 100 # the size of the 2D printed cube
theme = "dark" # dark or white
screenCenter = [screen.get_width()/2, screen.get_height()/2] #x, y

# making the 3D cube:
points = []
points.append(np.matrix([-1, 1, -1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([1, 1, -1]))

points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, -1, -1]))

# bottom
#points.append(np.matrix([-1, -1, 1]))
#points.append(np.matrix([1, -1, 1]))
#points.append(np.matrix([1, 1, 1]))
#points.append(np.matrix([-1, 1, 1]))

# top:
#points.append(np.matrix([0, 0, -1]))
print(TD.Make(points,{
    "a":"a",
    "CanLogs": True
}))
points = TD.Make([
    [-1, 1, -1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, 1, -1],

    [-1, -1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, -1, -1],
], {
    "a":"a",
    "CanLogs": True
}) # "cube", [array with the x,y,z], [array with all the matrix already maded.]
print(points)
# how will project?
projected_points = []
for i in range(len(points)):
    projected_points.append([i, i])

def connect_points(i, j, points):
    color = "white"
    if theme == "white": color = "black"
    pygame.draw.line(screen, color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

angle = 0
while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            if theme == "white":
                theme = "dark"
            else:
                theme = "white"

    # update stuff
    TD.Next(points, np.matrix([[1, 0, 0],[0, 1, 0]]), angle, [1, 1, 1])
    angle += .01

    # draw stuff
    if theme == "white":
        screen.fill("white")
    else:
        screen.fill("black")

    toRenderPoints = []
    render_line_index = 0
    for point in points:
        result = TD.twoD(point, { "scale": 100, "startPos": screenCenter })
        x, y = result[0], result[1]

        projected_points[render_line_index] = [x,y]
        toRenderPoints.append((x,y))
        render_line_index += 1

    pointsHalf = floor(len(points)/2)
    if pointsHalf % 2 != 0:
        pointsHalf = 4
    for point in range(pointsHalf):
        connect_points(point, (point+1)%4, projected_points)
        connect_points(point+4, ((point+1)%4)+4, projected_points)
        connect_points(point, (point+4), projected_points)

    for axys in toRenderPoints:
        color = "grey"
        if toRenderPoints.index(axys) < pointsHalf:
            color = "green"
        pygame.draw.circle(screen, color, axys, 4)

    # render stuff
    pygame.display.update()