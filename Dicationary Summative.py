files = {}

def add_items():
    exit = False
    while exit == False:
        key = input("What do you want to shop for? Type 'exit' to be done > ").lower()
        if key == "exit":
            exit = True
        elif key != "exit":
            value = input("How much is it $")
            print("Adding", value, key)
            files[key] = value
            print(files)
        

def remove_items():
    exit = False
    while exit == False:
        for (key, value) in files.items():
            print("You got so far", key)
        key = input("What do you want to remove? Type 'exit' to exit > ").lower()
        if key == "exit":
            exit = True
        elif key != "exit":
            if key in files:
                print("Erasing", key)
                del files[key]
            else:
                print("your done, try again")

def print_items():
    for (key,value) in files.items():
        print("You have $",value, key)

def main():
    go = 1
    while go == 1:
        print("Welcome to the Shop")
        print("What would you like to do?")
        choice = input("Shop, View, Remove, Leave The Store? ").lower()
        if choice == "shop":
            add_items()
        elif choice == "view":
            print_items()
        elif choice == "remove":
            remove_items()
        elif choice == "leave the store":
            go = 0
            print("You left the store have a Good Day :)!!!")
        else:
            print("Try again")
            
main()