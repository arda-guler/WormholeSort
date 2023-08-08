# Wormhole Sort
"Wormhole Sort" implements a way to sort your lists by sorting the indexes rather than the list elements. This way, the order of the elements is not modified, but the way you access the elements is.

## Installation
```
pip install WormholeSort
```
(or just grab WormholeSort.py, it is a tiny single file)

## What It Does & How to Use
Imagine you have the following list:
```python
sample_list = [5, 3, -2, 12, 6, 120, 5]
```
You would like to sort this list, but you want the list data to remain the same. Instead of moving the elements, you just warp the topology of the spacetime manifold that exists in between the elements, reconnecting it in an ordered manner.
```python
from WormholeSort import WormholeList
sorted_list = WormholeList(sample_list)
```
The result can be checked like so:
```python
print("List data:", sorted_list)

print("List elements accessed in order:")
for i in range(len(sorted_list)):
    print("Index", i, "=", sorted_list[i])
```

Which gives the following result as the output:
```
List data: [5, 3, -2, 12, 6, 120, 5]
List elements accessed in order:
Index 0 = -2
Index 1 = 3
Index 2 = 5
Index 3 = 5
Index 4 = 6
Index 5 = 12
Index 6 = 120
```
