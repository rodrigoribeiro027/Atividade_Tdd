import pytest
from Employees import Employee, Position

@pytest.fixture
def developer():
    return Employee("Jose", "Jose@Gmail.com", 3500, Position.DEVELOPER)

def test_calculates_developer_salary_less_than_3000():
    developer = Employee("Eliane", "eliane@Gmail.com", 2500, Position.DEVELOPER)
    assert developer.calculate_net_salary() == 2250.0

def test_calculates_developer_salary_greater_than_or_equal_to_3000(developer):
    assert developer.calculate_net_salary() == 2800.0

@pytest.fixture
def dba():
    return Employee("Yasmin", "yasmin@Gmail.com", 2500, Position.DBA)

def test_calculates_dba_salary_less_than_2000():
    dba = Employee("Alice", "alice@Gmail.com", 1500, Position.DBA)
    assert dba.calculate_net_salary() == 1275.0

def test_calculates_dba_salary_greater_than_or_equal_to_2000(dba):
    assert dba.calculate_net_salary() == 1875.0

@pytest.fixture
def tester():
    return Employee("Beatrix", "beatrix@Gmail.com", 2500, Position.TESTER)

def test_calculates_tester_salary_less_than_2000():
    tester = Employee("Aline", "aline@Gmail.com", 1500, Position.TESTER)
    assert tester.calculate_net_salary() == 1275.0

def test_calculates_tester_salary_greater_than_or_equal_to_2000(tester):
    assert tester.calculate_net_salary() == 1875.0

@pytest.fixture
def manager():
    return Employee("Rodrigo", "rodrigo@Gmail.com", 6000, Position.MANAGER)

def test_calculates_manager_salary_greater_than_or_equal_to_5000(manager):
    assert manager.calculate_net_salary() == 4200.0

def test_calculates_manager_salary_less_than_5000():
    manager = Employee("Mariane", "mariane@Gmail.com", 4000, Position.MANAGER)
    assert manager.calculate_net_salary() == 3200.0
