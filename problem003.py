# Problem #3 [Medium]
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
import pickle


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# I really do not understand what this method should do, I just made it a string ready to be executed  as code
# and create the desired object
def serialize(node):
    if node == None:
        return ''
    returnString = "Node('"+node.val+"'"
    if node.left is not None:
        returnString += "," + serialize(node.left)
    if node.right is not None:
        returnString += "," + serialize(node.right)
    return returnString+")"


# add the object name for use
def deserialize(param):
    param = "node = " + param
    exec(param)
    return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

# looking online for serialization and python I found many references to pickle so I tested one use
with open("pickledNode.p", "wb") as myFile:
    pickle.dump(node, myFile)
with open("pickledNode.p", "rb") as myFile:
    pickledNode = pickle.load(myFile)
assert pickledNode.left.left.val == 'left.left'

# I do not like this solution, looks weird to me, but I also do not know what I must do
# My solution was fast do think and implement, took less than 20 minutes and spent also almost one hour trying
# to understand more about serialization, pickle and json
