import csv
import time
start_time = time.time()

#binary tree
class TreeNode:
    def __init__(self,value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self,value):
        if self.value is None:
            self.value = value
            return
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                return
            else:
                self.left.insert(value)
                return
        else:
            if self.right is None:
                self.right = TreeNode(value)
                return
            else:
                self.right.insert(value)
                return

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        return True

tree = TreeNode()

def csvFiles():
    filepath = open('../files/datastructures3.csv','r')
    with filepath as csvfile:
        filecontent = csv.reader(csvfile,delimiter=';')
        for row in filecontent:
            yield row

def addingToNode():
    counter = 0
    for i in csvFiles():
        if counter <= 1000:
            tree.insert(i[0])
            print(i[0])
            counter += 1

addingToNode()

print(tree.find(input('Search for movie? ')))