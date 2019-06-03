# 输入任一字符串，输出所有的组合

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        pStr = []
        charlist = list(ss)
        charlist.sort()

        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i - 1]:
                continue
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i + 1:]))
            for j in temp:
                pStr.append(charlist[i] + j)
        return pStr


s = Solution()
print(s.Permutation('abdfg'))
