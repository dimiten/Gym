from gym import Gym


python_gym = Gym(name="Python gym", address="Pajtonska ulica 6", phone_number="+38163415341",
                 email="pythongym@gmail.com", pib="321431934")


def main():
    print("Welcome to the Python Gym!\n"
          "Please choose an option you want from bellow (type in a letter of an option you want):\n"
          "a) Join gym\n"
          "b) Quit gym\n"
          "c) Enter gym\n"
          "d) Leave gym\n"
          "e) Weight in\n"
          "f) Show all members of the gym\n"
          "g) Show all members with for a specific plan\n"
          "h) Show monthly and yearly income of the gym\n"
          "i) Show monthly and yearly income for a specific plan\n"
          "j) Percentage of members with a specific plan\n"
          "k) Show all members that are currently in the gym\n"
          "l) Hire an employee\n"
          "m) Fire an employee\n"
          "n) Reset times trained of a gym member\n"
          "o) End program\n")

    while True:

        choice = input("\nChoose a letter of an option you want (choose \"o\" if you want to end the program): ")

        match choice:
            case "a":
                python_gym.join_gym()
                continue
            case "b":
                python_gym.quit_gym()
                continue
            case "c":
                python_gym.enter_gym()
                continue
            case "d":
                python_gym.leave_gym()
                continue
            case "e":
                python_gym.weight_in()
                continue
            case "f":
                python_gym.print_all_members()
                continue
            case "g":
                python_gym.print_all_members_for_plan()
                continue
            case "h":
                python_gym.monthly_and_yearly_profit()
                continue
            case "i":
                python_gym.monthly_and_yearly_profit_for_plan()
                continue
            case "j":
                python_gym.percentage_for_plan()
                continue
            case "k":
                python_gym.print_members_in_gym()
                continue
            case "l":
                python_gym.hire_employee()
                continue
            case "m":
                python_gym.fire_employee()
                continue
            case "n":
                python_gym.reset_times_trained()
                continue
            case "o":
                print("Ending program...")
                break
            case other:
                print("Invalid input! Choose only a letter of an option you want! Try again...")
                continue


if __name__ == "__main__":
    main()
