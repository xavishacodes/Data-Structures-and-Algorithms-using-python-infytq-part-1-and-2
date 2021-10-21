# Problem Statement
# Given two lists, both having integer elements, write a python program using python lists to create and return a new list as per the rule given below:

# If the double of an element in list1 is present in list2, then add it to the new list. 
 

# Sample Input	Expected Output
#  list1 - [11, 8,23,7,25, 15]
#  list2 – [6, 33, 50,31, 46, 78, 16,34]	 new_list – [8,23,25]
 
 #lex_auth_0127426336682147841449
def check_double(list1,list2):
    new_list=[]
    #write your logic here
    for i in range(0,len(list1)):
        a=2*list1[i]
        if a in list2:
            new_list.append(list1[i])
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))