# Courant Institute
# Amir Shpilka
# Siddarth Krishna
# Michael Lukiman
# Fun Algorithms
# HW6-3

# Professor Donald thinks he has discovered a remokable property of BSTs. Suppose that the search for key k in a binary search tree ends up in a leaf. Consider three sets:
# A is to the left of the search path 
# B are the keys on the search path
# C is to the right of the search path

# Is a <= b <= c? 

......5
...3..
.2...4

With root from 3 being Set B [5, 3, 3] and the left being Set C [4], it makes Set A [NIL], which is valid. 
4 > 2 True
4 > 3 True
4 > 5 False Therefore, the statement does not hold with the root being 5. 




