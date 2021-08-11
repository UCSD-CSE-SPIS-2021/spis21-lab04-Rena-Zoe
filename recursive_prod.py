#Lab Warmup: Multiple without *

#We want to define the function and create a loop that adds together the sum of "a" "b" amount of times

def rec_product(a,b):
  if b == 0:
    return 0
  elif b < 0:
    return -a + rec_product(a, b+1)
  else:
    return a + rec_product(a, b-1)
    #You can go back up from the bottom because you are returning a, then calling the function again

    #Our a value is 6 and b is 2
    #b != 0 so it returns 6, calling the function again, a is still 6, but b is 1
      #Calls again and when b is 0 the first is returned (0)
    #Have to call on the function within the function to make it recursive
print(rec_product(6,2))
print(rec_product(0, 5)) #returns 0
print(rec_product(1, 5)) #returns 5
print(rec_product(-1, 5)) #returns -5
print(rec_product(3,-2))
print(rec_product(5, -1)) #return -5
print(rec_product(-5, -1)) #return 5