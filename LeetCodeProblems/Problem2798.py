
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours:List[int], target: int) -> int:
        """We declare employee_count variable and initialize it with value 0
        to keep track of the number of employees that worked more than 2 hours"""
        employee_count = 0
        for i in range(len(hours)):
            """Inside this loop in range of (1(by default) , 5(number of elements in the list 'hours'))
            we check if the i element from the list is greater or equal with the target"""
            if hours[i] >= target:
                """If the condition is true employee_count+1"""
                employee_count += 1
        return employee_count







