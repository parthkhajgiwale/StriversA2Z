class Solution:
    def celebrity(self, M):
        """
        Celebrity Problem

        A celebrity is a person who:
        1. Is known by everyone else at the party
        2. Does NOT know anyone else

        You are given a square matrix M of size N x N where:
        - M[i][j] = 1 means person i knows person j
        - M[i][j] = 0 means person i does NOT know person j
        - M[i][i] is always 0 (a person does not know themselves)

        Task:
        Return the index of the celebrity if one exists, otherwise return -1.

        Example:
        Input:
        M = [
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0]
        ]

        Output:
        1
        """

        n = len(M)

        # Step 1: Find a potential celebrity
        # We use two pointers to eliminate non-celebrities
        i, j = 0, n - 1

        while i < j:
            # If person i knows person j, i cannot be a celebrity
            if M[i][j] == 1:
                i += 1
            else:
                # If person i does NOT know person j, j cannot be a celebrity
                j -= 1

        # At this point, i is the only possible celebrity candidate
        candidate = i

        # Step 2: Verify the candidate
        for k in range(n):
            if k != candidate:
                # Celebrity should NOT know anyone
                # Everyone else SHOULD know the celebrity
                if M[candidate][k] == 1 or M[k][candidate] == 0:
                    return -1

        return candidate
