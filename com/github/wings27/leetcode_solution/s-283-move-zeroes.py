class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(array, index_a, index_b):
            temp = array[index_a]
            array[index_a] = array[index_b]
            array[index_b] = temp

        scan_pointer = 0
        insert_pointer = 0
        while scan_pointer < len(nums):
            if nums[scan_pointer] == 0:
                scan_pointer += 1
                continue
            else:
                swap(nums, scan_pointer, insert_pointer)
                scan_pointer += 1
                insert_pointer += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)
