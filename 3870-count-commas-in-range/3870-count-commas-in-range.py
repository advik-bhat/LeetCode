class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        if len(str(n))<4:
            return count
        else:
            for i in range (1000,n+1):
                count +=1
            return count
        
