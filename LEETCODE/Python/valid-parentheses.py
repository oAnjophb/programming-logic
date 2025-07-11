class Solution:
    def isValid(self, string):
        chars = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for currency_char in string:
            if currency_char in chars:
                stack.append(currency_char)

            else:
                if not stack:
                    return False
                last_open = stack.pop()

                if chars[last_open] != currency_char:
                    return False
            
        return len(stack) == 0

strs = '({[]})'
s = Solution()
print(s.isValid(strs))