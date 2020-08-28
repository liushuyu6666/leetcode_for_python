class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        def findPalindrome(left: int, right: int, s: str):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return (left + 1, right -1)

        ans = 1
        left = 0
        right = 0
        i = 0


        while(i < len(s)-1):
            # even palindrome
            (temp_left, temp_right) = findPalindrome(i, i + 1, s)
            if(temp_right - temp_left + 1 > ans):
                left = temp_left
                right = temp_right
                ans = temp_right - temp_left + 1
            # odd palindrome
            (temp_left,temp_right) = findPalindrome(i, i, s)
            if(temp_right - temp_left + 1 > ans):
                left = temp_left
                right = temp_right
                ans = temp_right - temp_left + 1
            i += 1

        return s[left: right+1]


if __name__ == '__main__':
    l = "babad"
    s = Solution()
    print(s.longestPalindrome(l))