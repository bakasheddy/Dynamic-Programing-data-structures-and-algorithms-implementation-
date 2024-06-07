class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None 
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
 
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def display_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.display_tree()
    
    
def build_tree():
    root = TreeNode('Electronics')
    
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('hp'))
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Dell'))
    
    cellphones = TreeNode('Cell phones')
    cellphones.add_child(TreeNode('iPhone'))
    cellphones.add_child(TreeNode('Huawei'))
    cellphones.add_child(TreeNode('Samsung'))
    
    tv = TreeNode('TVs')
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Max'))
    
    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(tv)
    return root

if __name__ == '__main__':
    root = build_tree()
    root.display_tree()