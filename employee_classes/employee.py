from abc import ABC


class Employee(ABC):
    def __init__(self, name: str, surname: str, jmbg: str, address: str):
        self.name = name
        self.surname = surname
        self.jmbg = jmbg
        self.address = address

