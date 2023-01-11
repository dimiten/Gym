import os

from employee_classes.employee import Employee
from gym_user import GymUser
from exceptions import *

COST_OF_TRAINING = 300


class Gym:
    def __init__(self, name: str, address: str, phone_number: str, email: str, pib: str, employees=None,
                 gym_users=None):
        if gym_users is None:
            self.gym_users = []
        if employees is None:
            self.employees = []
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.__pib = pib

    def get_pib(self):
        return self.__pib

    def set_pib(self, pib):
        self.__pib = pib

    def show_gym(self):
        print(f"Name: {self.name}\nAdress: {self.address}\nPhone number: {self.phone_number}\nemail: {self.email}")

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def add_gym_user(self, gym_user: GymUser):
        self.gym_users.append(gym_user)

    def join_gym(self):
        gym_user_name = input("Enter your name: ")
        while not is_name_valid(gym_user_name):
            gym_user_name = input("Enter your name: ")

        gym_user_surname = input("Enter your surname: ")
        while not is_surname_valid(gym_user_surname):
            gym_user_surname = input("Enter your surname: ")

        gym_user_jmbg = input("Enter your jmbg: ")
        while not is_jmbg_valid(gym_user_jmbg):
            gym_user_jmbg = input("Enter your jmbg: ")

        gym_user_phone_number = input("Enter your phone number(format: +3816312345): ")
        while not is_phone_number_valid(gym_user_phone_number):
            gym_user_phone_number = input("Enter your phone number(format: +3816312345): ")

        gym_user_email = input("Enter your email: ")
        while not is_email_valid(gym_user_email):
            gym_user_email = input("Enter your email: ")

        gym_user_address_street = input("Enter your street: ")
        while not is_street_valid(gym_user_address_street):
            gym_user_address_street = input("Enter your street: ")

        gym_user_address_number = input("Enter your address number: ")
        while not is_street_number_valid(gym_user_address_number):
            gym_user_address_number = input("Enter your address number: ")

        gym_user_address = gym_user_address_street + " " + gym_user_address_number

        gym_user_weight = input("Enter your current weight (in kg): ")
        while not is_weight_valid(gym_user_weight):
            gym_user_weight = input("Enter your current weight (in kg): ")

        print("\nOne month plan:\n"
              "a) 12 times per month: 2000 din\n"
              "b) 16 times per month: 2500 din\n"
              "c) Unlimited times per month: 3000 din\n"
              "\n"
              "Three months plan:\n"
              "d) 12 times per month: 5500 din\n"
              "e) 16 times per month: 6500 din\n"
              "f) Unlimited times per month: 7500 din\n")

        membership_plans_dict = {
            "a": "One month plan, 12 times per month: 2000 din",
            "b": "One month plan, 16 times per month: 2500 din",
            "c": "One month plan, unlimited times per month: 3000 din",
            "d": "Three months plan, 12 times per month: 5500 din",
            "e": "Three months plan, 16 times per month: 6500 din",
            "f": "Three months plan, unlimited times per month: 7500 din"
        }

        choice = input("Choose a letter of a plan you want to make: ")
        while choice not in membership_plans_dict.keys():
            print("You must choose letters a-f")
            choice = input("Choose a letter of a plan you want to make: ")

        membership_plans_entries_allowed_dict = {
            "a": 12,
            "b": 16,
            "c": "unlimited",
            "d": 12,
            "e": 16,
            "f": "unlimited"
        }

        gym_user = GymUser(gym_user_name, gym_user_surname, gym_user_jmbg, gym_user_phone_number, gym_user_email,
                           gym_user_address)

        self.gym_users.append(gym_user)

        if not os.path.exists("gym_members"):
            os.mkdir("gym_members")

        os.chdir("gym_members")

        if not os.path.exists("gym_membership_ids.txt"):
            with open("gym_membership_ids.txt", "w") as f:
                f.write("")

        with open("gym_membership_ids.txt", "r") as f:
            data = f.read()
            if data == "":
                empty = True
            else:
                empty = False

        if empty:
            with open("gym_membership_ids.txt", "w") as f:
                for i in range(101, 1001):
                    f.write(f"{i}\n")

        with open("gym_membership_ids.txt", "r") as f:
            membership_id = f.readlines()[0]

        membership_id = membership_id.replace("\n", "")

        gym_user_dict = {"Name": gym_user_name, "Surname": gym_user_surname, "Membership id": membership_id,
                         "jmbg": gym_user_jmbg,
                         "Phone number": gym_user_phone_number, "email": gym_user_email, "Address": gym_user_address,
                         "Weight": gym_user_weight + "kg",
                         "Membership plan": membership_plans_dict.get(choice),
                         "Entries allowed per month": membership_plans_entries_allowed_dict.get(choice),
                         "Times trained this month": 0,
                         "Times trained past allowed number of times": 0}

        with open(f"{gym_user_name}_{gym_user_surname}_{membership_id}.txt", "w") as f:
            for key in gym_user_dict:
                f.write(f"{key}: {gym_user_dict.get(key)}\n")

        with open("gym_membership_ids.txt", "r") as f:
            membership_ids = f.readlines()

        membership_ids.remove(membership_ids[0])

        with open("gym_membership_ids.txt", "w") as f:
            for el in membership_ids:
                f.write(f"{el}")

        os.chdir("../")

    def quit_gym(self):

        while True:
            gym_user_name = input("Enter your name: ")
            gym_user_surname = input("Enter your surname: ")
            gym_user_membership_id = input("Enter your membership id: ")
            if os.path.exists(f"gym_members/{gym_user_name}_{gym_user_surname}_{gym_user_membership_id}.txt"):

                os.chdir("gym_members")

                with open("gym_membership_ids.txt", "r") as f:
                    membership_ids = f.readlines()

                membership_ids = list(map(int, membership_ids))
                membership_ids.append(int(gym_user_membership_id))
                membership_ids.sort()

                with open("gym_membership_ids.txt", "w") as f:
                    for gym_id in membership_ids:
                        f.write(f"{str(gym_id)}\n")

                os.remove(f"{gym_user_name}_{gym_user_surname}_{gym_user_membership_id}.txt")

                os.chdir("../")
                break
            else:
                print("That person isn't a member of the gym. Please check if you typed everything correctly")
                continue

    def enter_gym(self):
        while True:
            gym_user_name = input("Enter your name: ")
            gym_user_surname = input("Enter your surname: ")
            gym_user_member_id = input("Enter your membership id: ")

            if os.path.exists(f"gym_members/{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt"):

                os.chdir("gym_members")

                with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt") as f:
                    lines = f.readlines()

                    times_trained = lines[-2]
                    times_trained = times_trained.split(":")
                    times_trained = times_trained[1].strip()

                    allowed_times_to_train = lines[-3]
                    allowed_times_to_train = allowed_times_to_train.split(":")
                    allowed_times_to_train = allowed_times_to_train[1].strip()

                os.chdir("../")

                if not os.path.exists("current_users_in_gym"):
                    os.mkdir("current_users_in_gym")

                os.chdir("current_users_in_gym")

                if os.path.exists(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt"):
                    print("That person is already in the gym.")
                    continue

                if not os.path.exists("available_keys.txt"):
                    with open("available_keys.txt", "w") as f:
                        f.write("")

                with open("available_keys.txt", "r") as f:
                    data = f.read()
                    if data == "":
                        empty = True
                    else:
                        empty = False

                if empty:
                    with open("available_keys.txt", "w") as f:
                        for i in range(1, 101):
                            f.write(f"{i}\n")

                with open("available_keys.txt", "r") as f:
                    list_of_keys = f.readlines()

                if allowed_times_to_train != "unlimited":
                    if int(times_trained) == int(allowed_times_to_train):
                        choice = input(f"You aren't allowed to train this month anymore. "
                                       f"Do you want to pay extra {COST_OF_TRAINING} "
                                       f"din in order to train today? yes or no: ")
                        while choice != "yes" and choice != "no":
                            print("Invalid input! Type in: yes or no")
                            choice = input(f"You aren't allowed to train this month anymore. "
                                           f"Do you want to pay extra {COST_OF_TRAINING} "
                                           f"din in order to train today? yes or no: ")
                        if choice == "no":
                            break
                        elif choice == "yes":
                            with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                                f.write(f"Key in use:{list_of_keys[0]}")
                            list_of_keys.remove(list_of_keys[0])
                            os.chdir("../gym_members")
                            with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "r") as f:
                                lines = f.readlines()
                            times_trained_past_allowed = int(lines[-1].split(":")[1].strip())
                            times_trained_past_allowed += 1
                            lines[-1] = f"Times trained past allowed number of times: {times_trained_past_allowed}\n"
                            with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                                for line in lines:
                                    f.write(line)
                            os.chdir("../current_users_in_gym")
                    elif int(times_trained) < int(allowed_times_to_train):
                        with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                            f.write(f"Key in use:{list_of_keys[0]}")
                        list_of_keys.remove(list_of_keys[0])
                        os.chdir("../gym_members")
                        with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "r") as f:
                            lines = f.readlines()
                        times_trained = int(lines[-2].split(":")[1].strip())
                        times_trained += 1
                        lines[-2] = f"Times trained this month: {times_trained}\n"
                        with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                            for line in lines:
                                f.write(line)
                        os.chdir("../current_users_in_gym")
                else:
                    with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                        f.write(f"Key in use:{list_of_keys[0]}")
                    list_of_keys.remove(list_of_keys[0])
                    os.chdir("../gym_members")
                    with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "r") as f:
                        lines = f.readlines()
                    times_trained = int(lines[-2].split(":")[1].strip())
                    times_trained += 1
                    lines[-2] = f"Times trained this month: {times_trained}\n"
                    with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                        for line in lines:
                            f.write(line)
                    os.chdir("../current_users_in_gym")

                with open("available_keys.txt", "w") as f:
                    for key in list_of_keys:
                        f.write(f"{key}")

                os.chdir("../")
                break
            else:
                print("That person isn't a member of the gym. Please check if you typed everything correctly")
                continue

    def leave_gym(self):
        while True:
            gym_user_name = input("Enter your name: ")
            gym_user_surname = input("Enter your surname: ")
            gym_user_member_id = input("Enter your membership id: ")
            if os.path.exists(f"gym_members/{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt"):
                if os.path.exists(f"current_users_in_gym/{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt"):

                    os.chdir("current_users_in_gym")

                    with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "r") as f:
                        line = f.readline()
                        key_used = line.split(":")[1]

                    os.remove(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt")

                    with open("available_keys.txt", "r") as f:
                        available_keys = f.readlines()

                    for el in available_keys:
                        el.replace("\n", "")

                    available_keys = list(map(int, available_keys))
                    available_keys.append(int(key_used))
                    available_keys.sort()

                    with open("available_keys.txt", "w") as f:
                        for i in available_keys:
                            f.write(f"{str(i)}\n")

                    os.chdir("../")

                    break
                else:
                    print("That person isn't currently in the gym. Please check if you typed everything correctly")
                    continue
            else:
                print("That person isn't a member of the gym. Please check if you typed everything correctly")
                continue

    def weight_in(self):
        while True:
            gym_user_name = input("Enter your name: ")
            gym_user_surname = input("Enter your surname: ")
            gym_user_member_id = input("Enter your membership id: ")
            gym_user_new_weight = input("Enter your new weight: ")
            while not is_weight_valid(gym_user_new_weight):
                gym_user_new_weight = input("Enter your current weight (in kg): ")

            if os.path.exists(f"gym_members/{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt"):

                os.chdir("gym_members")

                with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "r") as f:
                    lines = f.readlines()

                lines[7] = f"Weight: {gym_user_new_weight}kg\n"

                with open(f"{gym_user_name}_{gym_user_surname}_{gym_user_member_id}.txt", "w") as f:
                    f.writelines(lines)

                os.chdir("../")
                break
            else:
                print("That person isn't a member of the gym. Please check if you typed everything correctly")
                continue

    def print_all_members(self):
        for filename in os.listdir("gym_members"):
            if filename != "gym_membership_ids.txt":
                os.chdir("gym_members")
                with open(filename, "r") as f:
                    data = f.readlines()

                for i in range(3):
                    print(data[i].replace("\n", ""))

                print("\n")

                os.chdir("../")

    def print_all_members_for_plan(self):
        print("\nOne month plan:\n"
              "a) 12 times per month: 2000 din\n"
              "b) 16 times per month: 2500 din\n"
              "c) Unlimited times per month: 3000 din\n"
              "\n"
              "Three months plan:\n"
              "d) 12 times per month: 5500 din\n"
              "e) 16 times per month: 6500 din\n"
              "f) Unlimited times per month: 7500 din\n")

        membership_plans_dict = {
            "a": "One month plan, 12 times per month: 2000 din",
            "b": "One month plan, 16 times per month: 2500 din",
            "c": "One month plan, unlimited times per month: 3000 din",
            "d": "Three months plan, 12 times per month: 5500 din",
            "e": "Three months plan, 16 times per month: 6500 din",
            "f": "Three months plan, unlimited times per month: 7500 din"
        }

        choice = input("Choose a letter of a plan you want to make: ")
        while choice not in membership_plans_dict.keys():
            print("You must choose letters a-f")
            choice = input("Choose a letter of a plan you want to make: ")

        plan = membership_plans_dict.get(choice)

        for filename in os.listdir("gym_members"):
            if filename != "gym_membership_ids.txt":
                os.chdir("gym_members")
                with open(filename, "r") as f:
                    data = f.readlines()

                    if plan in data[8]:
                        for i in range(3):
                            print(data[i].replace("\n", ""))
                        print("\n")

                os.chdir("../")

    def percentage_for_plan(self):
        print("\nOne month plan:\n"
              "a) 12 times per month: 2000 din\n"
              "b) 16 times per month: 2500 din\n"
              "c) Unlimited times per month: 3000 din\n"
              "\n"
              "Three months plan:\n"
              "d) 12 times per month: 5500 din\n"
              "e) 16 times per month: 6500 din\n"
              "f) Unlimited times per month: 7500 din\n")

        membership_plans_dict = {
            "a": "One month plan, 12 times per month: 2000 din",
            "b": "One month plan, 16 times per month: 2500 din",
            "c": "One month plan, unlimited times per month: 3000 din",
            "d": "Three months plan, 12 times per month: 5500 din",
            "e": "Three months plan, 16 times per month: 6500 din",
            "f": "Three months plan, unlimited times per month: 7500 din"
        }

        choice = input("Choose a letter of a plan you want to make: ")
        while choice not in membership_plans_dict.keys():
            print("You must choose letters a-f")
            choice = input("Choose a letter of a plan you want to make: ")

        plan = membership_plans_dict.get(choice)

        number_of_members = len(os.listdir("gym_members")) - 1

        counter = 0
        for filename in os.listdir("gym_members"):
            if filename != "gym_membership_ids.txt":
                os.chdir("gym_members")
                with open(filename, "r") as f:
                    data = f.readlines()

                    if plan in data[8]:
                        counter += 1

                os.chdir("../")

        percentage = round(counter / number_of_members, 2)

        print(f"Percentage of members with that plan is: {percentage}")

    def monthly_and_yearly_profit(self):
        monthly_profit = 0
        for filename in os.listdir("gym_members"):
            if filename != "gym_membership_ids.txt":
                os.chdir("gym_members")
                with open(filename, "r") as f:
                    data = f.readlines()
                    times_trained_above_limit = int(data[-1].split(":")[1].strip())
                    if "One month" in data[-4]:
                        cost_per_month = int(data[-4].split(":")[2].split()[0]) + (
                                times_trained_above_limit * COST_OF_TRAINING)
                        monthly_profit += cost_per_month
                    elif "Three months" in data[-4]:
                        cost_per_month = (int(data[-4].split(":")[2].split()[0]) / 3) + (
                                times_trained_above_limit * COST_OF_TRAINING)
                        monthly_profit += cost_per_month
                os.chdir("../")

        print(f"Monthly profit: {round(monthly_profit, 2)} din")
        print(f"Yearly profit: {round(monthly_profit * 12, 2)} din")

    def monthly_and_yearly_profit_for_plan(self):
        print("\nOne month plan:\n"
              "a) 12 times per month: 2000 din\n"
              "b) 16 times per month: 2500 din\n"
              "c) Unlimited times per month: 3000 din\n"
              "\n"
              "Three months plan:\n"
              "d) 12 times per month: 5500 din\n"
              "e) 16 times per month: 6500 din\n"
              "f) Unlimited times per month: 7500 din\n")

        membership_plans_dict = {
            "a": "One month plan, 12 times per month: 2000 din",
            "b": "One month plan, 16 times per month: 2500 din",
            "c": "One month plan, unlimited times per month: 3000 din",
            "d": "Three months plan, 12 times per month: 5500 din",
            "e": "Three months plan, 16 times per month: 6500 din",
            "f": "Three months plan, unlimited times per month: 7500 din"
        }

        choice = input("Choose a letter of a plan you want to make: ")
        while choice not in membership_plans_dict.keys():
            print("You must choose letters a-f")
            choice = input("Choose a letter of a plan you want to make: ")

        plan = membership_plans_dict.get(choice)

        monthly_profit = 0

        for filename in os.listdir("gym_members"):
            if filename != "gym_membership_ids.txt":
                os.chdir("gym_members")
                with open(filename, "r") as f:
                    data = f.readlines()
                    if plan in data[8]:
                        times_trained_above_limit = int(data[-1].split(":")[1].strip())
                        cost_per_month = int(data[-4].split(":")[2].split()[0]) + (
                                times_trained_above_limit * COST_OF_TRAINING)
                        monthly_profit += cost_per_month
                os.chdir("../")

        print(f"Monthly profit for that plan: {round(monthly_profit, 2)} din")
        print(f"Yearly profit for that plan: {round(monthly_profit * 12, 2)} din")

    def print_members_in_gym(self):
        for filename in os.listdir("current_users_in_gym"):
            if filename != "available_keys.txt":
                name = filename.split("_")[0]
                surname = filename.split("_")[1]
                member_id = filename.split("_")[2].replace(".txt", "")

                print(f"Name: {name}\nSurname: {surname}\nMembership id: {member_id}\n")

    def reset_times_trained(self):
        for filename in os.listdir("gym_members"):
            if filename != "gym_membership_ids.txt":
                os.chdir("gym_members")
                with open(filename, "r") as f:
                    data = f.readlines()
                data[-2] = f"Times trained this month: {0}\n"
                data[-1] = f"Times trained past allowed number of times: {0}\n"
                with open(filename, "w") as f:
                    for line in data:
                        f.write(line)
                os.chdir("../")

    def hire_employee(self):
        gym_employee_name = input("Enter your name: ")
        while not is_name_valid(gym_employee_name):
            gym_employee_name = input("Enter your name: ")

        gym_employee_surname = input("Enter your surname: ")
        while not is_surname_valid(gym_employee_surname):
            gym_employee_surname = input("Enter your surname: ")

        gym_employee_jmbg = input("Enter your jmbg: ")
        while not is_jmbg_valid(gym_employee_jmbg):
            gym_employee_jmbg = input("Enter your jmbg: ")

        gym_employee_phone_number = input("Enter your phone number(format: +3816312345): ")
        while not is_phone_number_valid(gym_employee_phone_number):
            gym_employee_phone_number = input("Enter your phone number(format: +3816312345): ")

        gym_employee_email = input("Enter your email: ")
        while not is_email_valid(gym_employee_email):
            gym_employee_email = input("Enter your email: ")

        gym_employee_address_street = input("Enter your street: ")
        while not is_street_valid(gym_employee_address_street):
            gym_employee_address_street = input("Enter your street: ")

        gym_employee_address_number = input("Enter your address number: ")
        while not is_street_number_valid(gym_employee_address_number):
            gym_employee_address_number = input("Enter your address number: ")

        gym_employee_address = gym_employee_address_street + " " + gym_employee_address_number

        print("Positions:\n"
              "a) Receptionist\n"
              "b) Trainer\n"
              "c) Cleaner\n")

        gym_employee_position_choice = input("Choose a letter of a position from above (a, b or c): ")
        while gym_employee_position_choice not in ["a", "b", "c"]:
            print("Invalid input! Try again...")
            gym_employee_position_choice = input("Choose a letter of a position from above (a, b or c): ")

        gym_employee_position = ""
        match gym_employee_position_choice:
            case "a":
                gym_employee_position = "Receptionist"
            case "b":
                gym_employee_position = "Trainer"
            case "c":
                gym_employee_position = "Cleaner"

        gym_employee_dict = {"Name": gym_employee_name,
                             "Surname": gym_employee_surname,
                             "jmbg": gym_employee_jmbg,
                             "Phone number": gym_employee_phone_number,
                             "email": gym_employee_email,
                             "Address": gym_employee_address,
                             "Position": gym_employee_position}

        if not os.path.exists("gym_employees"):
            os.mkdir("gym_employees")

        os.chdir("gym_employees")

        with open(f"{gym_employee_name}_{gym_employee_surname}_{gym_employee_position}.txt", "w") as f:
            for key in gym_employee_dict:
                f.write(f"{key}: {gym_employee_dict.get(key)}\n")

        os.chdir("../")

    def fire_employee(self):

        while True:
            gym_employee_name = input("Enter your name: ")
            gym_employee_surname = input("Enter your surname: ")
            gym_employee_position = input("Enter your position: ")

            if os.path.exists(f"gym_employees/{gym_employee_name}_{gym_employee_surname}_{gym_employee_position}.txt"):
                os.chdir("gym_employees")
                os.remove(f"{gym_employee_name}_{gym_employee_surname}_{gym_employee_position}.txt")
                os.chdir("../")
                break
            else:
                print("That employee doesn't exist. Please check if you typed everything correctly!")
                continue
