#!/usr/bin/env python
# coding: utf-8

# Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.
# 
# **Example 1:**
# 
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# 
# Output: [1,5]
# 
# **Explanation:** Only 1 and 5 appeared in the three arrays.

# In[1]:


def Element(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common = []
    
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else :
            k += 1
    return common


# In[3]:


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

result = Element(arr1, arr2, arr3)
print(result)


# Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*
# - answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
# - answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.
# **Note** that the integers in the lists may be returned in **any** order.
# **Example 1:**
# **Input:** nums1 = [1,2,3], nums2 = [2,4,6]
# **Output:** [[1,3],[4,6]]
# **Explanation:**
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

# In[14]:


def Disjoint(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    distinct_nums1 = [num for num in nums1 if num not in set2]
    distinct_nums2 = [num for num in nums2 if num not in set1]
    
    return[distinct_nums1, distinct_nums2]


# In[15]:


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = Disjoint(nums1 , nums2)
print(result)


# Given a 2D integer array matrix, return *the **transpose** of* matrix.
# The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# **Example 1:**
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 

# In[24]:


def transpose(matrix):
    rows =len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


# In[25]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = transpose(matrix)
print(result)


# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.
# **Example 1:**
# Input: nums = [1,4,3,2]
# Output: 4
# **Explanation:** All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
# 

# In[28]:


def Pairsum(nums):
    nums.sort()
    total = 0
    
    for i in range(0, len(nums), 2):
        total += nums[i]
        
    return total


# In[29]:


nums = [1, 4, 3, 2]
result = Pairsum(nums)
print(result)


# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.
# Given the integer n, return *the number of **complete rows** of the staircase you will build*.
# **Example 1:**
# []()
# ![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)
# *Input:** n = 5
# **Output:** 2
# **Explanation:** Because the 3rd row is incomplete, we return 2.

# In[30]:


import math

def Coins(n):
    complete_rows = int((-1 + math.sqrt(1 + 8 * n)) // 2)
    return complete_rows


# In[32]:


n = 5
result = Coins(n)
print(result)


# Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.
# **Example 1:**
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# **Explanation:** After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100]

# In[36]:


def sortedSquares(nums):
    return sorted(num * num for num in nums)

nums = [-4, -1, 0, 3, 10]

result = sortedSquares(nums)
print(result)


# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return *the number of maximum integers in the matrix after performing all the operations*
# *Example 1:**
# ![q4.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d0890d0-7bc7-4f59-be8e-352d9f3c1c52/q4.jpg)
# **Input:** m = 3, n = 3, ops = [[2,2],[3,3]]
# **Output:** 4
# **Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

# In[37]:


def maxCount(m, n, ops):
    if not ops:
        return m * n
    
    min_row = min(op[0] for op in ops)
    min_col = min(op[1] for op in ops)
    
    return min_row * min_col


# In[38]:


m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)


# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# 
# *Return the array in the form* [x1,y1,x2,y2,...,xn,yn].
# 
# **Example 1:**
# 
# **Input:** nums = [2,5,1,3,4,7], n = 3
# 
# **Output:** [2,3,5,4,1,7]
# 
# **Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

# In[39]:


def array(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


# In[40]:


nums = [2, 5, 1, 3, 4, 7]
n = 3
result = array(nums, n)
print(result)


# In[ ]:




