import pytest
from person import Person, Email, PersonDAO

@pytest.fixture
def valid_person():
    return Person(1, "Rodrigo R", 30)

@pytest.fixture
def valid_email():
    return Email(1,"Rodrigo@Gmail.com")

@pytest.fixture
def invalid_person():
    return Person(2, "Alice", 300)

@pytest.fixture
def invalid_email():
    return Email(2, "invalid_email")

def test_save_valid_person(valid_person, valid_email):
    valid_person.emails.append(valid_email)
    dao = PersonDAO()
    dao.save(valid_person)
    assert len(dao.persons) == 1

def test_is_name_valid():
    dao = PersonDAO()
    assert dao.is_name_valid("Rodrigo R") is True
    assert dao.is_name_valid("Alice") is False
    assert dao.is_name_valid("123 Rodrigo") is False

def test_save_invalid_person(invalid_person):
    dao = PersonDAO()
    dao.save(invalid_person)
    assert len(dao.persons) == 0

def test_person_has_email():
    dao = PersonDAO()
    valid_email = Email(1, "Rodrigo@Gmail.com")
    assert dao.person_has_email([valid_email]) is True
    assert dao.person_has_email([]) is False

def test_is_email_valid():
    dao = PersonDAO()
    assert dao.is_email_valid("Rodrigo@Gmail.com") is True
    assert dao.is_email_valid("invalid_email") is False

def test_is_age_valid():
    dao = PersonDAO()
    assert dao.is_age_valid(30) is True
    assert dao.is_age_valid(300) is False

