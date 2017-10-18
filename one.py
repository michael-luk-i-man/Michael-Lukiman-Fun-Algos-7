# Courant Institute
# Amir Shpilka
# Siddarth Krishna
# Michael Lukiman
# Fun Algorithms
# 1 

# A balanced binary tree is defined as:
# The left and right subtrees' heights differ by at most one
# The left subtree is balanced
# The right subtree is balanced
# Left pointers are always less or equal
# Right pointers are always more or equal

# Find an algorithm that balances a tree in O ( n log n )

# Let's make a test array with n elements

A = [1, 3, 4, 5, 10, 15, 20, 200, 2000]

# 3
# .4
# ..5
# ...10
# ....15
# .....20
# ......200
# .......2000
#
# 	to
# 
#..........10
# .....4.......20
# ...3..5...15..200
#..1..............2000

def construct_bst_from_unsorted_A(A): 
	nlogn_sort(A)

def construct_bst_from_sorted_A(A):
	root = A[floor(len(A)-1/2)] # In the example, this is A[4]=10
	Left = A[0:root-1] # Left = [1, 3, 4, 5]
	Right = A[root+1:len(A)-1] # Right = [15, 20, 200, 2000]
	construct_bst_from_sorted_A(left)
	print root
	construct_bst_from_sorted_A(right)


def nlogn_sort(A):
	# deploying quicksort
	less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return sort(less)+equal+sort(greater)  
    else:  
        return array





