from enum import Enum

class Position(Enum):
    DEVELOPER = 1
    DBA = 2
    TESTER = 3
    MANAGER = 4

class Employee:
    def __init__(self, name, email, base_salary, position):
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.position = position

    def calculate_net_salary(self): 
        if self.position == Position.DEVELOPER:
            if self.base_salary >= 3000:
                return self.base_salary * 0.8
            else:
                return self.base_salary * 0.9
        elif self.position == Position.DBA or self.position == Position.TESTER:
            if self.base_salary >= 2000:
                return self.base_salary * 0.75
            else:
                return self.base_salary * 0.85
        elif self.position == Position.MANAGER:
            if self.base_salary >= 5000:
                return self.base_salary * 0.7
            else:
                return self.base_salary * 0.8
