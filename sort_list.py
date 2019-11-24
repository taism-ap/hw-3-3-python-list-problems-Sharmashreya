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
#Create empty list k
  k = []
#Start for loop to last as long as there are elements in the list
  for i in range(10):
#Start a second for loop that also lasts as long as there are elements in the list
    for j in range(10):
#Compare each value on the list to j, which goes from 0 and adds one each time it goes through this loop. If it is equal to 0, add it to the empty list k. 
      if l[j] == i:
        x = l[j]
        k.append(x)

#Return k
  return(k)
#Define k again and print 
k = sort_list()
print(k)
