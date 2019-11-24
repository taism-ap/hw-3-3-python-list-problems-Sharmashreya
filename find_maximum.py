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
#Define function find_maximum
def find_maximum():
#Create a random list in which the largest possible element is 10 and the size of said list is 10 elements
 l = random_list(10,10)
#Print the list
 print(l)
#Define variable a and set it equal to the minimum possible element in the list
 a = 0
 #Start a for loop that lasts for as long as there are elements in the list
 for i in range(10):
#Test each element against that minimum value. If any element is greater, make it the new standard of comparison and continue till all of the elements in the list have been tested. 
   if l[i] > a:
    a = l[i]
#Return a, which is the maximum 
 return(a)
#Define a outside of the function
a = find_maximum()
#Print a 
print(a)
