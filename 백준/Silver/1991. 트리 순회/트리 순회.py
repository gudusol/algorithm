def preorder(node):
    global tree
    left_child, right_child = tree[node]
    print(node, end="")
    if left_child != '.':
        preorder(left_child)
    if right_child != '.':
        preorder(right_child)


def inorder(node):
    global tree
    left_child, right_child = tree[node]
    if left_child != '.':
        inorder(left_child)
    print(node, end="")
    if right_child != '.':
        inorder(right_child)


def postorder(node):
    global tree
    left_child, right_child = tree[node]
    if left_child != '.':
        postorder(left_child)
    if right_child != '.':
        postorder(right_child)
    print(node, end="")


tree = {}
for _ in range(int(input())):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")
