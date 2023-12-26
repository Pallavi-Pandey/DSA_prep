class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lis=[]
        tot=0
        for i in nums:
            tot+=i
            lis.append(tot)
        return lis
