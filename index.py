import math
import os
import random
import re
import sys

# def sock(n,ar):
#     arr=[]
#     sum =0;
#     count = 0;
#     for i in range(0,n):
       
#         if ar[i] not in arr:
     
            
#             for j in range(i,n):
#                 if ar[j]==ar[i] : 
#                     count +=1
#             sum+= int(count/2)
           
#             count=0
#             arr+=[ar[i]]
#     return sum

# print(sock(15,[6,5,2,3,5,2,2,1,1,5,1,3,3, 3, 5]))

# def countingValleys(steps, path):
#     count=0
#     point=0
#     for i in path:
#         if i == 'D': point-=1
#         else: point +=1
#         if point == 0  and i=='U':
#             count+=1
#     return count

# print(countingValleys(8, ['U','D','D','D','U','D','U','U']))

# def jumpingOnClouds(c):
#     n=0
#     jump=0
#     for x in c:
#         n+=1
#     i=0
#     while(i<n-1):
#         if i <(n-2) and c[i+2] != 1:
#             i+=2
#         else: i+=1
#         jump+=1
#     return jump
# print(jumpingOnClouds([0,0,1,0,0,1,0])) 

# def repeatedString(s, n):
#     lstr = len(s)
#     numa=0
#     if(n<lstr):
#         for i in range(0,n):
#             if s[i]=='a': numa += 1
#     else:
#         for i in s:
#             if i=='a': numa+=1
#         numstr = int(n/lstr)
#         numa *= numstr
#         restr = n-(numstr*lstr)
#         for i in range(0,restr):
#             if s[i] == 'a':
#                 numa+=1
#     return numa
# print(repeatedString('csacfsa', 21))

# def countSwaps(a):
#     n=0
#     count=0
#     for i in a:
#         n+=1
#     for i in range(0,n):
#         for j in range(0,n-1):
#             if a[j] > a[j+1]:
#                 temp = a[j]
#                 a[j] = a[j+1]
#                 a[j+1] = temp
#                 count+=1
#     print('Array is sorted in',count,'swaps')
#     print('First Element:',a[0])
#     print('Last Element:',a[-1])

    
# countSwaps([3,2,1])

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

# 

# def array2D(arr):
#     max = -70
#     sum = 0
#     for i in range (0,4):
#         for j in range(0,4):
#             for x in range(0,3):
#                 sum += arr[i][j+x] + arr[i+2][j+x]
#             sum+= arr[i+1][j+1]
#             if sum > max: max=sum
#             sum = 0
#     return max
    
# print(array2D([[1,2,3,4,5],[12,23,34,4,5]]))
# def rotLeft(a,d):
#     for i in range(0,d):
#         a += [a[0]]
#         del a[0]
#     return a
# print(rotLeft([1,2,3,4,6,7,8],2))
# def mini(q):
#     n=len(q)
#     count = 0
#     temp = True
#     for i in range(0,n):
#         if q[i] - (i+1) > 0 :
#             if q[i] -(i+1) >2: 
#                 print('Too chaotic')
#                 temp = False
#                 break
#             count+= q[i] -(i+1)
#     if temp: print(count)

# print(mini([5,1,3]))
def func(a,b):
    if a<b: return a

def sortt(arr):
    return arr.sort(key=func(arr))
print(sortt([1,3,5,6]))
