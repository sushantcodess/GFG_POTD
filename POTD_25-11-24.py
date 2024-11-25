class Solution:

    def maxProduct(self, arr):
        max_product = arr[0]
        max_val = arr[0]
        min_val = arr[0]

        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_val, min_val = min_val, max_val

            max_val = max(arr[i], max_val * arr[i])
            min_val = min(arr[i], min_val * arr[i])

            max_product = max(max_product, max_val)

        return max_product