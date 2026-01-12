class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        """
        Problem:
        Given two arrays:
        - Student: minimum cookie size each student requires
        - Cookie: sizes of available cookies
        
        Each student can get at most one cookie and each cookie
        can be given to only one student.
        
        A cookie can be assigned only if:
        Cookie[j] >= Student[i]
        
        Goal:
        Maximize the number of students who receive cookies.
        """

        # Step 1: Sort both arrays
        # This helps us greedily assign the smallest possible cookie
        Student.sort()
        Cookie.sort()

        # Step 2: Initialize pointers
        student_index = 0   # pointer for students
        cookie_index = 0    # pointer for cookies

        # Step 3: Traverse both arrays
        while student_index < len(Student) and cookie_index < len(Cookie):
            # If current cookie can satisfy current student
            if Cookie[cookie_index] >= Student[student_index]:
                # Assign cookie
                student_index += 1
                cookie_index += 1
            else:
                # Cookie too small, try next larger cookie
                cookie_index += 1

        # student_index represents number of students satisfied
        return student_index
