
def main_menu():
   """
            This function will display menu to the user 

   return:None
   """
while True:
       print("===== LT POS =====", end="\n\n")
       print("1. Sale")
       print("2. Inventary")
       print("3. Exit", end="\n\n")
       option = input("Select an option ")
       if option.isnumeric():
          if option == 1:
              print("You have Selected the Sale :")
          elif option == 2:
               print("You have selected the Inventary : ")
          elif option == 3:
               print("Good Bye")
               break
          else:
             print("Invalid option ")
       else:
           print("Invalid option ")
def add_items(itemname:str,
              description:str,
              price:int|float,
              quantity:int)->bool:
    print("Enter the itemname: ")
    itemname=input("Enter the itemname: ")
    print("Enter the price: ")
    price=input("Enter the price: ")
    print("Enter the quantity: ")
    quantity = input("Enter the quantity: ")










if __name__ == "__main__":
    main_menu()
