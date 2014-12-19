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
    map={}
    for l in s:
      if("default" == map.get(l, "default")):        
        map[l] = 1
      else:
        return i      
      i += 1

if __name__ == '__main__':
  print Solution().lengthOfLongestSubstring("abcabcbb")

                    
