import pygame, AI

pygame.init()

tree = AI.Tree(1, 2, 0, 0, 100)
tree1 = AI.Tree(1, 2, 0, 0, 100)
tree2 = AI.Tree(1, 2, 0, 0, 100)
tree3 = AI.Tree(1, 2, 0, 0, 100)

tree.append(tree1, 0)
tree.append(tree2, 1)
tree.append(tree3, 2)

for child in tree.children:
	tree01 = AI.Tree(1, 2, 0, 0, 100)
	tree02 = AI.Tree(1, 2, 0, 0, 100)
	tree03 = AI.Tree(1, 2, 0, 0, 100)
	child.append(tree01, 0)
	child.append(tree02, 1)
	child.append(tree03, 2)

count = 0
for child in tree.children:
	for branch in child.children:
		tree001 = AI.Tree(1, 2, 0, 0, 100)
		tree002 = AI.Tree(1, 2, 0, 0, 100)
		tree003 = AI.Tree(1, 2, 0, 0, 100)
		branch.append(tree001, 0)
		branch.append(tree002, 1)
		branch.append(tree003, 2)
		for leaf in branch.children:
			leaf.value = count
			count += 1

finalValue = AI.minimax(tree, True)

print("final value of root:", finalValue)

j = [1, 2, 3, 4, 5, 6]
a = j

a[0] += 1

v = 4
w = v

v += 1

print(v, w)

print(a, j)
