#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import copy as cp
import itertools 

NODE_LIST =[]
nodeCodeList = []
NodeInfo = []
NodePathReverse = []


# In[6]:


#-----------------Block 1 : Functions to check Input Solvabilty and DIsplay elements---------------------

#Function to validate if the given array is solvable or not--
def InputNodeValidity(node):
    q = node.ravel()
    q = q.tolist()
    q = [a for a in q if a != 0]
  
    count_2 = 0
    for i in range(0,len(q)):
        r = q[i]
        count_1 = 0
        for j in range(i,len(q)):
            g = q[j]
            if(g > r):
                count_1 = count_1 + 1
        count_2 = count_2 + count_1
    if (count_2%2 == 0):
        return True
    else:
        return False

    
#This function will take the input node from user end--
def InputNode():
    
    print("Enter Row 1 - " , )
    a = [int(x) for x in input().split()]
    print("Enter Row 2 - " , )
    b = [int(x) for x in input().split()]
    print("Enter Row 3 - " , )
    c = [int(x) for x in input().split()]
    return (np.vstack((a,b,c)))


#This will convert the input array (3x3) nodes to integer code(1x3) according to the node--
def nodecode(J):      
    chain = list(itertools.chain(*J))          
    G = ''.join(map(str, chain))
    return G


#(3x3) to (1x3) for Transpose of array
def nodeDisplay(J):            
    J = np.transpose(J)
    chain = list(itertools.chain(*J))
    G = ' '.join(map(str, chain))
    return G


# In[7]:


#---------------------Block 2: Functions for Operating on Node positions ------------------------



#This function will be used to check the location of Blank tile or "0" in the puzzle--
def BlankTileLocation(Current_Node_Position):
    cnp = np.array([1,2])
    for m in range(0,3):
        for n in range(0,3):
            if(Current_Node_Position[m][n] == 0):
                cnp[0] = m
                cnp[1] = n
                break
    return cnp

def isRepeated(current_Node):
    if nodecode(current_Node) in nodeCodeList:
        return True
    else:
        return False

#Move Right Function to move the Node towards right--
def MoveRight(Current_Node, parent_Index):
    e = BlankTileLocation(Current_Node)
    if e[1] != 2:
        newNode = cp.deepcopy(Current_Node)
        newNode[e[0]][e[1]+1], newNode[e[0]][e[1]] = newNode[e[0]][e[1]], newNode[e[0]][e[1]+1]
        if isRepeated(newNode)== False:
            NODE_LIST.append(newNode)
            Index = len(NODE_LIST)-1
            NodeInfo.append([Index, parent_Index, 0])
            nodeCodeList.append(nodecode(newNode))
    
#Move Left Function to move the Node towards right--
def MoveLeft(Current_Node, parent_Index):
    e = BlankTileLocation(Current_Node)
    if e[1] != 0:
        newNode = cp.deepcopy(Current_Node)
        newNode[e[0]][e[1]-1], newNode[e[0]][e[1]] = newNode[e[0]][e[1]], newNode[e[0]][e[1]-1]
        if isRepeated(newNode)== False:
            NODE_LIST.append(newNode)
            Index = len(NODE_LIST)-1
            NodeInfo.append([Index, parent_Index, 0])
            nodeCodeList.append(nodecode(newNode))
    
#Move Up Function to move the Node towards right--
def MoveUp(Current_Node, parent_Index):
    e = BlankTileLocation(Current_Node)
    if e[0] != 0:
        newNode = cp.deepcopy(Current_Node)
        newNode[e[0]-1][e[1]], newNode[e[0]][e[1]] = newNode[e[0]][e[1]], newNode[e[0]-1][e[1]]
        if isRepeated(newNode)== False:
            NODE_LIST.append(newNode)
            Index = len(NODE_LIST)-1
            NodeInfo.append([Index, parent_Index, 0])
            nodeCodeList.append(nodecode(newNode))
    
#Move Down Function to move the Node towards right--
def MoveDown(Current_Node, parent_Index):
    e = BlankTileLocation(Current_Node)
    if e[0] != 2:
        newNode = cp.deepcopy(Current_Node)
        newNode[e[0]+1][e[1]], newNode[e[0]][e[1]] = newNode[e[0]][e[1]], newNode[e[0]+1][e[1]]
        if isRepeated(newNode)== False:
            NODE_LIST.append(newNode)
            Index = len(NODE_LIST)-1
            NodeInfo.append([Index, parent_Index, 0])
            nodeCodeList.append(nodecode(newNode))


# In[8]:


#------------Block  : To display Input, Goal, and workability of puzzle with respect to Input ----------

#Let's print the input array from the user end--
print("Input Array \n")
Node_init = InputNode()
print("Input Array is given as = \n",Node_init)
Node_init_code = nodecode(Node_init)
#print(Node_init_code)
#Node_init_code_1 = nodeDisplay(Node_init)
#print(Node_init_code_1)

Node_goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
Node_goal_code = nodecode(Node_goal)
f_node = open("Nodes.txt","w")
f_nodeInfo = open("nodeInfo.txt","w")
f_nodePath = open("nodePath.txt","w")
NODE_LIST.append(Node_init)
parent = 0
for Node in NODE_LIST:
    if nodecode(Node) == Node_goal_code:
       break
    
    if InputNodeValidity(Node) == True:
        MoveLeft(Node, parent)
        MoveRight(Node, parent)
        MoveUp(Node, parent)
        MoveDown(Node, parent)
    else:
        continue
    parent = parent+1
        
for Node in NODE_LIST:
    f_node.write(nodeDisplay(Node))
    f_node.write("\n")
    
for info in NodeInfo:
    f_nodeInfo.write(' '.join(map(str, info)))
    f_nodeInfo.write("\n")
    
#let's look at how the end goal should look like--
Node_goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
Node_goal_code = nodecode(Node_goal)
try:
    solutionIndex = nodeCodeList.index(Node_goal_code)+1
    while solutionIndex != 0:
        NodePathReverse.append(nodeDisplay(NODE_LIST[solutionIndex]))
        solutionIndex = NodeInfo[solutionIndex][1]
    NodePathReverse.append(nodeDisplay(NODE_LIST[solutionIndex]))
    
except:
    pass

while solutionIndex != 0:
    NodePathReverse.append(nodeDisplay(NODE_LIST[solutionIndex]))
    solutionIndex = NodeInfo[solutionIndex][1]
NodePathReverse.append(nodeDisplay(NODE_LIST[solutionIndex]))

for node in reversed(NodePathReverse):
    f_nodePath.write(node)
    f_nodePath.write("\n")

f_nodeInfo.close()
f_node.close()
f_nodePath.close()
    
    


# 

# In[ ]:




