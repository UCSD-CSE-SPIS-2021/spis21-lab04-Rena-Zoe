
import turtle

#Snowflake:
def snowflake_side(side_length, levels):
  
  #This is our base case
  if levels < 1:
    turtle.forward(side_length)
    return
  
  #turtle.forward(side_length)

  #Each "if" statement is for a new base case
  #"Else" statement is where you do the recursive call

  else:
    snowflake_side(side_length, levels-1)
   #We want it to create the 60 degree angle for the tip of triangle
    turtle.left(60)
    snowflake_side(side_length, levels-1)
   
   #We want it to create another 60 degree angle to go back down
    turtle.right(120)
    snowflake_side(side_length, levels-1)

   #We want the turtle to go back horizontally
    turtle.left(60)
    snowflake_side(side_length, levels-1)

      
def snowflake(side_length, levels): 
  turtle.right(120)
  snowflake_side(side_length, levels)
  turtle.right(120)
  snowflake_side(side_length, levels)
  turtle.right(120)
  snowflake_side(side_length, levels)

turtle.speed(10)
snowflake(10, 4)