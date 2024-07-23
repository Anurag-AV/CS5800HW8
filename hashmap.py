import math
import numpy as np
import matplotlib.pyplot as plt 

# Create a Node class to create a node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, key, value):
        if self.getValue(key) != None:
            return "key already present"
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            return "addedd successfully"
        else:
            new_node.next = self.head
            self.head = new_node
            return "addedd successfully"


    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
    def getValue(self, key):
        current_node = self.head
        while(current_node != None and current_node.key != key):
            current_node = current_node.next

        if current_node != None:
            return current_node.value
        else:
            return None

    # Update node of a linked list
        # at given position
    def incrementNode(self, key):
        current_node = self.head
        while(current_node != None and current_node.key != key):
            current_node = current_node.next

        if current_node != None:
            current_node.value += 1
            return "Incremented successfully"
        else:
            return "Key not present"

    # # Method to remove first node of linked list

    # def remove_first_node(self):
    #     if(self.head == None):
    #         return

    #     self.head = self.head.next

    # # Method to remove last node of linked list
    # def remove_last_node(self):

    #     if self.head is None:
    #         return

    #     current_node = self.head
    #     while(current_node != None and current_node.next.next != None):
    #         current_node = current_node.next

    #     current_node.next = None

    # # Method to remove at given index
    # def remove_at_index(self, index):
    #     if self.head == None:
    #         return

    #     current_node = self.head
    #     position = 0
    #     if position == index:
    #         self.remove_first_node()
    #     else:
    #         while(current_node != None and position+1 != index):
    #             position = position+1
    #             current_node = current_node.next

    #         if current_node != None:
    #             current_node.next = current_node.next.next
    #         else:
    #             print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, key):
        current_node = self.head
        if current_node == None:
            return "Key not found"
        if current_node.key == key:
            self.head = self.head.next
            return "Successfully removed"

        while(current_node != None and current_node.next.key != key):
            current_node = current_node.next

        if current_node == None:
            return "Key not found"
        else:
            current_node.next = current_node.next.next
            return "Successfully removed"

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # # print method for the linked list
    def printLL(self):
        current_node = self.head
        s = ""
        while(current_node):
            # print(current_node.key,"|",current_node.value,  end ="->")
            if current_node.key != None:
                s += current_node.key+":"+ str(current_node.value) + "|->|"
            current_node = current_node.next
        return s

#---------------------------------------------------------------------------------------------------------------------------------------------
class HashMap:
    def __init__(self,size):
        self.size = size
        self.prime = 7
        self.array = [LinkedList() for i in range(self.size)]
    def hash(self, key):
        hash = 0
        for i in key:
            hash = hash * self.prime + ord(i)
        return (hash%self.size)

    def put(self, key, value):
        h = self.hash(key)
        return self.array[h].insertAtBegin(key, value)
    def get(self, key):
        h = self.hash(key)
        print(h)
        result = self.array[h].getValue(key)
        if result != None:
            return result
        else:
            return  "Key not present"
    def delete(self,key):
        h = self.hash(key)
        return self.array[h].remove_node(key)
    def increase(self, key):
        h = self.hash(key)
        return self.array[h].incrementNode(key)
    def print(self):
        s = ""
        for i in self.array:
            # print(i.printLL(),"\n")
            s += i.printLL() + "\n"
        return s
    def printSize(self):
        tot = 0
        ans = []
        answer = []
        indexes = []
        for i in range(len(self.array)):
            print(i," ",self.array[i].sizeOfLL())
            tot += self.array[i].sizeOfLL()
            ans.append(self.array[i].sizeOfLL())
            indexes.append(i)
            answer.append(self.array[i].sizeOfLL())
        mean = (tot/self.size)
        for i in range(len(ans)):
            ans[i] = (mean-ans[i])**2
        s = sum(ans)
        var = s / self.size
        print("variance is ",var)
        fig = plt.figure(figsize = (10, 5))
        plt.bar(np.array(indexes) , np.array(answer), color ='maroon', 
        width = 0.4)

        plt.xlabel("Indexes")
        plt.ylabel("Collisions")
        plt.title("Collision histogram for "+str(self.size))
        # plt.show()
        plt.savefig('foo'+str(self.size)+'.png')




# # create a new linked list
# llist = LinkedList()

# # add nodes to the linked list
# llist.insertAtEnd('a')
# llist.insertAtEnd('b')
# llist.insertAtBegin('c')
# llist.insertAtEnd('d')
# # llist.insertAtIndex('g', 2)

# # print the linked list
# print("Node Data")
# llist.printLL()

# # # remove a nodes from the linked list
# # print("\nRemove First Node")
# # llist.remove_first_node()
# # print("Remove Last Node")
# # llist.remove_last_node()
# # print("Remove Node at Index 1")
# # llist.remove_at_index(1)

# # print the linked list again
# print("\nLinked list after removing a node:")
# llist.printLL()

# # print("\nUpdate node Value")
# # llist.updateNode('z', 0)
# # llist.printLL()

# print("\nSize of linked list :", end=" ")
# print(llist.sizeOfLL())


hm30 = HashMap(30)
hm100 = HashMap(300)
hmT = HashMap(1000)
f = open("alice.txt", "r")
s = f.read()
for i in s.split("\n"):
    for j in i.split(" "):
        if hm30.get(j) == "Key not present":
            hm30.put(j,1)
        else:
            hm30.increase(j)
        if hm100.get(j) == "Key not present":
            hm100.put(j,1)
        else:
            hm100.increase(j)
        if hmT.get(j) == "Key not present":
            hmT.put(j,1)
        else:
            hmT.increase(j)
s30 = hm30.print()
s100 = hm100.print()
sT = hmT.print()
with open("Output30.txt", "w") as text_file:
    text_file.write(s30)

with open("Output300.txt", "w") as text_file:
    text_file.write(s100)
with open("Output1000.txt", "w") as text_file:
    text_file.write(sT)
hm30.printSize()
hm100.printSize()
hmT.printSize()
hm = HashMap(20)
while(True):
    ch=input("Enter operation\n 1: Put \n 2: Get \n 3: Increase\n 4: Display \n 5: quit\n 6: print")
    if(ch=='1'):
        n=input("Enter key to insert: ")
        v=int(input("Enter value to insert: "))
        hm.put(n,v)
    elif(ch=='2'):
        n=input("Enter key to delete: ")
        hm.delete(n)
    elif(ch=='3'):
        n=input("Enter key to increment: ")
        hm.increase(n)
    elif(ch=='4'):
        hm.printSize()
    elif(ch=='5'):
        break
    elif(ch == '6'):
        print(hm.print())

