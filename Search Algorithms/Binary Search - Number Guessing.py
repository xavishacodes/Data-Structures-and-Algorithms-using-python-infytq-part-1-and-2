#DSA-Tryout
# Problem Statement
# Use the binary search algorithm to implement the logic for the number guessing game that you had played. The program should display the number of guesses made each time you play.

 

# Assume that the list has elements sorted in ascending order.

 

# Hint: use random.randrange() to identify a random number from the list to be guessed.

# Note: Reuse the earlier written code for number guessing game wherever required
import random

def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
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
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    a=[]
    a= initialize_list_of_elements(n)    
    b=random.randrange(1,n)
    c=find_it(b,a)
    # pass
    print(c)


#Pass different values to play() and observe the output
play(400)