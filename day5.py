"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    if node == None:
        return 'None'
    return "({}:({},{}))".format(node.val, serialize(node.left), serialize(node.right))
    
def deserialize(stree):
    if stree == 'None':
        return None

    splt = stree.split(":",1)
    val = splt[0][1:]
    childs = splt[1][1:-2]
    
    if "(" not in childs:
        left, right = childs.split(",",1)
        return Node(val,Node(left),Node(right))

    openb = closeb = 0
    for idx in range(len(childs)):
        if childs[idx] == "(":
            openb += 1
        if childs[idx] == ")":
            closeb += 1
        if openb == closeb:
            mid = idx
            break
        

    node = Node(val,deserialize(childs[:mid+1]),deserialize(childs[mid+2:]))
    return node

    




def test():
    node = Node('root',  Node('left', Node('left.left')) , Node('right') )
    assert deserialize(serialize(node)).left.left.val == 'left.left'
test()