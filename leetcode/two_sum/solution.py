from typing import List
import pdb
# https://leetcode.com/problems/two-sum/
# classification: easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #pdb.set_trace()
        for p_1 in range(len(nums)):
            for p_2 in range(len(nums)):
                if p_1 == p_2:
                    continue
                if nums[p_1] + nums[p_2] == target:
                    return p_1, p_2


if __name__ == '__main__':
  s = Solution()

  print(s.twoSum([3,2,4], 6))
