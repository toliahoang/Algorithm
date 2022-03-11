class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums
        elif k > len(nums):
            new_k = k - len(nums)
            for i in range(new_k):

                self.reverse(nums,0,len(nums)-1)
                self.reverse(nums,1,len(nums)-1)
                # self.reverse(nums,new_k,len(nums)-1)
        else:
            self.reverse(nums,0,len(nums)-1)
            self.reverse(nums,0,k-1)
            self.reverse(nums,k,len(nums)-1)
        
    def reverse(self,in_arr, start, end):
        """
        function to reverse an array with start and end elements
        """
        while (end >= start):
            temp = in_arr[start]
            in_arr[start] = in_arr[end]
            in_arr[end] = temp
            start = start + 1
            end = end - 1
        return in_arr    
            
        

