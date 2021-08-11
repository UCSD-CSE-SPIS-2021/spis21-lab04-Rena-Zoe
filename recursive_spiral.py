import turtle

def spiral(initial_length, angle, multiplier):
 turtle.forward(initial_length)
 turtle.right(angle)
 turtle.forward(initial_length * multiplier)
 
 if multiplier < 0:
   return 
 else:
   return spiral(initial_length, angle, multiplier-0.5)
#Our spiral keeps stopping randomly? Anything above 0.2 creates a weird tail at the end
spiral(50, 90, 4)

#version 2-Hannah
import turtle

def spiral(initial_length, angle, multiplier):
 #turtle.forward(initial_length)
 turtle.right(angle)
 turtle.forward(initial_length * multiplier)
 
 if multiplier < 0.5:
   return 
 else:
   return spiral(initial_length, angle, multiplier*0.9)

spiral(50, 90, 4)