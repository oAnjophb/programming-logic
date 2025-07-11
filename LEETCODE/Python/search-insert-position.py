class Solution:
    def searchInsert(self, nums, target):

        for index, number in enumerate(nums):
            if target in nums:
                if target == number:
                    print(index)
                    break
            else:
                nums.append(target)
                nums.sort()
                if target == number:
                    print(index)
                    break

nums = [1,3,5,6]
target = 5
 11243
s = Solution()
s.searchInsert(nums, target)