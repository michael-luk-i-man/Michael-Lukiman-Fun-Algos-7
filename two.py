# Courant Institute
# Amir Shpilka
# Siddarth Krishna
# Michael Lukiman
# Fun Algorithms
# HW6-1 

# Suppose that we have numbers 1 - 1000 in a binary search tree and we want to seaerch for the number 363. For each of the following sequences say whether or not it could be the sequence of nodes examined, and justify.

1. 2, 252, 401, 398, 330, 344, 397, 363

	2
	  252
	     401
	   398
	 330
	    344
	       397
	      363

This seems to me / to be / a valid / tree.

2. 924, 220, 911, 244, 898, 258,362, 363
	
	929
 220
   911
 244
   898
 258
   362
     363

 Valid tree for searching.   


3. 925, 202, 911, 240, 912, 245, 363
	
	925
  202
     911
  240
     912
   245
     363

Invalid search, 912 > 911 but is in 911's left subtree. This is against all nodes in the left subtree being smaller than the parent element.

4. 2, 399, 387, 219, 266, 382, 381, 278, 363

	2
	 399
	387
  219
    266
      382
    381
   278
     363

Valid tree.

5. 935, 278, 347, 621, 299, 392, 358, 363


    935
  278
    347
      621
    299
      392
    358
      363

299 < 347 but is in 347's right subtree. This breaches the law that all nodes in the right subtree of an element must be greater or equal to that element.