import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ballSize = 40
ballX = random.randint(ballSize,WIDTH-ballSize)
ballY = random.randint(ballSize,HEIGHT-ballSize)
speedX = random.uniform(-3,3)
speedY = random.uniform(-3,3)





def draw():
  screen.clear()
  screen.draw.filled_circle((ballX,ballY),ballSize,"white")
  

def update():
  global ballX, ballY, speedX, speedY

  ballX += speedX
  ballY += speedY

  if ballX < ballSize:
    ballX = ballSize
    speedX = -speedX
  if ballX > WIDTH-ballSize:
    ballX = WIDTH-ballSize
    speedX = -speedX
  if ballY < ballSize:
    ballY = ballSize
    speedY = -speedY
  if ballY > HEIGHT-ballSize:
    ballY = HEIGHT-ballSize
    speedY = -speedY
    

  


pgzrun.go() # Must be last line