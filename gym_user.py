class GymUser:

    def __init__(self, name, surname, jmbg, phone_number, email, address):
        self.name = name
        self.surname = surname
        self.jmbg = jmbg
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def show_gym_user(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\njmbg: {self.jmbg}\nPhone number: "
              f"{self.phone_number}\nemail: {self.email}\nAddress: {self.address}")
