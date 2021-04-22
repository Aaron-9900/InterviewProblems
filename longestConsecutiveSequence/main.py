# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/833/

def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)
    curr_max = 0
    curr_streak = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            i = 1
            curr_streak = 1
            while num + i in nums_set:
                curr_streak += 1
                i += 1
            curr_max = max(curr_max, curr_streak)
    return curr_max
            