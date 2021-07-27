# 트리순회 - 백준

#전위 순회
def preorder(node):
    if node == '.':
        return
    print(node, end = "")
    preorder(tree[node][0])
    preorder(tree[node][1])

#중위 순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end = "")
    inorder(tree[node][1])

#후위 순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = "")

n = int(input())
#dictionary 로 key-value 형태로 받아서 tree순회
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')