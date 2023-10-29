#2798.Number of Employees Who Met the Target
#There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
#The company requires each employee to work for at least target hours.
#You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
#Return the integer denoting the number of employees who worked at least target hours.
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







