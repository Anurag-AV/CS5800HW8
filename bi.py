# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.height = 0
#         self.parent = None
#         self.children = []
# class bino:
#     def __init__(self):
#         self.roots = []
#         self.min = None
#         self.max = None

#     def merge(self, heap1, heap2):
#         if heap1.parent != None or heap2.parent != None:
#             print("can only merge two roots")
#             return False
#         if heap1.height != heap2.height:
#             print("can only merge two heaps of same size")
#             return False
#         if heap1.key < heap2.key:
#             heap2.parent = heap1
#             heap1.children.append(heap2)
#             return heap1
#         else:
#             heap1.parent = heap2
#             heap2.children.append(heap1)
#             return heap2
#     def union(self, heap):
#         update = []
#         h1 = self.children
#         h2 = heap.children
#         while !h1.isEmpty() or !h2.isEmpty():
#             if h1[0].height < h2[0].height:
#                 update.append(h1.pop(0))
#             else:
#                 update.append(h1.pop(0))
#         if !h1.isEmpty():
#             update.extend(h1)
#         if !h2.isEmpty():
#             update.extend(h2)

#         self.children = update
#     def consolidate(self):
#         if self.children.isEmpty() or len(self.children <= 1):
#             return None
#         if len(self.children) == 2:
#             return merge(self.children[0], self.children[1])
#         
class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.sibling = None
        self.child = None

    def reverse(self, sib):
        ret = self
        if self.sibling:
            ret = self.sibling.reverse(self)
        self.sibling = sib
        return ret

    def findMin(self):
        x = self
        y = self
        min_key = self.key
        while x is not None:
            if x.key < min_key:
                y = x
                min_key = x.key
            x = x.sibling
        return y

    def search(self, value):
        temp = self
        node = None
        while temp is not None:
            if temp.key == value:
                node = temp
                break
            if temp.child is not None:
                node = temp.child.search(value)
                if node is not None:
                    break
            temp = temp.sibling
        return node

    def get_size(self):
        size = 1
        if self.child is not None:
            size += self.child.get_size()
        if self.sibling is not None:
            size += self.sibling.get_size()
        return size

