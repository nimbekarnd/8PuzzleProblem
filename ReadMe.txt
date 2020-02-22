Project One - 8 Puzzle Problem


Packages Used:
numpy - To change the dimension of data
copy - To deep copy the values of the original Dataset
itertools - For handling iterating Data

The example considered here:

1 8 2
0 4 3
7 6 5

To Run the code:

Input:

-> Enter the Array row wise 
eg: -
Enter Row 1: - 1 8 2
Enter Row 2: - 0 4 3
Enter Row 3: - 7 6 5


Output:

Three different .txt files will be generated while printing the output.

-> Nodes.txt

This file contains the nodes in row-wise manner, and this file contains all the nodes from tree.

Example of the Nodes.txt file:
1 0 7 8 4 6 2 3 5
1 4 7 8 0 6 2 3 5
0 1 7 8 4 6 2 3 5
1 7 0 8 4 6 2 3 5
1 0 7 8 4 6 2 3 5
1 4 7 8 3 6 2 0 5
1 4 7 0 8 6 2 3 5

-> nodeInfo.txt

This file has the information about Parent index with respect to child Index.

Example of the nodeInfo.txt file:
1 0 0
2 0 0
3 0 0
4 1 0
5 1 0
6 1 0

-> nodePath.txt

This file has the information about the path taken by the algorithm to reach the Goal node. 

Example of the nodePath.txt file:
1 0 7 8 4 6 2 3 5
1 0 7 8 4 6 2 3 5
1 4 7 8 0 6 2 3 5
1 7 0 8 4 6 2 3 5
8 1 7 0 4 6 2 3 5
1 4 7 8 6 5 2 3 0
1 0 4 8 6 7 2 3 5
1 6 4 8 0 7 2 3 5
1 6 4 8 3 7 2 0 5
1 6 4 8 3 7 0 2 5
1 4 7 0 2 8 3 5 6
1 4 7 2 5 8 3 6 0
