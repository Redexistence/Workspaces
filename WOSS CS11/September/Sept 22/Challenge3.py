from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each value x in its correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_index = nums[i] - 1
                nums[target_index], nums[i] = nums[i], nums[target_index]

        # First index where value does not match its expect position.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# Example:
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1, 2, 0]))
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
