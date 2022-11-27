class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # result = [0]
        # unique_list = []
        # for index, i in enumerate(list(s)):
        #     if i in unique_list:
        #         result.append(len(unique_list))
        #         unique_list.clear()
        #     unique_list.append(i)
        #     if index == len(list(s))-1:
        #         result.append(len(unique_list))
        # return max(result), list(s)
        output = 0
        count = {}
        pos = -1
        for index, letter in enumerate(s):
            if letter in count and count[letter] > pos:
                pos = count[letter]
            count[letter] = index 
            output = max(output,index-pos)
        return output

    
solution = Solution()
question1 = solution.lengthOfLongestSubstring("abcabcbb")
print(question1)
question2 = solution.lengthOfLongestSubstring("abcabcbb")
print(question2)
question3 = solution.lengthOfLongestSubstring("bbbbb")
print(question3)
question4 = solution.lengthOfLongestSubstring(" ")
print(question4)
question5 = solution.lengthOfLongestSubstring("au")
print(question5)
question6 = solution.lengthOfLongestSubstring("dvdf")
print(question6)