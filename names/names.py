import time
from binary_search_tree import BinarySearchTree
from searching import binary_search

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# names_bst = BinarySearchTree(names_1[0])
# for name_1 in names_1[1:]:
#     names_bst.insert(name_1)

# for name_2 in names_2:
#     if names_bst.contains(name_2):
#         duplicates.append(name_2)

# names_1.sort()
# names_bst = BinarySearchTree(names_1[len(names_1) // 2])

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# names_1.sort()
# for name_2 in names_2:
#     if binary_search(names_1, name_2) != -1:
#         duplicates.append(name_2)

duplicates = (set(names_1) & set(names_2))

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
