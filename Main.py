import os
from Users import validate_credentials
from Employees import main_employees
from Holidays import main_holidays
from Reports import generate_report

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    """Show the main menu"""
    print("\n" + "="*50)
    print("   HOLIDAY MANAGEMENT SYSTEM  -  RIWI")
    print("="*50)
    print("1. Employee management")
    print("2. Vacation management")
    print("3. Generate reports CSV")
    print("4. Exit")
    print("="*50)

def main():
    """Main function of the program"""
    clear_screen()
    
    print("\n" + "="*50)
    print("     LOGIN  -  PEOPLE OPERATIONS")
    print("="*50)
    
    user = input("\nUSER: ")
    password = input("Password: ")
    
    if validate_credentials(user, password):
        print("\n✓ Successful login")
        input("Press Enter to continue...")
        
        while True:
            clear_screen()
            show_main_menu()
            option = input("\nSelect an option: ")
            
            if option == "1":
                main_employees()
                
            elif option == "2":
                main_holidays()
                
            elif option == "3":
                generate_report()
                
            elif option == "4":
                print("\n¡Good bye!")
                break
            
            else:
                print("\n✗ Invalid option")
                input("Press Enter to continue...")
    
    else:
        print("\n✗ Incorrect credentials")

if __name__ == "__main__":
    main()
