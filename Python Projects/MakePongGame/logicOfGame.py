import pygame
pygame.init()
width,height=700,500
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong Game By Valeska")
fps=60 #frames per sec
white=(255,255,255)
black=(0,0,0)
paddleWigth,paddleHeight=100,20
ball_radius=7

class Paddle:
    color=white
    vel=4
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self ,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.height,self.width))
    def move(self,up=True):
        if up:
            self.y-=self.vel
        else:
            self.y+=self.vel
    
class Ball:
    max_vel=5
    color=white

    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.x_vel=self.max_vel
        self.y_vel=0
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    def move(self):
        self.x +=self.x_vel
        self.y +=self.y_vel

def draw (win,paddles,ball):
    win.fill(black)
    for paddle in paddles :
        paddle.draw(win)

    for i in range (10, height+1,height//20):
        if i % 2 ==1:
            continue
        pygame.draw.rect(win,white,(width //2-5 ,i,10,height//20))  #did not understand this parat
    ball.draw(win)
    pygame.display.update()

def handle_collision(ball,left_paddle,right_paddle):
    if ball.y +ball.radius >= height:
        ball.y_vel *=-1
    elif ball.y-ball_radius<=0:
        ball.y_vel *=-1
    
    if ball.x_vel<0:
        if ball.y>= left_paddle.y and ball.y <= left_paddle.y +left_paddle.height:
            if ball.x-ball_radius<=left_paddle.x +left_paddle.width:
                ball.x_vel *=-1
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x +ball.radius >=right_paddle.x:
                ball.x_vel*=-1

def handle_paddle_movement(keys,left_paddle,right_paddle):
    if keys[pygame.K_w] and left_paddle.y -left_paddle.vel >=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.vel + left_paddle.height <=height:
        left_paddle.move(up=False)
    if keys[pygame.K_UP]and right_paddle.y - right_paddle.vel >=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.vel + right_paddle.height <=height:
        right_paddle.move(up=False)


def main():
    run=True
    clock=pygame.time.Clock()

    left_paddle=Paddle(10,height//2-paddleHeight//2,paddleWigth,paddleHeight)
    right_paddle=Paddle(width-10-paddleHeight,height//2-paddleHeight//2,paddleWigth,paddleHeight)
    ball=Ball(width//2,height//2,ball_radius)


    
    while run:
        clock.tick(fps)
        draw(win,[left_paddle,right_paddle],ball )

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                break

        keys=pygame.key.get_pressed()
        handle_paddle_movement(keys,left_paddle,right_paddle)
        ball.move()
        handle_collision(ball,left_paddle,right_paddle)

    pygame.quit()

if __name__=='__main__':
    main()