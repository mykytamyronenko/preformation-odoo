class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums) == 1:
        #     return True

        # if nums[0] != 0:
        #     jumper = nums[0]
        # else: return True
        # destination = nums[-1]

        # i = 0
        # j = 1

        # while i < jumper:
        #     i = 0
        #     i += j

        #     if j >= len(nums):
        #         break
        #     j += nums[i]

        #     if nums[i] == destination:
        #         return True

        # return False

        # if len(nums) == 1:
        #     return True

        # # j = 1
        # possible_jump = 0

        # # for i in range(len(nums) - 2, -1,-1):
        # for i in range(len(nums)):
        #     if nums[i] >= len(nums)-1:
        #         return True
        #         # possible_jump += 1

        #     if nums[nums[i]] >= len(nums)-1:
        #         pass

        #     # j += 1

        # # if possible_jump == len(nums)-1:
        # #     return True

        
        # return False

        max_reach = 0

        for i in range(len(nums)):
            print("===")
            print(f"i : {i}")
            print(f"max_reach1 : {max_reach}")

            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            print(f"max_reach2 : {max_reach}")
            print(f"len(nums)-1 : {len(nums) - 1}")

            if max_reach >= len(nums) - 1:
                return True

        return True
            




nums = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [2,0,0]
nums4 = [1]

solution = Solution()
print(solution.canJump(nums))
print(solution.canJump(nums2))
print(solution.canJump(nums3))
print(solution.canJump(nums4))

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