class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
       
    
    def display(self):
        # pass
        #Remove pass and copy the code you had written to display the element(s).
        temp=self.__head
        while temp is not None:
            print(temp.get_data())
            temp=temp.get_next()
    
    def find_node(self,data):
        # pass
        #Remove pass and write the logic to find the node and return the node if found or return None.
        node=self.__head
        while(node!=None):
            if node.get_data()==data:
                return node
            node=node.get_next()
        return node
    
    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node
                print(data_before,"is present")
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present")
        #Remove pass and write the logic to insert an element.

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is found in the Linked list")
                                            
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


snack_list=LinkedList()
#Add all the required element(s)
#Search for the required node
# node=list1.find_node("Sugar")
snack_list.add("Sugar")
snack_list.insert("Salt","Sugar")
snack_list.add("TeaBags")
snack_list.add("Milk")
snack_list.add("Biscuits")
snack_list.insert("Butter","Milk")
# print(list1.display())
# node=list1.find_node("Sugar")
snack_list.display()
# if(node!=None):
#     print("Node found")
# else:
#     print("Node not found") 
# print(node)