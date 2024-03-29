import sys, pygame
from sys import exit
pygame.init()

size = width, height = 1200, 700
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode()
ball = pygame.image.load("ball_black.jpg")
ball = pygame.transform.scale(ball, (300, 200))
ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0  or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

pygame.quit()