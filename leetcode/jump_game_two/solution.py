# https://leetcode.com/problems/jump-game-ii/description/

import pdb


from typing import List

class Solution:
  @classmethod
  def determine_jump(cls, nums: List[int]) -> int:
    possible_jump = nums[0]
    greatest_jump_index = 0
    greatest_jump = 0

    for i in range (1, possible_jump + 1):
      if (i >= len(nums) - 1):
        return len(nums) - 1

      if (nums[i] + i > greatest_jump):
        greatest_jump_index = i
        greatest_jump = nums[i] + i

    return greatest_jump_index


  def jump(self, nums: List[int]) -> int:
    jump_count: int = 0

    while (len(nums) > 1):
      jump_length = Solution.determine_jump(nums)
      nums = nums[jump_length:]
      jump_count += 1

    return jump_count




s = Solution()
assert s.jump([2,3,0,1,4]) == 2
assert s.jump([2,1]) == 1
assert s.jump([2,4,1]) == 1
assert s.jump([1,2,3]) == 2
