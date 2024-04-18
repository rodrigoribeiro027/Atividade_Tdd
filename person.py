from typing import List

class Person:
    def __init__(self, id: int, name: str, age):
        self.id = id
        self.name = name
        self.age = age
        self.emails: List[Email] = list()

class Email:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class PersonDAO:
    def __init__(self):
        self.persons: List[Person] = list()

    def save(self, person:Person):
        errors = self.isValidToInclude(person)
        if len(errors) == 0:
            self.persons.append(person)

    def isValidToInclude(self, person: Person) -> List[str]:
        if isinstance(person, Person):
            errors = []
            errors.extend(filter(None, (
                "Name is invalid" if not self.is_name_valid(person.name) else None,
                "Age is invalid" if not self.is_age_valid(person.age) else None,
                "Person must have at least one email" if not self.person_has_email(person.emails) else None,
                *(f"Email '{email.name}' is invalid, it must be in the format example: rodrigo@gmail.com" for email in person.emails if not self.is_email_valid(email.name))
            )))
            return errors

    def is_name_valid(self, name: str) -> bool:
        names = name.split()
        if len(names) >= 2 and not any(char.isdigit() for char in name):
            return True
        return False


    def is_age_valid(self, age:int) -> bool:
        if age in range(1, 201):
            return True
        else:
            return False

    def person_has_email(self, emails: List[Email]):
        if len(emails) >= 1:
            return True
        else:
            return False

    def is_email_valid(self, email: str) -> bool:
        if "@" in email:
            local_part, domain_part = email.split("@", 1)
            if local_part and domain_part:
                if "." in domain_part:
                    return True
        return False
