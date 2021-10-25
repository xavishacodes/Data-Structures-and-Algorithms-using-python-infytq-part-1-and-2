#lex_auth_0127667385795952643524
# Problem Statement
# Write a python function which accepts a list of numbers, the start index and the end index. The numbers are arranged in the list in increasing order until a particular index and after that it is arranged in decreasing order.

# This function should find and return the index position at which the increasing list starts decreasing.

# Sample Input

# Expected Output

# [1,4,7,8,9,5,4], 0, 6

# 5

def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    # pass
    for i in list1[start+1:]:
        if i<list1[start]:
            return list1.index(i)
        start+=1
        

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)