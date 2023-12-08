class Solution:
    def isPalindrome(self, x: int) -> bool:

        if (x == int(str(x)[::-1])):
            return True

        return False


s = Solution()
print(s.isPalindrome(121))