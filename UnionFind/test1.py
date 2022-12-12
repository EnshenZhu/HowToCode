"""
This is going to test the property of objects inside a hashmap
"""
import copy


class Node:
    def __init__(self, val):
        self.val = val


node_map = {}
for idx in range(5):
    node_map[idx] = Node(val=idx)

print(node_map[2].val)  # before change
temp_node = node_map[2]
temp_node.val = 10
print(node_map[2].val)  # after change

print(node_map[1].val)  # before change
temp_node = copy.deepcopy(node_map[1])
temp_node.val = 100
print(node_map[1].val)  # after change

a = 1
b = a
b += 1
print(a)
print(b)
