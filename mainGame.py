import random
import pygame
from Ball import Ball
from paddle import Paddle
pygame.init()    


def game_over(ball):
    global paddle, score
    if ball.y >= paddle.y + ball.radius + 10:
        print('GAME is OVER!')
        print('Your score is : ', score)
        return True
    return False

def ball_hit_paddle(ball):
    global paddle, score
    if paddle.x <= ball.x <= paddle.x + paddle.width and ball.y+ball.radius >= paddle.y + 10:
        ball.dy *= -1
        score += 1
    return False

def ball_hits_Wall(ball):
    if ball.x < ball.radius or ball.x + ball.radius >= screen_width:
        return True
    return False

def ball_hits_Ceiling(ball):
    if ball.y <= ball.radius:
        return True
    return False





def main():
    while True:

        if game_over(ball):
            break
            pygame.quit()

        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        

        screen.fill(screen_color)
        ball.x += ball.dx
        ball.y += ball.dy
        ball.drawBall(screen, ball.x, ball.y)

        if ball_hits_Wall(ball):
            ball.dx *= -1
        
        if ball_hits_Ceiling(ball):
            ball.dy *= -1
                
        if ball_hit_paddle(ball):
            ball.x += ball.dx
            ball.y += ball.dy
        
        

        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_LEFT]:
            paddle.x -= paddle.dx
        
        if key_pressed[pygame.K_RIGHT]:
            paddle.x += paddle.dx



        if paddle.x <= 0:
            paddle.x = 0
        if paddle.x + paddle.width >= screen_width:
            paddle.x = screen_width - paddle.width

        paddle.drawPaddle(screen, paddle.x, paddle.y)
        pygame.display.update()






#---------------------------------------------SCREEN------------------------------------------------------

clock = pygame.time.Clock()     # time for frames
speed = 30                      # 30 frames 
screen_width = 500
screen_height = 700
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG GAME")

#-------------------------------------------------------------------------------------------------------------------

ball = Ball()
paddle = Paddle()
score = 0
#------------------------------------------------MAIN GAME LOOP-------------------------------------------------------------


main()
# for 