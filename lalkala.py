class Node:
    def __init__(self, value):
        self.colour = "r"
        self.value = value
        self.parent  = None
        self.left  = None
        self.right  = None
class BST:
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = "b"
        self.nil.left = self.nil.right = self.nil
        self.root = self.nil

    def leftRotate(self, x): 
        # print("left rotate", x.value)
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent  =  x
        y.parent  =  x.parent
        if x.parent ==  None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.p.right = y
        y.left = x 
        x.parent = y

    def rightRotate(self, x):
        # print("right rotate ", x.value) 
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent  =  x
        y.parent  =  x.parent
        if x.parent ==  None:
            self.root = y
            # self.root.parent = self.nil
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x 
        x.parent = y

    def insert(self,z):
        # print("inserting ",z.value)
        z.left = self.nil
        z.right = self.nil
        x = self.root
        y = None
        while x != self.nil:
            # print("getting location")
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.value < y.value:
            # print("got it, comes under ",z.parent.value)
            y.left = z
        else:
            # print("got it, comes under ",z.parent.value)
            y.right = z
        if z.parent == None:
            z.colour = "b"
            return
        if z.parent.parent == None:
            z.colour = "b"
            return
        self.insertFixup(z)

    def insertFixup(self,z):
        # print("fixing ",z)
        while z != self.root and z.parent.colour == "r":
            # print(z.value,z.colour," is a being checked ",z.parent.colour, z.parent.value)
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.colour == "r":
                    # print("uncle ",y.value, " is ", y.colour)
                    z.parent.colour = "b"
                    y.colour = "b"
                    z.parent.parent.colour = "r"
                    z = z.parent.parent
                else:
                    # print("parent is red and ","uncle ",y.value, " is ", y.colour)
                    if z == z.parent.right:
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.colour = "b"
                    z.parent.parent.colour = "r" 
                    self.rightRotate(z.parent.parent)
            else:
                # print("in else")
                y = z.parent.parent.left
                if y.colour == "r":
                    # print("uncle ",y.value, " is ", y.colour)
                    z.parent.colour = "b"
                    y.colour = "b"
                    z.parent.parent.colour = "r"
                    z = z.parent.parent
                else:
                    # print("parent is red and ","uncle ",y.value, " is ", y.colour)
                    if z == z.parent.left:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.colour = "b"
                    z.parent.parent.colour = "r"
                    self.leftRotate(z.parent.parent)
        # print("setting root to black")
        self.root.colour = "b"

    def inorder(self, x):
        if x != self.nil:
            self.inorder(x.left)
            print(x.value,"|",x.colour)
            self.inorder(x.right)
 
    def height_of_tree(self, root):
        if root is  None or root is self.nil:
            return 0
        return 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))


    def sort(self):
        self.inorder(self.root)

    def search(self, value):
        res= self.searchHelper(self.root,value)
        if res==self.nil or res==None :
            return "Not Found"
        else:
            return "Found"
    def searchHelper(self,node,value):
        if node==self.nil or value==node.value:
            return node
        elif value<node.value :
            return self.searchHelper(node.left,value)
        else:
            return self.searchHelper(node.right,value)

    def getPred(self, node, value):
        if self.root == self.nil or self.root == None or node == self.nil or node == None:
            return "No predescessor"
        if node.value == value:
            if node.left != self.nil:
                t = node.left
                while t.right != self.nil:
                    t = t.right
                return t.value
            else:
                t = node.parent
                x = node
                while t != self.nil and t != None:
                    if x == t.left:
                        x = t
                        t = t.parent
                    else:
                        return t.value
                return "No predecessor"
        if node.value > value:
            return self.getPred(node.left, value)
        else:
            return self.getPred(node.right, value)
    def predecessor(self, value):
        return (self.getPred(self.root,value))

    def getSucc(self, node, value):
        if self.root == self.nil or self.root == None or node == self.nil or node == None:
            return "No predescessor"
        if node.value == value:
            if node.right != self.nil:
                t = node.right
                while t.left != self.nil:
                    t = t.left
                return t.value
            else:
                t = node.parent
                x = node
                while t != self.nil and t != None:
                    if x == t.right:
                        x = t
                        t = t.parent
                    else:
                        return t.value
                return "No successor"
        if node.value > value:
            return self.getSucc(node.left, value)
        else:
            return self.getSucc(node.right, value)
    def successor(self, value):
        return (self.getSucc(self.root,value))

    def max(self):
        t = self.root
        if t == self.nil or t == None:
            return "no max"
        while t.right != self.nil and t.right != None:
            t = t.right
        return t.value
    def min(self):
        t = self.root
        if t == self.nil or t == None:
            return "no min"
        while t.left != self.nil and t.left != None:
            t = t.left
        return t.value
    
    def deleteNode(self,value):
        t  = self.root
        if self.root == self.nil or self.root == None:
            return "no data to delete"
        while t != self.nil and t.value != value and t != None:
            if value > t.value:
                t = t.right
            elif value < t.value:
                t = t.left
        if t == self.nil or t == None:
            return "no data to delete"
        if t.right != None and t.right != self.nil:
            print("has a right")
            node = self.minValue(t.right)
            print("value is ", node.value)
            t.value = node.value
            if node == t.right:
                t.right  = t.right.right
                return
            node.parent.left = node.right
            if node.right != self.nil:
                node.right.parent = node.parent
        elif t.left != None and t.left != self.nil:
            print("has a left")
            node = self.maxValue(t.left)
            t.value = node.value
            if node == t.left:
                t.left  = t.left.left
                return
            node.parent.right = node.left
            if node.left != self.nil:
                node.left.parent = node.parent
        else:
            print("no child")
            if t == t.parent.left:
                t.parent.left = self.nil
            else:
                t.parent.right = self.nil

    
    def minValue(self, node):
        minv = node
        while node.left!=self.nil:
            minv = node.left
            node = node.left
        return minv
    def maxValue(self, node):
        maxv = node
        while node.right!=self.nil:
            minv = node.right
            node = node.right
        return maxv

    # def print_space(self,n, removed):
    #     for i in range(n):
    #         print("\t", end="")
    #     if removed is None:
    #         print(" ", end="")
    #     else:
    #         print(removed.value,"|",removed.colour, end="")
    def displpayTree(self):
        self.print_tree(self.root, 0)
    def print_tree(self, root, space):
        COUNT = [10]
        if (root == None or root == self.nil):
            return
     
        # Increase distance between levels
        space += COUNT[0]
     
        # Process right child first
        self.print_tree(root.right, space)
     
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.value,"|",root.colour)
     
        # Process left child
        self.print_tree(root.left, space)
    # def print_binary_tree(self,root):
    #     tree_level = []
    #     temp = []
    #     tree_level.append(root)
    #     counter = 0
    #     height = self.height_of_tree(root) - 1
    #     number_of_elements = 2 ** (height + 1) - 1
    #     while counter <= height:
    #         removed = tree_level.pop(0)
    #         if len(temp) == 0:
    #             self.print_space(int(number_of_elements /
    #                             (2 ** (counter + 1))), removed)
    #         else:
    #             self.print_space(int(number_of_elements / (2 ** counter)), removed)
    #         if removed is None:
    #             temp.append(None)
    #             temp.append(None)
    #         else:
    #             temp.append(removed.left)
    #             temp.append(removed.right)
    #         if len(tree_level) == 0:
    #             print("\n")
    #             tree_level = temp
    #             temp = []
    #             counter += 1

