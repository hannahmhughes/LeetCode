class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = set()
        length = 0

        for char in s:
            if char in pairs:
                pairs.remove(char)
                length += 2
            else:
                pairs.add(char)
        
        if pairs:
            length += 1

        return length

        