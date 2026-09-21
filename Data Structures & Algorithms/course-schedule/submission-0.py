'''
0 <- 1
2 <- 3
4 <- 1
'''
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereqs = {}
        for [course, pre] in prerequisites:
            course_to_prereqs[course] = course_to_prereqs.get(course, []) + [pre]
        
        courses = deque(course_to_prereqs.keys())

        while courses and numCourses > 0:
            course_to_take = courses.popleft()
            if course_to_take in course_to_prereqs:
                for pre in course_to_prereqs[course_to_take]:
                    courses.append(pre)
            
            numCourses -= 1

        if len(courses) == 0:
            return True
            
        return False 