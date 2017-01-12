# -*- coding: utf-8 -*-
"""

"""
import pygame
from walls import Wall
import constants as con

class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        
        # Make the walls. (x_pos, y_pos, width, height) 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, con.WHITE],
                 [0, 350, 20, 250, con.WHITE],
                 [780, 0, 20, 250, con.WHITE],
                 [780, 350, 20, 250, con.WHITE],
                 [20, 0, 760, 20, con.WHITE],
                 [20, 580, 760, 20, con.WHITE],
                 [20, 540, 740, 20, con.WHITE],
                 [390, 50, 20, 500, con.BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, con.RED],
                 [0, 350, 20, 250, con.RED],
                 [780, 0, 20, 250, con.RED],
                 [780, 350, 20, 250, con.RED],
                 [20, 0, 760, 20, con.RED],
                 [20, 580, 760, 20, con.RED],
                 [190, 50, 20, 500, con.GREEN],
                 [590, 50, 20, 500, con.GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, con.PURPLE],
                 [0, 350, 20, 250, con.PURPLE],
                 [780, 0, 20, 250, con.PURPLE],
                 [780, 350, 20, 250, con.PURPLE],
                 [20, 0, 760, 20, con.PURPLE],
                 [20, 580, 760, 20, con.PURPLE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, con.RED)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, con.WHITE)
            self.wall_list.add(wall)