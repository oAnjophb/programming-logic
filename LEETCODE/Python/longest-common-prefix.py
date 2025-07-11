class Solution:
    def longestCommonPrefix(self, listOfWords):
        if not listOfWords:
            return ''

        igualityLetters = ''

        for i in range(len(listOfWords[0])):
            char = listOfWords[0][i]

            for word in listOfWords[1:]:
                if i >= len(word) or word[i] != char:
                    return igualityLetters
                
            igualityLetters += char

        return igualityLetters

strs = ["flower","flow","flight"]
s = Solution()
print(s.longestCommonPrefix(strs))