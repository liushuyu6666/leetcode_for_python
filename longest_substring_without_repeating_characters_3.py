class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        repeat_dict = {}
        start = 0
        end = 1
        ans = 1
        repeat_dict[s[start]] = start
        while(end < len(s)):
            if(s[end] not in repeat_dict.keys() or repeat_dict[s[end]] < start):
                repeat_dict[s[end]] = end
                end += 1
            else:
                ans = max(ans, end - start)
                start = repeat_dict[s[end]] + 1
                repeat_dict[s[end]] = end
                end += 1
        ans = max(ans, end - start)

        return ans

if __name__ == '__main__':
    l = "pwwkew"
    s = Solution()
    print(s.lengthOfLongestSubstring(l))



