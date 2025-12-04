import csv
import os

def start_employee_file():
    """Create the csv file if it does not exist"""
    if not os.path.exists('employees.csv'):
        with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['employee_id', 'full_name', 'position', 'area', 'contract_start_date'])

def register_employee():
    """Register a new employee"""
    start_employee_file()
    
    print("\n--- REGISTER EMPLOYEE ---")
    employee_id = input("Employee ID: ")
    full_name = input("Full name: ")
    position = input("Position: ")
    area = input("Area: ")
    contract_start_date = input("Contract start date (DD/MM/YYYY): ")
    
    with open('employees.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([employee_id, full_name, position, area, contract_start_date])
    
    print(f"\n✓ Employee {full_name} registered successfully")
    input("Press Enter to continue...")

def list_employees():
    """Show all registered employees"""
    start_employee_file()
    
    print("\n--- EMPLOYEE LIST ---")
    
    with open('employees.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        employees = list(reader)
        
        if not employees:
            print("No employees registered")
        else:
            for emp in employees:
                print(f"\nID: {emp['employee_id']}")
                print(f"Name: {emp['full_name']}")
                print(f"Position: {emp['position']}")
                print(f"Area: {emp['area']}")
                print("-" * 40)
    
    input("\nPress Enter to continue...")

def search_employee():
    """Show detailed information of an employee"""
    start_employee_file()
    
    print("\n--- SEARCH EMPLOYEE ---")
    employee_id = input("Enter employee ID: ")
    
    with open('employees.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        found = False
        
        for emp in reader:
            if emp['employee_id'] == employee_id:
                print(f"\n{'='*40}")
                print(f"ID: {emp['employee_id']}")
                print(f"Name: {emp['full_name']}")
                print(f"Position: {emp['position']}")
                print(f"Area: {emp['area']}")
                print(f"Contract start date: {emp['contract_start_date']}")
                print(f"{'='*40}")
                found = True
                break
        
        if not found:
            print(f"\n✗ Employee with ID {employee_id} not found")
    
    input("\nPress Enter to continue...")

def main_employees():
    """Employee management menu"""
    while True:
        print("\n" + "="*50)
        print("   EMPLOYEE MANAGEMENT")
        print("="*50)
        print("1. Register employee")
        print("2. List employees")
        print("3. Search employee")
        print("4. Return to main menu")
        print("="*50)
        
        option = input("\nSelect an option: ")
        
        if option == "1":
            register_employee()
        elif option == "2":
            list_employees()
        elif option == "3":
            search_employee()
        elif option == "4":
            break
        else:
            print("\n✗ Invalid option")
            input("Press Enter to continue...")
