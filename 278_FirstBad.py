# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if isBadVersion(1): return 1
        
        high = n
        low = 2
        mid = low + (high - low)// 2
        
        while low <= high:
            isBadMid = isBadVersion(mid)

            if isBadMid and not isBadVersion(mid - 1):
                return mid

            if isBadMid:
                high = mid - 1
                mid = low + (high - low)// 2
            else: 
                low = mid + 1
                mid = low + (high - low)// 2
            

