def main_menu():
    """
    This function will display menu to the user

    return: None
    """
    while True:
        print("===== LT POS =====", end="\n\n")
        print("1. Sale")
        print("2. Inventory")
        print("3. Exit", end="\n\n")
        option = input("Select an option: ")

        if option.isnumeric():
            if option == "1":            
                print("You have Selected the Sale.")
            elif option == "2":         
                print("You have selected the Inventory.")
            elif option == "3":         
                print("Good Bye")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        else:
            print("Invalid option. Please enter a number.")

if __name__ == "__main__":   # ✅ Outside the function, not inside the while loop
    main_menu()