rb = BST()
# s = 356
# for i in range(s-1, 0, -1):
#     rb.insert(Node(i))
# # rb.sort()
# print(rb.search(s-1))
# for i in range(s-1, 0, -1):
#     if rb.predecessor(i) == None:
#         print("its none")
#     elif i == 1:
#         print("reached the end")
#     elif i - rb.predecessor(i) != 1:
#         print("hopefully last hai")
# for i in range(1, s):
#     if rb.successor(i) == None:
#         print("its none")
#     elif i == s-1:
#         print("reached the end")
#     elif rb.successor(i) - i != 1:
#         print("hopefully last hai")
# for i in range(3,s):
#     print("deleting", i-1)
#     rb.deleteNode(i-1)
#     if rb.predecessor(i) != 1:
#         print("gadbad hai", rb.predecessor(i), "---",i)
#         break

# rb.deleteNode(10)
# rb.sort()
# rb.print_binary_tree(rb.root)
print(rb.min(),rb.max())
while(True):
    print("\n1. Insert \n2. Delete\n3. Minimum\n4. Maximum\n5. Predecessor\n6. Sort\n7. Search\n8. Exit\n10. Successor")
    ch=input("Select an operation: ")
    if(ch=='1'):
        n=int(input("Enter node to be inserted: "))
        rb.insert(Node(n))
        print("Height of tree is: ",rb.height_of_tree(rb.root))
    elif(ch=='2'):
        n=int(input("Enter node to be deleted: "))
        rb.deleteNode(n)
        # print("Height of tree is: ",rbt.findHeight)
    elif(ch=='3'):
        print("Minimum: ",rb.min())
    elif(ch=='4'):
        print("Maximum: ",rb.max())
    elif(ch=='5'):
        n=int(input("Enter node for which Predecessor is required: "))
        print(rb.predecessor(n))
    elif(ch=='10'):
        n=int(input("Enter node for which successor is required: "))
        print(rb.successor(n))
    elif(ch=='6'):
        rb.sort()
        # rb.print_binary_tree(rb.root)
    elif(ch=='7'):
        n=int(input("Enter node to be searched: "))
        print(rb.search(n))
    elif(ch=='8'):
        print('Thank you')
        break
    elif(ch == '9'):
        rb.displpayTree()
    else:
        print("Invalid")
