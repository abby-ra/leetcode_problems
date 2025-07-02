class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1  # +1 for '+', -1 for '-'
        
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char in ['+', '-']:
                result += sign * number
                number = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push current result and sign
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * number
                number = 0
                result *= stack.pop()  # multiply by sign before '('
                result += stack.pop()  # add to result before '('
        
        # Add last number if any
        result += sign * number
        return result
