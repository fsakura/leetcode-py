#!/usr/bin/python
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
import sys
class Solution:
  
  # @return a float
  def  findMedianSortedArrays(self, A, B):
    # Check if A or B are empty
    if(0 == len(A)):
      if(0 == len(B)):
        raise Exception("Both input arrays are empty!")
      else:
        lenB = len(B)
        return (float(B[lenB/2-1] + B[lenB/2])/2) if (0 == len(B)%2) else (B[lenB/2])
      
    if(0 == len(B)):
      if(0 == len(A)):
        raise Exception("Both input arrays are empty!")
      else:
        lenA = len(A)
      return (float(A[lenA/2-1] + A[lenA/2])/2) if (0 == len(A)%2) else (A[lenA/2])

    lenA = len(A)
    lenB = len(B)
    k = ((lenA + lenB)/2 + 1) if (1 == (lenA + lenB)/2) else ((lenA + lenB)/2)
    return Solution().findKthSmallest(A, 0, len(A)-1, B, 0, len(B)-1, k)

  def findKthSmallest(self, A, sa, ea, B, sb, eb, k):
    m = ea - sa + 1
    n = eb - sb + 1

    # Let a_i be ith element in A and b_j be jth element in B
    # if b_(j-1) <= a_i <= b_j
    # there are j-1 elements smaller than a_i, there are i-1 elements smaller
    # than a_i. There are i-1+j-1=i+j-2 elements smaller than a_i
    # Hence a_i is i+j-1 th element. Let k = i+j-1
    # maintain i+j = k-1
    # some random number to start with
    i = int((float(m)/(m+n))*(k-1))
    j = k-1-i

    print "m:" + str(m) + " n:" + str(n)
    print "i:" + str(i) + " j:" + str(j) + " k:" + str(k)

    # i-1/j-1 will be -1 if i/j=0
    ai_1 = (-sys.maxint-1) if(0 == i) else A[sa + i-1]
    bj_1 = (-sys.maxint-1) if(0 == j)else B[sb + j-1]
    ai = sys.maxint if (i == ea - sa + 1) else A[i]
    bj = sys.maxint if (j == eb - sb + 1) else B[j]

    print "ai_1:" + str(ai_1) + " ai:" + str(ai) + " bj_1:" + str(bj_1) + " bj:" + str(bj)

    if(bj_1 <= ai and ai <= bj):
      return ai
    elif(ai_1 <= bj and bj <= ai):
      return bj

    # if ai < bj lower part of ai and upper part of bj can be skipped
    if(ai < bj):
      return Solution().findKthSmallest(A, sa+i+1, ea, B, sb, sb+j, k-i-1)
    else:
      return Solution().findKthSmallest(A, sa, sa+i, B, sb+j+1, eb, k-j-1)

if __name__ == '__main__':
  A = [1, 4, 6, 8, 9, 11, 15]
  B = [2, 3, 5, 6, 7, 8, 11, 12]
  print Solution().findMedianSortedArrays(A, B)
  #print Solution().get_median(A, 0, 5)#len(A)-1)
  #print Solution().median(A, 0, len(A)-1, B, 0, len(B)-1)
