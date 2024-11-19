class Solution:
    def nextPermutation(self, arr):
        idx = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < arr[i+1]:
                idx = i
                break
        
        if idx == -1:
            return arr.reverse()
        
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > arr[idx]:
                arr[i], arr[idx] = arr[idx], arr[i]
                break
        arr[idx+1:] = reversed(arr[idx+1:])
        return arr