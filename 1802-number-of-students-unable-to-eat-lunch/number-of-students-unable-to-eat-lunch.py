import time
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        max_execution_time = 0.0001

        try:
            start_time = time.time()
            while(students):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    
                else:
                    
                    y = students.pop(0)
                    students.append(y)
                    
                if time.time() - start_time > max_execution_time:
                    raise TimeoutError("Execution time limit exceeded")
                
        except:
            return( len(students))
        return( len(students))