class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Problem Statement:
        ------------------
        Given a valid parentheses string `s`, we first decompose it into its
        primitive valid parentheses strings.

        A *primitive valid parentheses string* is:
        - Non-empty
        - Valid
        - Cannot be split into two smaller non-empty valid parentheses strings

        After decomposing `s` into primitive parts:
            s = P1 + P2 + ... + Pk

        We need to remove the *outermost parentheses* from each primitive
        string Pi and return the final concatenated result.

        Example:
        --------
        Input:  s = "()(()())(())"
        Primitives: "()" + "(()())" + "(())"
        After removing outermost parentheses:
            "" + "()()" + "()"
        Output: "()()()"

        ----------------------------------------------------
        Approach:
        ----------------------------------------------------
        We use a counter `depth` to track the current nesting level
        of parentheses.

        Key Observations:
        - When we encounter '(':
            - If depth > 0, it means this '(' is NOT an outermost one,
              so we include it in the result.
            - Then we increase depth.
        - When we encounter ')':
            - We decrease depth first.
            - If depth > 0 after decrement, this ')' is NOT an outermost one,
              so we include it in the result.

        This way:
        - The very first '(' of a primitive (depth == 0) is skipped.
        - The matching ')' that closes the primitive (depth becomes 0)
          is also skipped.

        Time Complexity:  O(n)
        Space Complexity: O(n)
        """

        result = []   # To build the final answer efficiently
        depth = 0     # Tracks current nesting level

        for ch in s:
            if ch == '(':
                # If depth > 0, this '(' is not an outermost one
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:  # ch == ')'
                depth -= 1
                # If depth > 0, this ')' is not an outermost one
                if depth > 0:
                    result.append(ch)

        return "".join(result)
