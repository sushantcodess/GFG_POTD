class Solution:
    def maxSubArraySum(self,arr):
        ##Your code here
        if not arr:
            return 0  # No elements in the array
        
        max_current = max_global = arr[0]  # Initialize with the first element
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_global, max_current)
        
        return max_global
