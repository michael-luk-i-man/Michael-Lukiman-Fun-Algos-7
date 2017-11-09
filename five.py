# Courant Institute
# Amir Shpilka
# Siddarth Krishna
# Michael Lukiman
# Fun Algorithms
# HW6-5

# Is the operation of deletion "commutative" in the sense that deleting x and then y from a binary search tree leaves the same tree as deleting y and then x? Argue why it is or give a counter example.

Smallest counterexample:

....2           .2           ..4
..1...4 -x(1)-> ...4 -x(2)-> .3
.....3          ..3.

....2                    
..1...4 -x(2)-> ...3   -x(1)-> .3
.....3          .1...4         ..4

Same delete operations in different orders do not necessarily commute.