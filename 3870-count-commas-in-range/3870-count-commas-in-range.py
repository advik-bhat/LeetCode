class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        if n<1000:
            return count
        else:
            return (n-999)
        
