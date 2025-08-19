
class Solution:
    def plusOne(self, digits: list):
        lastItem = digits[len(digits)- 1]
        new_lastItem = digits[len(digits)-1] + 1

        if lastItem < 9:
            digits[len(digits)- 1] = new_lastItem

        else:

            for i in str(new_lastItem):
                digits.append(int(i))
            digits.pop(0)

        return digits
    

digits = [9]

s = Solution()
print(s.plusOne(digits))