# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长字符串的长度。
# 假设字符串中只包含‘a’-‘z’的字符。例如，在字符串“arabcacfr”中，最长的不含重复字符的子字符串是“acfr”，长度为4

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1 # 字符串遇到第二个a的时候起始位要从r开始
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i

        return maxLength