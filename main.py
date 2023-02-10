import pygame as py
import nplanet
import random
py.init() #initializing pygame 

print("welcome to the planet simulation")
n=input(str("what do you want your solar system to be called?"))

num=random. randint(0, 255) 
num1=random. randint(0, 255)
num2=random. randint(0, 255)
num3=random. randint(0, 255)
num4=random. randint(20, 255)

# create the canvas & name for the window
dim = 500
window=py.display.set_mode((dim,dim))
py.display.set_caption(n)

#creating colors 
black=(0,0,0)
red= (255, num4, 30)

col4=(num3, num1, 255)
col3=(num2, num3, 255)
col1=(num1, 255, num)
col2=(num,num2,255)


earth= nplanet.Planet(250,250,15,400,col4,window,1.5)
venus= nplanet.Planet(250,250,12.5,400,col3,window,1.2)
mercury=nplanet.Planet(250,250,10,400,col2,window,2)
jupiter=nplanet.Planet(250,250,20,400,col1,window,1)


PLANETS=[mercury,earth,jupiter,venus]
time=py.time.Clock()
done=True
while done:
  time.tick(30)
  window.fill(black)
  sun=py.draw.circle(window, red, (dim//2,dim//2),30)
  for exit in py.event.get():
    if exit.type ==py.QUIT:
      done=False   
  for i in PLANETS:
     i.draw(window)
     i.move()
  earth.angle += .05
  mercury.angle += .05
  jupiter.angle += 0.05
  venus.angle += 0.05
  py.display.update()
  
py.quit()


