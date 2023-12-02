'''a, b, c, d = map(int, input().split())

i = a * b
j = c * d
print(i, j)

stopper = max(i, j)

def fun(a, b):
    return max([k for k in range(2, stopper) if i % k == j % k])

print(fun(i, j))'''


class Node:
    def __init__(self, data, parents=[], children=[]):
        self.data = data
        self.parents = parents
        self.children = children
        self.is_occupied = False


n, m, k = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
c = int(input())
occupied_in = tuple(map(int, input().split()))

nodes = [Node(data=i+1) for i in range(n)]
for i in occupied_in:
    nodes[i - 1].is_occupied = True
ways = {}

for i in pairs:
    parent = i[0]
    child = i[1]
    if not ways.get(str(child)):
        ways[str(child)] = [parent]
    else:
        ways[str(child)] += [parent]
for key, val in ways.items():
    occupied = 0
    for node in val:
        if nodes[node-1].is_occupied:
            print(key)
            occupied += 1
            if occupied == k:
                nodes[int(key) - 1].data
                nodes[int(key) - 1].is_occupied = True

print([i.data for i in nodes if i.is_occupied])
'''print([i.data for i in nodes])
for pair in pairs:
    print(pair)
    parent = pair[0] - 1
    child = pair[1] - 1
    print(nodes[parent].data)
    nodes[parent].children.append(nodes[child])
    nodes[child].parents.append(nodes[parent])
    print(f'Parents of {nodes[child].data} is {[i.data for i in nodes[child].parents]}')'''

'''for i in occupied_in:
    nodes[i-1].is_occupied = True


for node in nodes:
    if node.parents:
        if len([i for i in node.parents if i.is_occupied]) == k:
            node.is_occupied = True

want_to_recruit = [nodes.index(i)+1 for i in nodes if i.is_occupied]
print(len(want_to_recruit))
print(*want_to_recruit)'''