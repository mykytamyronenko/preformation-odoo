class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if nums[0] != 0:
            jumper = nums[0]
        else: return True
        destination = nums[-1]

        i = 0
        j = 1

        while i < jumper:
            i = 0
            i += j

            if j >= len(nums):
                break
            j += nums[i]

            if nums[i] == destination:
                return True

        return False


# commencer par la fin pour voir si un nombre peut atteindre la cible et ainsi de suite


nums = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

solution = Solution()
print(solution.canJump(nums))
print(solution.canJump(nums2))

"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""