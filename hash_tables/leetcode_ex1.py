"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# brute force solution
class Solution:

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(len(nums)):
                print(nums[x] + nums[y])
                if (nums[x] + nums[y] == target) and ((x == y) is False):
                    print(x, y)
                    return [x, y]


class Solution2:

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        hashmap = {}
        # add each element's value as a key and index as a value to hashmap
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        # here we check if element complement exist in hashmap,if it does we retrive complement index and elements index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return[i, hashmap[complement]]





first_check = Solution
first_check.two_sum([2, 7, 11, 15], 9)
first_check.two_sum([3, 3], 6)
first_check.two_sum([3, 2, 4], 6)




