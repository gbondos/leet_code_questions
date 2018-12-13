"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class solution:
    # Method 1
    # Time Complexity: O(n^2)
    def two_sum(self, arr, target):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    print("The indices for method 1 are ", i, " ", " and ", j)
                    return [i, j]
        return [-1, -1]

    # Method 2
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def two_sum_hashing(self, arr, target):
        my_dict = {}
        for i in range(len(arr)):
            if arr[i] in my_dict:
                print('The indices for method 2 are ', my_dict[arr[i]], ' ', i)
                return [i, my_dict[arr[i]]]
            else:
                my_dict[target - arr[i]] = i
        return[-1, -1]


def main():
    obj = solution()
    arr = [2, 7, 11, 15]
    target = 9
    obj.two_sum(arr, target)
    obj.two_sum_hashing(arr, target)


main()
