class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = {}
        start = length = 0
        for i in range(len(s)):
            if s[i] in tmp and start <= tmp[s[i]]:#如果碰到重复的且起始位置小于现在的位置（确保是新的字符串），则把起始位置放到当前位置的后一位从新开始计算字符串长度。
            #NOTE：子字符串是遇上重复的字符则从上一个重复的字符的后一位开始，而非遇上的重复字符开始
                start = tmp[s[i]] + 1#从上一个重复的字符的后一个位置开始
            else:
                length = max(length,i - start +1)#若字符没有重复，则与之前的子字符串比较长度,因为要算上自己所以要+1
            
            tmp[s[i]] = i#存储位置
        return length
