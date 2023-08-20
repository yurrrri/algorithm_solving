n = int(input())
nodes = {}

class node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

def preorder(node):
  print(node.data, end='')
  if node.left != ".":
    preorder(nodes[node.left])
  if node.right != ".":
    preorder(nodes[node.right])

def inorder(node):
  if node.left != ".":
    inorder(nodes[node.left])
  print(node.data, end='')
  if node.right != ".":
    inorder(nodes[node.right])

def postorder(node):
  if node.left != ".":
    postorder(nodes[node.left])
  if node.right != ".":
    postorder(nodes[node.right])
  print(node.data, end='')

for _ in range(n):
  data, left, right = input().split()
  nodes[data] = node(data=data, left=left, right=right)

preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])