# -*- coding: utf-8 -*-
"""

"""
import pygame
import rooms
import constants as con
from player import Player 

 
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([con.SCREEN_HEIGHT, con.SCREEN_WIDTH])
 
    # Set the title of the window
    pygame.display.set_caption('Maze Runner')
 
    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    # Prepare the level rooms
    level_rooms = []
 
    room = rooms.Room1()
    level_rooms.append(room)
 
    room = rooms.Room2()
    level_rooms.append(room)
 
    room = rooms.Room3()
    level_rooms.append(room)
 
    current_room_no = 0
    current_room = level_rooms[current_room_no]
    player.level = current_room
 
    # The misc
    clock = pygame.time.Clock()    
    font = pygame.font.SysFont('Calibri', 25, True, False)    
 
    done = False
 
    
    # ---------- MAIN PROGRAM LOOP ---------- #
    while not done:
 
        # ---------- EVENT PROCESSING ---------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        # ---------- GAME LOGIC ---------- #
        player.move(current_room.wall_list)
 
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = level_rooms[current_room_no]
                player.level = current_room
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = level_rooms[current_room_no]
                player.level = current_room
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = level_rooms[current_room_no]
                player.level = current_room
                player.rect.x = 790
 
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = level_rooms[current_room_no]
                player.level = current_room
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = level_rooms[current_room_no]
                player.level = current_room
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = level_rooms[current_room_no]
                player.level = current_room
                player.rect.x = 0
 
        # ---------- DRAWING ---------- #
        screen.fill(con.BLACK)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        
        # Draw information
        
        
        text = font.render(("x={0} y={1} change_y={2:06.2f}".format(player.rect.x,
                            player.rect.y, player.change_y)), True, con.RED)
        screen.blit(text, [20, 20])
 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()