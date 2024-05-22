#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BinarySerachTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        #add data in left subtree
        if data < self.data: 
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySerachTree(data)
        else:# for right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySerachTree(data)
                
    def search(self, val):
        if self.data == val:#best case
            return True
        #search left subtree if search is less than rootnode
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        #search right subtree if search is greater than rootnode
        if val > self.data:
            if self.right:
                self.right.search(val) 
            else:
                return False
            
    def in_order_traversal(self):
        elements = []
        #visit left
        if self.left:
            elements += self.left.in_order_traversal()
            
        #visit base node
        elements.append(self.data)
        
        #visit right node
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements 
    
    
def build_tree(elements):
    root = BinarySerachTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [1,19,0,7,4,3,5,6,2,4,7,4,2]
    num_tree = build_tree(numbers)
    print(num_tree.in_order_traversal())
    print(num_tree.search(19))


# In[ ]:




