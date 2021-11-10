#lex_auth_0127667363860725763513
# Problem Statement
# Alice, a school teacher, has decided to take her 20 students to an exhibition. She got the tickets a week before (T1 to T20) and she was informed that students will be allowed only in groups of 10 inside the exhibition hall.

 

# On the day of exhibition, few students did not turn up. So the teacher followed the below strategy to identify the first 10 students who were sent as group-1.

 

# Suppose the ticket id of the students who turned up on that day is as follows:
# T20, T5, T10, T1, T2, T8, T16, T17, T9, T4, T12, T13, T18

# She made the students stand in a line in increasing order of their ticket numbers. They were asked to leave a vacant position, in case a student has not turned up.
# Ex: T1, T2, V, T4, T5, V, V, T8, T9, T10, V, T12, T13, V, V, T16, T17, T18, V, T20 where V - indicates vacant position.

# Grouped them into 2 groups of 10 each including vacant positions.
# Ex: Group – 1 (T1, T2, V, T4, T5, V, V, T8, T9, T10), Group – 2 (V, T12, T13, V, V, T16, T17, T18, V, T20)

# Filled the vacant positions with the students from the next group as shown in the example below.
# Ex: Group – 1 (T1, T2, T12, T4, T5, T13, T16, T8, T9, T10) Group -2 (T17, T18, T20)

# Write a python function which accepts the unsorted ticket id list and returns the list of ticket ids of the ten students who were finally sent inside as part of Group-1.

 

# Sample Input

# Expected Output

# ['T20','T5','T10','T1','T2','T8','T16','T17',

# 'T9','T4','T12','T13', 'T18']

# ['T1', 'T2', 'T12', 'T4', 'T5', 'T13', 'T16', 'T8', 'T9', 'T10']

 
#lex_auth_0127667363860725763513

def arrange_tickets(tickets_list):
    group1=[]
    group2=[]
    tickets_list.sort()
    for i in range(1,11):
        if('T'+str(i)) in tickets_list:
            group1.append('T'+str(i))
        else:
            group1.append('Vacant')
    for j in range(11,21):
        if('T'+str(j)) in tickets_list:
            group2.append('T'+str(j))
        else:
            continue
    # print("group1",group1)
    # print("group2",group2)
    for x in range(len(group1)):
        if group1[x] != 'Vacant':
            continue
        else:
            for i in range(len(group2)):
                group1[x]=group2[i]
                group2.remove(group2[i])
                break
    return group1
            
        
tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)