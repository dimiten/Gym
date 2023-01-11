from employee_classes.employee import Employee


class Cleaner(Employee):
    def __init__(self, name: str, surname: str, jmbg: str, address: str):
        super().__init__(name, surname, jmbg, address)