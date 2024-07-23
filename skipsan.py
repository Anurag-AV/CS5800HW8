import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SL:
    def __init__(self):
        self.level = 0
        self.header = self.create(-1, self.level)

    def toss(self):
        l = 0
        while random.randint(0, 1) == 0:
            l += 1
        return l

    def create(self, key, level):
        return Node(key, level)

    def insert(self, key):
        current = self.header
        update = [None] * (self.level + 1)

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        # if not current or current.key != key:
        rlevel = self.toss()
        if rlevel > self.level:
            for i in range(self.level + 1, rlevel + 1):
                update.append(self.header)
            self.header.forward.extend([None] * (rlevel - self.level))
            self.level = rlevel

        new_node = self.create(key, rlevel)

        for i in range(rlevel + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        print(f"Successfully Inserted key {key}")

    def delete(self, key):
        current = self.header
        update = [None] * (self.level + 1)

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1

            print(f"Successfully deleted key {key}")

    def search(self, key):
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            print(f"Found key: {key}")
        else:
            print(f"Key {key} not found")

    def print(self):
        for i in range(self.level, -1, -1):
            node = self.header.forward[i]
            print(f"Level {i}: ", end="")
            while node:
                print(node.key, end=" ")
                node = node.forward[i]
            print()

random.seed()
lst = SL()


lst.insert(3)
lst.insert(6)
lst.insert(7)
lst.insert(9)
lst.insert(12)
lst.insert(19)
lst.insert(17)
lst.insert(26)
lst.insert(21)
lst.insert(25)
lst.print()

lst.search(19)
lst.delete(19)
lst.print()

while(True):
    ch=input("Enter operation\n 1: Insert \n 2: Delete \n 3: Search\n 4: Display \n 5: Quit")
    if(ch=='1'):
        n=int(input("Enter element to insert: "))
        lst.insert(n)
    elif(ch=='2'):
        n=int(input("Enter element to delete: "))
        lst.delete(n)
    elif(ch=='3'):
        n=int(input("Enter element to search: "))
        lst.search(n)
    elif(ch=='4'):
        lst.print()
    elif(ch=='5'):
        print("Thank you")
        break