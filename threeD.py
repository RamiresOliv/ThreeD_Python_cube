import pygame
import numpy as np
from math import *

center = None

# cubie 👌:pinched_fingers:

class ThreeD:
    def __init__(self):
        print("threeD module loaded ;)")
        #self.center = pygame.Vector2(display.get_width() / 2, display.get_length() / 2)

    def Make(self, obj, settings):
        print("new obj created:")

        sendMatrixed = []

        if type(obj[0]) == np.matrix:
            print(obj)
            sendMatrixed = obj
        else:
            for value in obj:
                trueValue = (value[0], value[1], value[2])
                print(trueValue)
                sendMatrixed.append(np.matrix(trueValue))

        return sendMatrixed


    def Next(self, cube_matrix, projection_matrix, angle, rotation_matrix):
        if type(rotation_matrix) == dict:
            self.current_cube_rotation_matrix = rotation_matrix
        elif type(rotation_matrix) == list:
            x,y,z = rotation_matrix[0], rotation_matrix[1], rotation_matrix[2]

            if type(x) == list:
                x = x
            else:
                x = [0, 0, x]
            if type(y) == list:
                y = y
            else:
                y = [y, 0, 0]
            if type(z) == list:
                z = z
            else:
                z = [0, z, 0]
            self.current_cube_rotation_matrix = {
                # [0, 0, 0] format: X, Y, Z then matrixes need fit.
                "x": np.matrix([
                    [cos(angle), -sin(angle), 0],
                    [sin(angle), cos(angle), 0],
                    x,
                ]),
                "y": np.matrix([
                    y,
                    [0, cos(angle), -sin(angle)],
                    [0, sin(angle), cos(angle)],
                ]),
                "z": np.matrix([
                    [cos(angle), 0, sin(angle)],
                    z,
                    [-sin(angle), 0, cos(angle)],
                ]),
            }
        else:
            self.current_cube_rotation_matrix = {
                "x": np.matrix([
                    [cos(angle), -sin(angle), 0],
                    [sin(angle), cos(angle), 0],
                    [0, 0, 1],
                ]),
                "y": np.matrix([
                    [1, 0, 0],
                    [0, cos(angle), -sin(angle)],
                    [0, sin(angle), cos(angle)],
                ]),
                "z": np.matrix([
                    [cos(angle), 0, sin(angle)],
                    [0, 1, 0],
                    [-sin(angle), 0, cos(angle)],
                ]),
            }

        self.current_cube_matrix = cube_matrix

        self.current_projection_matrix = projection_matrix

    def twoD(self, point, options):
        rotated2D_x = np.dot(self.current_cube_rotation_matrix["x"], point.reshape((3, 1)))
        rotated2D_y = np.dot(self.current_cube_rotation_matrix["y"], rotated2D_x)
        rotated2D_z = np.dot(self.current_cube_rotation_matrix["z"], rotated2D_y)

        projected2D = np.dot(self.current_projection_matrix, rotated2D_z)

        x = int(projected2D[0][0] * options["scale"]) + options["startPos"][0]
        y = int(projected2D[1][0] * options["scale"])+ options["startPos"][1]

        result = (x, y) = x, y
        return result