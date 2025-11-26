#Operating System
#Read rute of files
#Clear screen of the console
import os

from Users import validate_credentials

from Employees import main_employees

from Holidays import main_holidays

from Reports import generate_report

#Os.system: execute code as if you were in the terminal
#Os.name:  Returns the name of the operating system
#Def: Define function to clear the console
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

#Show the main menu literrally with decorations     
def show_main_menu():
    print("\n" + "="*50)
    
    print("Holiday Management System  -  RIWI")
    
    print("="*50)
    
    print("1.  Employee management")
    
    print("2.  Vacation management")
    
    print("3.  Generate reports CSV")
    
    print("4.  Exit")
    
    print("="*50)
    
#Main function of the program    
def main():
    clear_screen()
    
    print("\n" + "="*50)
    
    print("     LOGIN  -     PEOPLE OPERATIONS      ")
    
    print("="*50)

#Asks the user to enter their username and saves it in the user variable    
    user = input("\nUSER:  ")
#Asks the user to enter their password and saves it in the password variable   
    password = input("Password:  ")
    
    if validate_credentials(user, password):
        print("\n Sucessful login ")
        input("press enter to continue")
    
    
    while True:
        clear_screen()
        show_main_menu()
        option = input("\Select an option: ")
        
        if option == "1":
            main_employees()
            
        elif option == "2":
            main_holidays()
            
        elif option == "3":
            generate_report()
            
        elif option == "4":
            print("\n Good bye...")
            break
        
        else:
            print("\n Invalid option")
            input("Press enter to continue...")
            
    else:
        print("\n Incorrect credentials")
        
if __name__ == "__main__":
    main()