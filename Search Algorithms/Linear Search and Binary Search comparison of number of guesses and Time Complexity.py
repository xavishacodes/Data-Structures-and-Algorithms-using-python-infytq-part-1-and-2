#DSA-Tryout
# Problem Statement
# Combine the two number guessing programs written earlier, one using linear search and the other using binary search. Along with the number of guesses, find and display the execution time for each of these algorithms.

 

# Use the template code given to compute the execution time.

 

# Play the game multiple times using values of n such as 100, 1000, 10000, 100000, 1000000 etc. and observe the difference w.r.t number of guesses and execution time between both the algorithms.
import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #remove pass and copy the code written earlier for linear search
    # pass
    count=0
    i=0
    # for i in range(element_list):
    for i in element_list:
        if num == element_list[i]:
            break
        else:
            count+=1
    return count

def find_it_binary(num,element_list):
    #remove pass and copy the code written earlier for binary search
    # pass
    count=0
    a=len(element_list)
    right=len(element_list)-1
    left=0
    mid = (a/2)-1
    for i in element_list:
        if num==element_list[int(mid)]:
            break
        elif num<element_list[int(mid)]:
            right=element_list[int(mid-1)]
            mid= ( left+right )/2
            count+=1
        else:
            left=element_list[int(mid+1)]
            mid= ( left+right )/2
            count+=1
    return count

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    rand_index=random.randrange(0,len(list_of_elements))
    rand_num=list_of_elements[rand_index]
    print("Number to be guessed:",rand_num)
    start=timer()
    print("No. of guesses made using linear search:",find_it_linear(rand_num,list_of_elements))
    end=timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format( (end-start)))
    start=timer()
    print("No. of guesses made using binary search:",find_it_binary(rand_num,list_of_elements))
    end=timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format( (end-start)))

#Pass different values to play() and observe the output
play(40000)

#Output
# Number to be guessed: 6574
# No. of guesses made using linear search: 6572
# Linear Search:Execution time in seconds:0.00048
# No. of guesses made using binary search: 13
# Binary Search:Execution time in seconds:0.00001