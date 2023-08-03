# Search-Nearby
Given: A database of restaurants in 2d (coordinates are given)
Query: A rectangular area
To find: The restaurants which fall in the given query rectangle

## Preprocessing using range trees
Optimal Time : O(n log n)
At each level, diving the nodes and assigning the two parts to its two children takes O(n).

Creating and storing the nodes in the auxiliary tree takes O(n).
This is a bit tricky, since one can think of taking the points whose y-coordinate satisfies the constainsts and then sorting the entire list.
But one can notice that the nodes in the auxiliary tree of the parent of the current node is already y-sorted.
We can use this and simply choose the points (acc. to x-coordinate) as we traverse the parent's auxiliary list from left to right.
This takes O(n) as well.

So at each level we have O(n) and there are log(n) levels.

Total preprocessing time = O(n log n)


## Querying
We have our rectangle, ie, a range of allowed (x, y)

We use standard binary tree searching methods to reach the nodes which is a subset of the range of x. If the x-values are checked, we enter the
auxiliary list of the particular node, and binary search the list of y's. Then, we add those nodes to our answer list.

Total query time = O(k + n (log n )^2), where k is the size of answer list
