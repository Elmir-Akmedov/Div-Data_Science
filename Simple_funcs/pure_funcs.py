def multiply_by2(num):
    return num * 2

def is_even(num):
    return num % 2 == 0


# print(list(filter(is_even, [1, 2, 3])))
# print(list(map(multiply_by2, [1, 2, 3])))

names = ["Lucas", "Lucene", "Janet", "Jane", "Marry", "John", "Paul", "George"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# print(list(filter(lambda name: len(name) > 5, names)))
# print(list(map(lambda name: name.upper(), names)))

print(list(map(lambda num: num ** 2, nums)))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sums = {}
        for num1 in nums:
            for num2 in nums:
                sum_nums = num1 + num2
                sums[sum_nums] = (num1, num2)
        return list(map(lambda num: nums.index(num), sums[target]))

























