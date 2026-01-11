class Solution:
    def infixToPostfix(self, s: str) -> str:
        # Stack to store operators
        stack = []

        # Result list for postfix expression
        result = []

        # Operator precedence
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

        # Helper function to check associativity
        def is_right_associative(op):
            return op == '^'

        for ch in s:
            # 1. If operand, add to result
            if ch.isalnum():
                result.append(ch)

            # 2. If '(', push to stack
            elif ch == '(':
                stack.append(ch)

            # 3. If ')', pop until '('
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # remove '('

            # 4. If operator
            else:
                while (stack and stack[-1] != '(' and
                       (precedence[stack[-1]] > precedence[ch] or
                       (precedence[stack[-1]] == precedence[ch] and
                        not is_right_associative(ch)))):
                    result.append(stack.pop())

                stack.append(ch)

        # Pop remaining operators
        while stack:
            result.append(stack.pop())

        return ''.join(result)
