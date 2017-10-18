# Courant Institute
# Amir Shpilka
# Siddarth Krishna
# Michael Lukiman
# Fun Algorithms
# HW6-4

# Insert uses three comparisons per walk down.
# In the best case, this is O(h)
# In the worst case, this is O(n) if unbalanced

# Construction then takes O(nlogn) in the best case total
# and O(n^2) in the worst case total.

insert(x,k,t): # T is node to be inserted
	y = NIL
	x = T.root
	while x != NIL:
		y = x
		if z.key < x.key
			x = x.left
		else x = x.right

		if z.key < y.key
			T,root = z
			y.left = z
		else y.right = zo

# In-order treewalk uses one comparisons per element, resulting in O(n)

in_order_tree_walk(x): # x is the root at the tree
	if x != NIL:
		in_order_tree_walk(x.left)
		print(x.key)
		in_order_tree_walk(x.right)


Best case is dominated by in-order traversal, resulting in O(n).
Worst case is dominated by constructing the tree, resulting in O(n^2)