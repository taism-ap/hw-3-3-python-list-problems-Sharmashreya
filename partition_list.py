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


#Define function to partition list
def partition_list(x):
#Create random list where the largest integer is 10 and the size of said list is 10 elements long
  l = random_list(10,10)
#Print the list
  print(l)
#Start an empty list j
  j = []
#Define three variables b, c, and d and set them equal to 0
  b = 0
  c = 0
  d = 0
#Start a for loop which lasts as long as there are elements in the list. If any element is less than the number decided above, then put add it to the list. 
  for i in range(10):
   if l[i] < x:
    b = l[i]
    j.append(b)
#Start another for loop which lasts as long as there are elements in the list. If any element is equal than the number decided above, then put add it to the list. 
  for i in range(10):
    if l[i] == x:
      d = l[i]
      j.append(d)
#Start a third for loop which lasts as long as there are elements in the list. If any element is greater than the number decided above, then put add it to the list. 
  for i in range(10):
    if l[i] > x:
      c = l[i]
      j.append(c)
#Return j
  return(j)
#Define j and choose the number at which to partition
j = partition_list(3)
#Print j
print(j)
