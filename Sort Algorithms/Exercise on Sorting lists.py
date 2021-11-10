# Problem Statement
# The school has reopened after the holidays. Maria, the faculty, wants to arrange her students in the increasing order of their heights.

 

# Write a python function which accepts a list of student names and a list of their heights. Assume there is one-to-one correspondence between the two lists. Arrange the students in the increasing order of their height and return a list containing the list of students and their heights.

def order_heights(student_list,height_list):
    new_list=height_list.copy()
    students=[]
    new_list.sort()
    for height in new_list:
        students.append(student_list[height_list.index(height)])
    return[students,new_list]

student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])