import turtle

#We did our code in a file with python turtle, so you might wanna copy it into one of those

def tree(trunk_length, height):
  #If the height is less than 1 we just want it to return
  if height < 1:
    return

  #We want the turtle to move forward
  turtle.forward(trunk_length)

  if height > 1:
  #We want the turtle to make a left branch
    turtle.left(45)
    tree(trunk_length-10, height-1)
    #We can call the function here, the function is to go forward, so it will go forward and decrease, so it's smaller than the trunk

  #We want the turtle to make a right branch
    turtle.right(90)
    tree(trunk_length-10, height-1)

  #We want the turtle to realign at the trunk
    turtle.left(45)
    #Need this step here because if you re-align it then it will not draw any other funky lines
    #Basically, puts the turtle back on track

  turtle.backward(trunk_length)
  #Need it to return to it's starting position, which is going up one line then down again to the bottom, facing north

turtle.setheading(90)
#This code makes it so we don't need to turn the turtle when going forward, but changes the canvas
turtle.exitonclick()

tree(75, 4)

#Gary went over this in Depth today^

#Our previous code:

#def tree(trunk_length, height):
  #if height < 1:
    #return
  #turtle.left(90)
  #turtle.forward(trunk_length)
  #turtle.right(45)
  #tree(trunk_length//2, height-1)
  #turtle.forward(trunk_length//2)
  #Backpart will happen in the recursion so think of the middle
  #turtle.left(90)
  #tree(trunk_length//2, height-1)
  #turtle.right(45)
  #turtle.backward(trunk_length//2)

  #turtle.right(45)

#import turtle
#def tree(trunk_length, height):
  #turtle.left(90)
  #turtle.forward(trunk_length)
  #turtle.right(45)
  #turtle.forward(trunk_length//2)
  #turtle.backward(trunk_length//2)
  #turtle.left(90)
  #turtle.forward(trunk_length//2)
  #turtle.right(45)
  #if height > 1:
    #return tree(trunk_length//2, height//2)
  #elif height < 1:
   #turtle.penup()
    #We want it to go back to original 90 degree angle
    #turtle.right(135)
    #turtle.forward(trunk_length//2)
    #turtle.right(45)
    #turtle.forward(trunk_length//2)

#tree(200, 4)