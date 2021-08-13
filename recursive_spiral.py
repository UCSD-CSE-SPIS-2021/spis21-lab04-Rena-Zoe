#Box Spiral - Hannah helped us :D
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

#Other (Hexagon-al?) Spiral
import turtle

def spiral(initial_length, angle, multiplier):
 #turtle.forward(initial_length)
 turtle.right(angle)
 turtle.forward(initial_length * multiplier)
 
 if multiplier < 0.5:
   return 
 else:
   return spiral(initial_length, angle, multiplier*0.9)

spiral(100, -45, 5)