import pygame as py
import math 
py.init() #initializing pygame 

class Planet():
  dim=500
 
  def __init__(self, x, y,radius, size, color,window,co):
    self.x=x
    self.y=y
    self.window=window
    self.radius = radius
    self.c = color
    self.size = size
    self.angle = 0
    self.co = co
    self.initial_x = self.x
    self.initial_y =self.y
    #self.star = star
    
  def draw(self, window): 


    py.draw.circle(window, self.c, (self.x,self.y),self.radius)
    #py.draw.lines(window, self.c, False, (self.x, self.y), 2)
  def move(self): 

    self.x = self.initial_x+  10 *self.radius*math.cos( self.co *self.angle)
    self.y = self.initial_y+ 10 *self.radius*math.sin(self.co *self.angle) 
    # self.x=self.x%360
    # self.y=self.y%360