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
#Define function to find minimum 
def find_minimum():
#Create random list in which the largest integer is 10 and the size of the list is 10 elements long
 l = random_list(10,10)
#Print list
 print(l)
#Set variable a to the largest value in the list
 a = 10
#Start a for loop which lasts as long as there are elements in the list. If any element is less than the maximum, make it the new value for comparison. Stop when you get to the end of the list.
 for i in range(10):
   if l[i] < a:
    a = l[i]
#Return 'a' which is the lowest value in the list
 return(a)
#Define 'a'
a = find_minimum()
#Print a
print(a)
