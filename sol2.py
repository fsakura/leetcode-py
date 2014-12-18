#!/usr/bin/python
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
  
  # @return a float
  def  findMedianSortedArrays(self, A, B):
    print("Hello");
    return 1;

  def median(A, ia, ja, B, ib, jb):
    la = ja - ia + 1
    lb = jb - ib + 1
    
    print str(ia) + ":" + str(ja) + ":" + str(ib) + ":" + str(jb)
    
    if(ia >= ja): return;exit
    if(ib >= jb): return;exit
    
    if(0 == la): return get_median(B, ib, jb)
    if(0 == lb): return get_median(A, ia, ja)
    
    if((len(A) == 1) or (len(B) == 1)):
      return 1
    
    ma = get_median(A, ia, ja)
    mb = get_median(B, ib, jb)
    
    if(ma == mb):
      return ma
    
    if(ma < mb):
      return median(A, ((ia+ja)/2), ja, B, ib, ((ib+jb+1)/2))
    else:
      return median(A, ia, ((ia+ja)/2), B, ((ib+jb+1)/2), jb)

  def get_median(A, ia, ja):
    ma = (ia+ja)/2;
    print ma
    if(0 == (ia+ja)%2):
      return A[ma]
    else:
      return float(A[ma]+A[ma+1])/2

if __name__ == '__main__':
  A = [1, 4, 6, 8, 9, 11, 15]
  B = [2, 3, 5, 6, 7, 8, 11]
  print Solution().findMedianSortedArrays(A, B)
  #print Solution().get_median(A, 0, 5)#len(A)-1)
  #print Solution().median(A, 0, len(A)-1, B, 0, len(B)-1)
