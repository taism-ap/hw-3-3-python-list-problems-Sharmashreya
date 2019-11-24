# import the randint function from the random module
from random import randint
# create a function to generate a list of "size" random integers
# up to a maximum of "largest"
def random_list(largest,size):
# create an empty list
  l = []
# add a random number to the list the appropriate number of times
  for i in range(size):
    n = randint(0,largest-1)
    l.append(n)
#return the list to check
  return(l)
#Define function sort_list
def sort_list():
#Create random list with the largest integer, 10, and size of 10
  l = random_list(10,10)
#Print the list
  print(l)
#Create empty list j
  j = []
#Define variable a and set it equal to 0
  a = 0
#Start for loop to repeat as many times as the list is large
  for i in range(10):
#If conditional statement if any variable is equal to 0, add it to the list first
   if l[i] == a:
     x = l[i]
     j.append(x)  
#Repeat steps mentioned above for each integer from the minimum to the maximum value
  for i in range(10):
    if l[i] == a + 1:
       x = l[i]
       j.append(x)

  for i in range(10):
    if l[i] == a + 2:
       x = l[i]
       j.append(x)

  for i in range(10):
    if l[i] == a + 3:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 4:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 5:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 6:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 7:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 8:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 9:
       x = l[i]
       j.append(x)
  
  for i in range(10):
    if l[i] == a + 10:
       x = l[i]
       j.append(x)
#Return j
  return(j)
#Define j again and print 
j = sort_list()
print(j)
