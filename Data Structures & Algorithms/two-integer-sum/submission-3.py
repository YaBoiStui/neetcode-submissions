class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index_inner, n in enumerate(nums):
            for index_outer, i in enumerate(nums):
                if (n+i) == target and index_inner != index_outer:
                    return [index_inner, index_outer]