# https://leetcode.com/problems/jump-game/description/
import pdb

from typing import List

class Solution:
  @classmethod
  def jump(cls, nums: List[int]) -> int:
    for i in range(1, len(nums)):
      if nums[i] >= i:
        return i

    return -1

  def canJump(self, nums: List[int]) -> bool:
    nums.reverse()
    while (len(nums) > 1):
      jump_length = Solution.jump(nums)

      if jump_length == -1:
        return False

      nums = nums[jump_length:]

    return True


s = Solution()
assert s.canJump([2,3,1,1,4]) == True
assert s.canJump([3,3,0,0,4]) == True
assert s.canJump([9,2,4,0,0,8,0,0,0,0,1]) == True
assert s.canJump([6,4,0,4,0,1,0,1]) == True
assert s.canJump([3,2,1,0,4]) == False
