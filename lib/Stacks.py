def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]"
    bracket_pairs = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    
    return not stack

# Test the function
expression1 = "([])"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
