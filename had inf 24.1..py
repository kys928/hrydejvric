import time

import pygame
import random
import numpy as np

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

c = list(np.random.choice(range(255), size=3))
l = ''
clicked = ''

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

dis.fill(black)

font_style = pygame.font.SysFont("monoscript", 60)
score_font = pygame.font.SysFont("monoscript", 35)
textTBD = pygame.font.SysFont("monoscript", 25)

running = True

while running:
    mesg = font_style.render("EDUSNAKE", True, white)
    dis.blit(mesg, (185, 180))
    mesg = textTBD.render("Press Space to Continue", True, white)
    dis.blit(mesg, (225, 225))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while running:
                    dis.fill(c)
                    mesg = font_style.render("Farba zeleného melónu zvnútra?", True, white)
                    dis.blit(mesg, (10, 100))
                    d = pygame.draw.rect(dis, red, [75, 250, 50, 50])
                    k = pygame.draw.rect(dis, blue, [275, 250, 50, 50])
                    o = pygame.draw.rect(dis, green, [475, 250, 50, 50])
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if d.collidepoint(event.pos):
                                dis.fill(black)
                                mesg = textTBD.render("Well done", True, white)
                                dis.blit(mesg, (150, 200))
                                pygame.display.update()

                                while running:
                                    dis.fill(c)
                                    mesg = font_style.render("Choose Your Snake Colour", True, white)
                                    dis.blit(mesg, (30, 50))
                                    r = pygame.draw.rect(dis, red, [75, 250, 50, 50])
                                    b = pygame.draw.rect(dis, blue, [275, 250, 50, 50])
                                    g = pygame.draw.rect(dis, green, [475, 250, 50, 50])
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            if r.collidepoint(event.pos):
                                                l = red

                                            if b.collidepoint(event.pos):
                                                l = blue

                                            if g.collidepoint(event.pos):
                                                l = green

                                            clock = pygame.time.Clock()

                                            snake_block = 10
                                            snake_speed = 10


                                            def Your_score(score):
                                                value = score_font.render("Your Score: " + str(score), True, white)
                                                dis.blit(value, [0, 0])


                                            def our_snake(snake_block, snake_list):
                                                for x in snake_list:
                                                    pygame.draw.rect(dis, l, [x[0], x[1], snake_block, snake_block])


                                            def message(msg, color):
                                                mesg = font_style.render(msg, True, color)
                                                dis.blit(mesg, (240, 170))


                                            def paused():

                                                pause = True

                                                while pause:
                                                    for event in pygame.event.get():

                                                        if event.type == pygame.QUIT:
                                                            pygame.quit()
                                                            quit()

                                                        if event.type == pygame.KEYDOWN:
                                                            if event.key == pygame.K_c:
                                                                pause = False

                                                            elif event.key == pygame.K_q:
                                                                pygame.quit()
                                                                quit()


                                            def gameLoop():
                                                game_over = False
                                                game_close = False

                                                x1 = 300
                                                y1 = 200
                                                snake_speed = 10

                                                x1_change = 0
                                                y1_change = 0

                                                snake_List = []
                                                Length_of_snake = 1

                                                foodx = round(
                                                    random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                                                foody = round(
                                                    random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

                                                while not game_over:

                                                    while game_close == True:
                                                        dis.fill(black)
                                                        mesg = font_style.render("Game Over", True, white)
                                                        dis.blit(mesg, (185, 180))
                                                        mesg = textTBD.render("Press Space to Play Again", True, white)
                                                        dis.blit(mesg, (190, 225))
                                                        Your_score(Length_of_snake - 1)
                                                        pygame.display.update()

                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                                if event.key == pygame.K_ESCAPE:
                                                                    game_over = True
                                                                    game_close = False
                                                                if event.key == pygame.K_SPACE:
                                                                    gameLoop()

                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            game_over = True
                                                        if event.type == pygame.KEYDOWN:
                                                            if event.key == pygame.K_a:
                                                                x1_change = -snake_block
                                                                y1_change = 0
                                                            elif event.key == pygame.K_d:
                                                                x1_change = snake_block
                                                                y1_change = 0
                                                            elif event.key == pygame.K_w:
                                                                y1_change = -snake_block
                                                                x1_change = 0
                                                            elif event.key == pygame.K_s:
                                                                y1_change = snake_block
                                                                x1_change = 0
                                                            elif event.key == pygame.K_p:
                                                                paused()

                                                    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                                                        game_close = True
                                                    x1 += x1_change
                                                    y1 += y1_change
                                                    dis.fill(c)
                                                    pygame.draw.rect(dis, white,
                                                                     [foodx, foody, snake_block, snake_block])
                                                    snake_Head = []
                                                    snake_Head.append(x1)
                                                    snake_Head.append(y1)
                                                    snake_List.append(snake_Head)
                                                    if len(snake_List) > Length_of_snake:
                                                        del snake_List[0]

                                                    for x in snake_List[:-1]:
                                                        if x == snake_Head:
                                                            game_close = True

                                                    our_snake(snake_block, snake_List)
                                                    Your_score(Length_of_snake - 1)

                                                    pygame.display.update()

                                                    if x1 == foodx and y1 == foody:
                                                        foodx = round(
                                                            random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                                                        foody = round(
                                                            random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

                                                        Length_of_snake += 1
                                                        snake_speed += 1

                                                    clock.tick(snake_speed)

                                                pygame.quit()
                                                quit()


                                            gameLoop()