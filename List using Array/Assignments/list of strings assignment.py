# Problem Statement
# Given two lists, both having String elements,
#  write a python program using python lists to 
#  create a new string as per the rule given below:
# The first element in list1 should be merged with last element in list2, 
# second element in list1 should be merged with second last 
# element in list2 and so on. If an element in list1/list2 is None, 
# then the corresponding element in the other 
# list should be kept as it is in the merged list. 

#lex_auth_0127426166978887681375


def merge_list(list1, list2):
    s=""
    #write your logic here
    for x,y in zip(list1,list2[::-1]):
        if y and x:
            s+= x + y
        elif x:
            s+= x
        elif y:
            s+= y  
        
        s+=' '
    return s[:-1]
        
       


#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)