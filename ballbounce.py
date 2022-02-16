import pgzrun
import random

ballSize = 40
ballX = random.randint(100,700)
ballY = random.randint(100,500)
speedX = random.uniform(-3,3)
speedY = random.uniform(-3,3)

WIDTH = 800
HEIGHT = 600



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