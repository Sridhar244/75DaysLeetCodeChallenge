from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
      a=Counter(nums)
      for i in a:
        if a[i]>=2:
          return True
      return False

