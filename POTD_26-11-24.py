def circularSubarraySum(arr):
    
    currSum = 0
    maxSum = 0
    negSum = 0
    negCurrSum = 0
    totalSum = 0
    
    for item in arr:
        totalSum += item
        
        currSum = max(currSum + item, item)
        
        if currSum > maxSum:
            maxSum = currSum
            
        item *= -1
        
        negCurrSum = max(negCurrSum + item, item)
        
        if negCurrSum > negSum:
            negSum = negCurrSum
            
    if totalSum + negSum > maxSum:
        return totalSum + negSum
        
    return maxSum