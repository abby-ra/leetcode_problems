class Solution:
    def decodeString(self, s):
        stack = []
        current_str = ""
        number = 0

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)  # Build the full number
            elif ch == '[':
                stack.append((current_str, number))  # Save the current context
                current_str = ""  # Start a new string
                number = 0        # Reset number
            elif ch == ']':
                prev_str, repeat = stack.pop()        # Get last context
                current_str = prev_str + current_str * repeat  # Decode
            else:
                current_str += ch  # Just a character, add to current

        return current_str
