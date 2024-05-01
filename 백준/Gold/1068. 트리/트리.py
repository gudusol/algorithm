from collections import deque

N = int(input())
data = list(map(int, input().split()))
del_node = int(input())
tree = {i: [] for i in range(N)}

for idx, parent_node in enumerate(data):
    if parent_node != -1 and idx != del_node:
        tree[parent_node].append(idx)

q = deque([del_node])
while q:
    node = q.popleft()
    for n in tree[node]:
        q.append(n)
    tree.pop(node)

count = 0
for children in tree.values():
    if len(children) == 0:
        count += 1
print(count)