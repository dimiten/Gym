import re


def is_name_valid(name: str):
    if not name[0].isupper():
        print("Name must start with upper case character!")
        return False
        # raise NameNotValidException("Name must start with upper case character!")
    for char in name:
        if not char.isalpha():
            print("Name must consist of alphabetic string and can't have spaces!")
            return False
            # raise NameNotValidException("Name must consist of alphabetic string and can't have spaces!")
    return True


def is_surname_valid(surname: str) -> bool:
    if not surname[0].isupper():
        print("Surname must start with upper case character!")
        return False
    for char in surname:
        if not char.isalpha():
            print("Surname must consist of alphabetic string and can't have spaces!")
            return False
    return True


def is_jmbg_valid(jmbg: str):
    if len(jmbg) != 13:
        print("Length of jmbg must be 13!")
        return False
    if not jmbg.isdigit():
        print("jmbg must consist of only numbers!")
        return False
    if int(jmbg[0:2]) > 31:
        print("invalid day of birth!")
        return False
    if int(jmbg[2:4]) > 12:
        print("invalid month of birth!")
        return False
    if int(jmbg[4]) not in [0, 9]:
        print("invalid year of birth!")
        return False

    a = int(jmbg[0])
    b = int(jmbg[1])
    c = int(jmbg[2])
    d = int(jmbg[3])
    e = int(jmbg[4])
    f = int(jmbg[5])
    g = int(jmbg[6])
    h = int(jmbg[7])
    i = int(jmbg[8])
    j = int(jmbg[9])
    k = int(jmbg[10])
    l = int(jmbg[11])
    m = int(jmbg[12])

    control_number = 11 - ((7 * (a + g) + 6 * (b + h) + 5 * (c + i) + 4 * (d + j) + 3 * (e + k) + 2 * (f + l)) % 11)

    if control_number in range(1, 10):
        if m != control_number:
            print("invalid control number!")
            return False
    elif control_number > 9:
        control_number = 0
        if m != control_number:
            print("invalid control number!")
            return False

    return True


def is_email_valid(email: str):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pattern, email):
        return True
    else:
        print("Invalid Email")
        return False


def is_phone_number_valid(phone_number: str):
    if len(phone_number) > 15:
        print("Phone number can't have more than 15 characters!")
        return False
    if phone_number[0] != "+":
        print("Phone number must start with \"+\"")
        return False
    if not phone_number[1:].isdigit():
        print("Characters after \"+\" must be only digits!")
        return False
    return True


def is_street_valid(street: str):
    if not street[0].isupper():
        print("Street must start with an upper case letter!")
        return False

    if not street.isalpha() and " " not in street:
        print("Street must only have letters!")
        return False

    if " " in street:
        street_list = street.split()
        for el in street_list:
            if not el.isalpha():
                print("Street must only have letters!")
                return False
    return True


def is_street_number_valid(street_number: str):
    if not street_number.isdigit():
        print("Street number must consist of only digits!")
        return False
    return True


def is_weight_valid(weight: str):
    if len(weight) < 2 or len(weight) > 3:
        print("Invalid weight!")
        return False

    if not weight.isdigit():
        print("Weight must consist of only digits!")
        return False
    return True

