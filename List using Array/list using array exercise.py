#lex_auth_012742471863279616506
# Problem Statement
# A teacher has given a project assignment to a class of 10 students.

# She wants to store the marks (out of 100 ) scored by each student. The marks scored are as mentioned below:
# 89,78,99,76,77,67,99,98,90

# Write a python program to store the marks in a list and perform the following:

# 1. The teacher forgot to include the marks of one student. Insert 78 at index position, 8 and display the marks of all 10 students.

# 2. The teacher also wants to know the marks scored by students represented by index positions, 5 and 7. Identify and display the two marks.

def update_mark_list(mark_list, new_element, pos):
    #Write your logic here
    mark_list.insert(pos,new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    '''Remove pass and write your logic here to return a list containing
    the marks at pos1 and pos2 respectively.'''
    # pass
    new_list=[]
    a = mark_list[pos1]
    b = mark_list[pos2]
    thistuple = (a, b)
    new_list.extend(thistuple)
    return new_list
    
#Provide different values for the variables and test your program
mark_list=[89,78,99,76,77,72,88,99]
new_element=78
pos=8
pos1=5
pos2=7
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))