class binoHippo:
    def __init__(self):
        self.head = None
        self.size = 0

    # def is_empty(self):
    #     return self.head is None

    def get_size(self):
        return self.size

    # def make_empty(self):
    #     self.head = None
    #     self.size = 0

    def insert(self, value):
        if value > 0:
            temp = Node(value)
            if self.head is None:
                self.head = temp
                self.size = 1
            else:
                self.union(temp)
                self.size += 1

    def merge(self, bin_heap):
        temp1 = self.head
        temp2 = bin_heap

        if temp1 is None:
            self.head = temp2
            return
        if temp2 is None:
            return

        if temp1.degree <= temp2.degree:
            self.head = temp1
        else:
            self.head = temp2
            temp2 = temp1
            temp1 = self.head

        while temp1.sibling is not None and temp2 is not None:
            if temp1.sibling.degree <= temp2.degree:
                temp1 = temp1.sibling
            else:
                temp3 = temp1.sibling
                temp1.sibling = temp2
                temp2 = temp3

        if temp1.sibling is None:
            temp1.sibling = temp2

    def union(self, bin_heap):
        self.merge(bin_heap)
        prev_x = None
        x = self.head
        next_x = self.head.sibling

        while next_x is not None:
            if x.degree != next_x.degree or (next_x.sibling is not None and next_x.sibling.degree == x.degree):
                prev_x = x
                x = next_x
            else:
                if x.key <= next_x.key:
                    x.sibling = next_x.sibling
                    next_x.parent = x
                    next_x.sibling = x.child
                    x.child = next_x
                    x.degree += 1
                else:
                    if prev_x is None:
                        self.head = next_x
                    else:
                        prev_x.sibling = next_x
                    x.parent = next_x
                    x.sibling = next_x.child
                    next_x.child = x
                    next_x.degree += 1
                    x = next_x
            next_x = x.sibling

    def minimum(self):
        if self.head is None:
            return None
        return self.head.findMin().key

    def delete(self, value):
        if self.head is not None and self.head.search(value) is not None:
            self.decrease_key(value, self.minimum() - 1)
            self.extract_min()

    def decrease_key(self, old_value, new_value):
        node = self.head.search(old_value)
        if node is None:
            return
        node.key = new_value
        temp = node
        temp_parent = node.parent

        while temp_parent is not None and temp.key < temp_parent.key:
            temp.key, temp_parent.key = temp_parent.key, temp.key
            temp = temp_parent
            temp_parent = temp_parent.parent

    def extract_min(self):
        if self.head is None:
            return -1

        temp = self.head
        prev_x = None
        min_node = self.head.findMin()

        while temp.key != min_node.key:
            prev_x = temp
            temp = temp.sibling

        if prev_x is None:
            self.head = temp.sibling
        else:
            prev_x.sibling = temp.sibling

        temp = temp.child
        fake_node = temp

        while temp is not None:
            temp.parent = None
            temp = temp.sibling

        if self.head is None and fake_node is None:
            self.size = 0
        elif self.head is None:
            self.head = fake_node.reverse(None)
            self.size = self.head.get_size()
        elif fake_node is None:
            self.size = self.head.get_size()
        else:
            self.union(fake_node.reverse(None))
            self.size = self.head.get_size()

        return min_node.key

    def display_heap(self):
        if self.head is None:
            print("\nHeap is empty.")
            return
        print("\nHeap:")
        self.display_heap_helper(self.head)

    def display_heap_helper(self, node):
        if node is not None:
            print(f"Key: {node.key}, Degree: {node.degree}, ", end="")
            if node.parent:
                print(f"Parent: {node.parent.key}, ", end="")
            else:
                print("Parent: None, ", end="")
            if node.sibling:
                print(f"Sibling: {node.sibling.key}, ", end="")
            else:
                print("Sibling: None, ", end="")
            if node.child:
                print(f"Child: {node.child.key}")
            else:
                print("Child: None")
            if node.child:
                self.display_heap_helper(node.child)
            if node.sibling:
                self.display_heap_helper(node.sibling)

def main():
    # Make object of binoHippo
    bin_heap = binoHippo()

    # Inserting in the binomial heap
    # Custom input integer values
    bin_heap.insert(12)
    bin_heap.insert(8)
    bin_heap.insert(5)
    bin_heap.insert(15)
    bin_heap.insert(7)
    bin_heap.insert(2)
    bin_heap.insert(9)

    # Size of binomial heap
    # print("Size of the binomial heap is", bin_heap.get_size())

    # # Displaying the binomial heap
    # bin_heap.display_heap()

    # # Deletion in binomial heap
    # bin_heap.delete(15)
    # bin_heap.delete(8)

    # # Size of binomial heap
    # print("Size of the binomial heap is", bin_heap.get_size())

    # # Displaying the binomial heap
    # bin_heap.display_heap()

    # # Making the heap empty
    # bin_heap.make_empty()

    # # checking if heap is empty
    # print(bin_heap.is_empty())

    bin_heap2=binoHippo()
    bin_heap2.insert(120)
    bin_heap2.insert(28)
    
    bin_heap.union(bin_heap2.head)
    print("After Union: ")
    bin_heap.display_heap()

    bin_heap.decrease_key(120,1)
    print("After Decrease Key: ")
    bin_heap.display_heap()
    
    bin_heap.extract_min()
    bin_heap.display_heap()
if __name__ == "__main__":
    main()

# while(True):
#     ch=input("Enter operation\n 1: Insert \n 2: Delete \n 3: Search\n 4: Display \n 5: Quit")
#     if(ch=='1'):
#         n=int(input("Enter element to insert: "))
#         bh.insert(n)
#     elif(ch=='2'):
#         n=int(input("Enter element to delete: "))
#         bh.delete(n)
#     elif(ch=='3'):
#         n=int(input("Enter element to search: "))
#         bh.search(n)
#     elif(ch=='4'):
#         bh.print_heap()
#     elif(ch=='5'):
#         print("Thank you")
#         break
