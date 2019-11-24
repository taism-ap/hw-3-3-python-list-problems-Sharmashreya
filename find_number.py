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

#define a function "find_number" to find the number of times a chosen integer appears in the randomly generated list
def find_number(x):
#Define the parameters of the list in the form of the following (largest number in the list, length of list) In this case (10,10)
  l = random_list(10,10)
#Print the list as described above
  print(l)
#Define two variables 'j' and 'a' and set them to 0
  j = 0
  a = 0 
#Start a loop, and set the range equal to the value entered above for "length of list"
  for i in range(10):
#Check to see if each element is equal to chosen integer 
    if l[j] == x:
#Add 1 to 'a' if the element is equal to the chosen integer
     a = a + 1
#Complete the for loop again till j = length of list
    j = j + 1
#Return a 
  return(a)
#Choose the integer you wish to find the frequency of in the list. In this case, the integer '7'
a = find_number(7)
#Print a
print(a)
