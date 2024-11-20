class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n=len(arr)
        threshold=n//3
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        result=[]
        for num,count in freq.items():
            if count>threshold:
                result.append(num)
        for i in range (len(result)):
            for j in range (0,len(result)-i-1):
                if result[j]>result[j+1]:
                    result[j],result[j+1]=result[j+1],result[j]
        return result