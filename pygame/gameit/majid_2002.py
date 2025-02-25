# JumpMan
# Created by Abdul Majid


#? The objective of the game is to jump through the blacks till the last block in the game
#* Use spacebar to jump and LEFT and RIGHT arrow keys to move through the screen

import pygame

def jumpMan():
    pygame.init()
    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("JumpMan by Majid")

    x = 45 #* position of character at the start of game x axis from 0 to 500
    y = 480 #* position of character at the start of game y axis from 0 to 500

    width = 20              #* width of the character

    speed = 2               #* speed of the character

    run = True
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed() 

        if keys[pygame.K_SPACE] and y > 0:  
            y -= speed

        if not keys[pygame.K_SPACE] and y < 480:
            y += speed

        if keys[pygame.K_RIGHT] and x < 480:
            x += speed

        if keys[pygame.K_LEFT] and x > 20:
            x -= speed

        win.fill((255, 255, 255))

        pygame.draw.circle(win, (255, 0, 0), [x, y], width, 2)
        pygame.draw.rect(win, (0, 0, 0), (25, 450, 40, 50))
        pygame.draw.rect(win, (0, 0, 0), (100, 375, 40, 125))
        pygame.draw.rect(win, (0, 0, 0), (200, 275, 40, 80))
        pygame.draw.rect(win, (0, 0, 0), (300, 305, 40, 105))
        pygame.draw.rect(win, (0, 0, 0), (400, 450, 40, 50))



        if not keys[pygame.K_SPACE] and x >= 25 and x <= 65: #? first box condition for character to change the position
            y = 430

        if not keys[pygame.K_SPACE] and x >= 100 and x <= 140: #? second box condition for character to change the position
            y = 355
        
        if not keys[pygame.K_SPACE] and x >= 200 and x <= 240: #? third box condition for character to change the position
            y = 255
        
        if not keys[pygame.K_SPACE] and x >= 300 and x <= 340: #? fourth box condition for character to change the position
            y = 285

        if not keys[pygame.K_SPACE] and x >= 400 and x <= 440: #? condition for character when it reached at the last block of the game
            y = 430
            print("You won the game !")
            pygame.quit()

        if y > 480: #? condition for character if doesnt't reach the last block or it fall from the block
            print("Game Over , Try Again!")
            pygame.quit()
        
        pygame.display.update()

    pygame.quit()

