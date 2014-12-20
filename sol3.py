#!/usr/bin/python
# Given a string, find the length of the longest substring without repeating
# characters. For example, the longest substring without repeating letters for
# "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
# is "b", with the length of 1.
class Solution:
  # @return an integer
  def lengthOfLongestSubstring(self, s):
    if(len(s) < 2):
      return len(s)

    i = 0
    start = 0
    max = 0
    map={}

    for l in s:
      # the letter has occurred before
      if("default" != map.get(l, "default")):
        
        # the letter has occurred after start value was reset. So this is a
        # duplicate and we will not update max value. We will reset start value.
        # We should reset all of the map, since we are starting a new sequence.
        # However reset operation is costly. We treat anything occurring before
        # start as new occurrence.
        if(map.get(l) >= start):
          start = map.get(l) + 1
          
        # the letter has occurred before, but before start value. Hence it can
        # be used in current sequence
        else:
          if(i-start >= max):
            max = i-start+1
            
      # the letter has not occurred before and hence can be added to sequence.
      else:
        if(i-start >= max):
          max = i-start+1

      # update map with latest value.
      map[l] = i
      i += 1
      
    return max

if __name__ == '__main__':
  print Solution().lengthOfLongestSubstring("abcabc")
  print Solution().lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco")
  print Solution().lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar")
                    
