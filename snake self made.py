import random

import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 255)
brown = (255, 0, 0)
blue = (0, 255, 0)

x1 = 400
y1 = 300

x_change = 0
y_change = 0

snake_block = 10
win_width = 800
win_height = 600

display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake by sarbocha")

game_over = False


def message(msg, color, ):
    print("YOu Lost")
score = 0
foodx = round(random.randrange(0, win_width - snake_block) / 10.0)*10.0
foody = round(random.randrange(0, win_width - snake_block) / 10.0)*10.0
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -10
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10

    if x1 >= win_width or y1 >= win_height:
        game_over = True
    x1 += x_change
    y1 += y_change

    if x1 == foodx or y1 == foody:
        score = score + 1
    display.fill(white)

    pygame.draw.rect(display, black, [x1, y1, 10, 10])
    pygame.draw.rect(display, blue, [foodx, foody, 10,10])
    time.sleep(0.11)

    pygame.display.update()
    time.sleep(0.11)
message("You Lost", blue)
print(score)
pygame.quit()
quit()
